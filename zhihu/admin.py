from django.contrib import admin
from common.models import ZhihuAuthorization, ZhihuStartMember
from zhihu.models import MemberFans, ZhihuMember
# Register your models here.

admin.site.register(ZhihuStartMember)
admin.site.register(ZhihuAuthorization)
admin.site.register(ZhihuMember)
admin.site.register(MemberFans)