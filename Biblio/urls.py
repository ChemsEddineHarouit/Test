
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .view import homeView

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('author/', include('Author.urls', namespace='author')),
    path('book/', include('Book.urls', namespace='book'))
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
