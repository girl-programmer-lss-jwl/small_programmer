from rest_framework import serializers
from yuanyuan_tools.yuanyuan_app.models import Users, WechatUsers, BirthdayLogs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    wechat_user_id = serializers.IntegerField

    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class WechatUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WechatUsers
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class BirthdayLogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BirthdayLogs
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
