from django.db import models
from common.models import CommonModelMixin
# Create your models here.


class ZhihuMember(CommonModelMixin, models.Model):
    """
        知乎用户
    """

    SEX = (
        ("1", "男"),
        ("-1", "女")
    )

    name = models.CharField(u"姓名", max_length=128)
    gender = models.CharField(u"性别", default="1", max_length=2, choices=SEX)
    user_type = models.CharField(u"用户类型", max_length=16, null=True, blank=True)
    url_token = models.CharField(u"用户URL", max_length=32, unique=True)
    is_advertiser = models.BooleanField("是否广告", default=False)
    avatar_url = models.CharField(u"头像", max_length=255)
    is_org = models.BooleanField(u"是否组织", default=False)
    type = models.CharField(u"类型", max_length=32)
    zhihu_id = models.CharField(u"知乎ID", max_length=36, unique=True)
    headline = models.CharField(u"headline", max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class MemberFans(CommonModelMixin, models.Model):
    """
        用户粉丝
    """

    member = models.ForeignKey(ZhihuMember, verbose_name=u"被关注", related_name=u"member")
    fans = models.ForeignKey(ZhihuMember, verbose_name=u" 关注者", related_name=u"fans")
    is_valid = models.BooleanField(u"是否有效", default=True)

    def __str__(self):
        return "mem: %s, fans: %s" % (self.member.name, self.fans.name)


