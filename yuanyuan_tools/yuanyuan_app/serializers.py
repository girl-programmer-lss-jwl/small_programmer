from rest_framework import serializers
from yuanyuan_app.models import Users, WechatUsers, BirthdayLogs, BIRTHDAY_TYPE, GENDER_TYPE


class UserSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    wechat_user_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    birthday_type = serializers.ChoiceField(choices=BIRTHDAY_TYPE)
    birthday = serializers.DateTimeField(required=True)
    avatar_name = serializers.CharField(required=False)
    phone_name = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = '__all__'


class WechatUserSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_TYPE)
    city = serializers.CharField(required=True)
    province = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    language = serializers.CharField(required=True)

    class Meta:
        model = WechatUsers
        fields = '__all__'


class BirthdayLogsSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    birthday_type = serializers.ChoiceField(choices=BIRTHDAY_TYPE)
    birthday = serializers.DateTimeField(required=True)
    avatar_name = serializers.CharField(required=False)
    phone_name = serializers.CharField(required=False)

    class Meta:
        model = BirthdayLogs
        fields = '__all__'
