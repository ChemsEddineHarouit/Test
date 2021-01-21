from django.urls import path
from rest_framework import routers
from .api.views import BookAPIViewSet
from.views import BookListView, BookCreateView, BookDetailView, BookDeleteView, BookUpdateView

app_name = 'book'

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('list/', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
]

router = routers.DefaultRouter()
router.register(r'', BookAPIViewSet, basename='books')
urlpatterns += router.urls