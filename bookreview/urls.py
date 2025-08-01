from django.urls import path
from .views import (
    BookListCreateView, BookDetailView,
    ReviewListCreateView, ReviewDetailView, UserRegisterView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #user registration (returns JWT tokens)
    path('api/register/',UserRegisterView.as_view(),name='user-register'),

    #JWT Auth
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair_view'), #login
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

    # Book endpoints
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Review endpoints
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
