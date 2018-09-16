from accounts.views import (
    AccountPasswordResetCompleteView,
    AccountPasswordResetConfirmView,
    AccountPasswordResetDoneView,
    AccountPasswordResetView,
)
from articles.views import ArticleListView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('password-reset-confirm/<uidb64>/<token>/', AccountPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', AccountPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset/', AccountPasswordResetView.as_view(), name='account-password-reset'),
    path('password-reset/done/', AccountPasswordResetDoneView.as_view(), name='account-password-reset-done'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
