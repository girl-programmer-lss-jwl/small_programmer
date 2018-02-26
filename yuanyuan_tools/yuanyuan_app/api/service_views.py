from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from yuanyuan_app import serializers, models


class WechatUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WechatUserSerializer
    queryset = models.WechatUsers.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()


class BirthdayLogViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BirthdayLogsSerializer
    queryset = serializers.BirthdayLogs.objects.all()
