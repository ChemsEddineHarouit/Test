from django.urls import path, include
from rest_framework import routers
from Book.views import BookCreateView
from .api.views import AuthorAPIViewSet
from .views import AuthorListView, AuthorCreateView, AuthorDetailView, AuthorDeleteView, AuthorUpdateView
app_name = 'author'

urlpatterns = [
    path('detail/<int:pk>/', AuthorDetailView.as_view(), name='detail'),
    path('list/', AuthorListView.as_view(), name='list'),
    path('create/', AuthorCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AuthorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete'),
    path('<int:owner>/create/book/', BookCreateView.as_view(), name='create-book'),
]



router = routers.DefaultRouter()
router.register(r'', AuthorAPIViewSet, basename='authors')
urlpatterns += router.urls