# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Banner
from .models import Expection
from .models import Experience
from .models import SNS
from .models import Skill
from .models import User
from .models import Works

# Register your models here.

admin.site.register(Banner)
admin.site.register(User)
admin.site.register(SNS)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Works)
admin.site.register(Expection)
