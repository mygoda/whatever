from django.db import models
from django.contrib.contenttypes.models import ContentType
from service.uuids import create_uuid

# Create your models here.


class CommonModelMixin(models.Model):

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s, %s" % (self.__class__.__name__, self.id)


class ZhihuAuthorization(models.Model):
    """
        知乎 header 头
    """

    value = models.CharField(u"值", max_length=255)
    UDID = models.CharField(u"UUID", max_length=255, null=True, blank=True)
    agent = models.TextField(u"浏览器代理", default="", null=True, blank=True)

    @classmethod
    def header_value(cls):
        item = cls.objects.all()[0]
        headers = {
            "authorization": item.value,
            "X-UDID": item.UDID,
            "User-Agent": item.agent
        }
        return headers


class ZhihuStartMember(models.Model):

    url_token = models.CharField(u"url", max_length=255)
    is_valid = models.BooleanField(u"是否有效", default=True)