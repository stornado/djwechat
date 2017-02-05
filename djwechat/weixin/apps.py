from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WeixinConfig(AppConfig):
    name = 'weixin'
    verbose_name = _('WEIXIN')
