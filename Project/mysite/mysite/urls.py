from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
<<<<<<< HEAD
=======
    path("tinymce/", include('tinymce.urls')),
    path("summernote/", include('django_summernote.urls')),
>>>>>>> 73f157eac73a6ce53f5775d16b5e182438dd4a21
    path("admin/", admin.site.urls),
    path("sfuanime/", include("sfuanime.urls"))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
