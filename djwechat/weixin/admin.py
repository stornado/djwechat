from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import CorpMenu
from models import MPMenu
from models import WeixinCorp
from models import WeixinMP
# Register your models here.


class WeixinMpAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('appid', 'name', 'secret')}),
        (_('Advanced options'), {
         'fields': ('token', 'aes_key', 'access_token', 'expire_time')
         }),
    )


class WeixinCorpAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('corpid',)}),
        (_('Team'), {'fields': ('name', 'secret')}),
        (_('Agent'), {'fields': ('agentid', 'agent_name')}),
        (_('Advanced options'), {
         'fields': ('token', 'aes_key', 'access_token', 'expire_time')
         }),
    )


admin.site.register(WeixinMP, WeixinMpAdmin)
admin.site.register(WeixinCorp, WeixinCorpAdmin)
admin.site.register(MPMenu)
admin.site.register(CorpMenu)
