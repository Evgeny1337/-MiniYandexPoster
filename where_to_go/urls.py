from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', views.get_place_by_id, name='place-detail'),
    path('', views.show_start),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
