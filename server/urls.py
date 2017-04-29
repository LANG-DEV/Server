from django.conf.urls import url, include
from rest_framework import routers
from api_routes import auth_routes

router = routers.DefaultRouter()
#router.register(r'api/v1', )

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', auth_routes.login)
]

