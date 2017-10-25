from django.conf.urls import url

from common.views import HealthCheck


urlpatterns = [
    url(r'^health-check/$', HealthCheck.as_view(), name='health_check'),
]
