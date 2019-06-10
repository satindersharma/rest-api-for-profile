from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset,base_name='hello-viewset')
router.register('profile', views.UserProfileViewset)
router.register('login', views.LoginViewset, base_name='login')
'''becouse its a model viewset we don't neet to specify a base_name'''
router.register('feed', views.UserProfileFeedViewset)

urlpatterns = [
    url(r'^hello-view/', views.HelloAPI.as_view()),
    url(r'', include(router.urls)),
]