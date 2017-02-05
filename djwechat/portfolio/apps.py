from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = _('Portfolio')
