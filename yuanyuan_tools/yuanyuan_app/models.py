# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


"""
MODEL
birthday_logs:
    id, user_id, name, birthday_type, birthday, avatar_url(nullable), phone_number(nullable)
wechat_users:
    id, nickname, avatar_url, gender, city, country, province, language
users:
    id, wechat_user_id, name, birthday_type, birthday, avatar_url(nullable), phone_number(nullable)
"""
BIRTHDAY_TYPE = (
    ('0', 'NULL'),
    ('1', '阳历'),
    ('2', '农历'),
)


GENDER_TYPE = (
    ('0', 'NULL'),
    ('1', 'MALE'),
    ('2', 'FEMALE'),
)


class BirthdayLogs(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=45)
    birthday_type = models.IntegerField(BIRTHDAY_TYPE, default=BIRTHDAY_TYPE[0])
    birthday = models.DateTimeField()
    avatar_url = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'birthday_logs'
        verbose_name = u'生日信息'


class Users(models.Model):
    wechat_user_id = models.IntegerField()
    name = models.CharField(max_length=45)
    birthday_type = models.IntegerField(BIRTHDAY_TYPE, default=BIRTHDAY_TYPE[0])
    birthday = models.DateTimeField()
    avatar_url = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'users'
        verbose_name = u'用户表'


class WechatUsers(models.Model):
    nickname = models.CharField(max_length=45)
    avatar_url = models.CharField(max_length=2000)
    gender = models.IntegerField(GENDER_TYPE, default=GENDER_TYPE[0])
    city = models.CharField(max_length=45)
    province = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'wechat_users'
        verbose_name = u'用户微信信息'
