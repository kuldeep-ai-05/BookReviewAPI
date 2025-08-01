from rest_framework import generics,permissions,status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Book , Review
from .serializers import BookSerializer, ReviewSerializer, UserRegisterSerializer
from .permissions import IsRevieworReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

#Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser|permissions.IsAuthenticatedOrReadOnly]

    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['author','genre','published_year']
    search_fields=['title','author']
    ordering_fields=['published_year','title']

    def get_permissions(self):
        if self.request.method=='POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser|permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

#Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['rating','reviewer__username','book']
    search_fields=['text']
    Ordering_fields=['created_at','rating']

    def get_queryset(self):
        queryset=Review.objects.all()
        book_id=self.request.query_params.get('book')
        if book_id:
            queryset=queryset.filter(book__id=book_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsRevieworReadOnly]

class UserRegisterView(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    permission_classes=[AllowAny]

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        refresh=RefreshToken.for_user(user)

        return Response({
            "user":{"username":user.username,"id":user.id},
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        },status=status.HTTP_201_CREATED)
