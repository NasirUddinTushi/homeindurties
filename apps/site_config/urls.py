from django.urls import path
from .views import SiteFeatureAPIView, SocialLinksAPIView

urlpatterns = [
    path("features/", SiteFeatureAPIView.as_view(), name="site-features"),
    path("social-links/", SocialLinksAPIView.as_view(), name="social-links"),
]
