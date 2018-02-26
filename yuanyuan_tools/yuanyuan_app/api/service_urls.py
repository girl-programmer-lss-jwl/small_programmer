# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from yuanyuan_app.api import service_views


router = DefaultRouter()
router.register(r'wechat_users', service_views.WechatUserViewSet)
router.register(r'users', service_views.UserViewSet)
router.register(r'birthday_logs', service_views.BirthdayLogViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
