from rest_framework import generics,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Book , Review
from .serializers import BookSerializer, ReviewSerializer
from .permissions import IsRevieworReadOnly

#Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser|permissions.IsAuthenticatedOrReadOnly]

    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['author','genre','published_year']
    search_fields=['title','author']
    ordering_fields=['published_year','title']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAdminUser|permissions.IsAuthenticatedOrReadOnly]

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
