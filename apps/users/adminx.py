# -*- coding: utf-8 -*-
import xadmin
from users.models import EmailVerifyRecord, Banner
from xadmin import views

__author__ = 'SheepYang'
__date__ = '2018/4/10 14:31'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GolbalSettings(object):
    site_title = '绿洲教育后台管理系统'
    site_footer = '绿洲科技'
    menu_style= 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GolbalSettings)
