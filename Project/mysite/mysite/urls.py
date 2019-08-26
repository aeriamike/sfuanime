from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("tinymce/", include('tinymce.urls')),
    path("summernote/", include('django_summernote.urls')),
    path("admin/", admin.site.urls),
    path("sfuanime/", include("sfuanime.urls"))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
