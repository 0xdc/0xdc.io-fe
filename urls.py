from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('frontend.urls', namespace="frontend")),
]
