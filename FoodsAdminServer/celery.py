from __future__ import absolute_import

from celery import Celery

import os

# 设置celery启动环境变量
from FoodsAdminServer import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'FoodsAdminServer.settings')


# 创建Celery应用对象
app = Celery('foods-server')

# 配置,拿到__init__()下的脚本对象settings
app.config_from_object('django.conf:settings')

# 自动扫描task函数
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)




