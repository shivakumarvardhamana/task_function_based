from django.urls import path,include
# from .views import blog_api,likes_api,user_api

from .views import blob,blob1,like,like1,use,use1,owner
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# import rest_framework
# router.register('api',blog_api,basename="api")
# router.register('api1',likes_api,basename="api1")
# router.register('api2',user_api,basename="api2")
# urlpatterns=[
#     path('',include(router.urls)),
#     path('api',include('rest_framework.urls')),

# ]

urlpatterns=[
    # path('api/',blob1),
    path('blog_api/',blob,name="blog_api"),
    path('blog_api/<int:pk>/',blob1,name="blog_api"),
    path('like_api1/',like,name="blog_api"),
    path('like_api1/<int:pk>/',like1,name="blob_api"),
    path('user_api/',use,name="user_api"),
    path('user_api/<int:pk>/',use1,name="user_api"),
    path('owner/',owner,name='owner_api'),
    path('api1/',include('rest_framework.urls')),
#     path('api2/')
 ]