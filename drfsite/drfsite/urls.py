"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers
class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]
# router = routers.SimpleRouter()
# router = routers.DefaultRouter()
router = MyCustomRouter()

router.register(r'women', WomenViewSet, basename='women')

#router = routers.DefaultRouter()
print(router.urls)
#api/v1/women
#[<URLPattern '^women/$' [name='women-list']>,
# <URLPattern '^women\.(?P<format>[a-z0-9]+)/?$' [name='women-list']>,

#api/v1/women/pk
# <URLPattern '^women/(?P<pk>[^/.]+)/$' [name='women-detail']>,
# <URLPattern '^women/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='women-detail']>,
#
# api/v1
# <URLPattern '^$' [name='api-root']>,
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)), #http://127.0.0.1:8000/api/v1/women/
    # path('api/v1/womenlist/', WomenAPIView.as_view()),
    # # path('api/v1/womenlist/<int:pk>/', WomenAPIView.as_view()),
    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),


]
