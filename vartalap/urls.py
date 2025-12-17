from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vartalap.accounts.views import welcome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("vartalap.accounts.urls")),
    path("", welcome, name="home"),
    path("chat/", include("vartalap.chats.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
