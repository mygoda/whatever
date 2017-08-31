from django.db import models
from django.contrib.contenttypes.models import ContentType
from service.uuids import create_uuid

# Create your models here.


class CommonModelMixin(models.Model):

    id = models.CharField(u"UID", max_length=36, primary_key=True, default=create_uuid)
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

    @classmethod
    def header_value(cls):
        return cls.objects.all()[0].value


class ZhihuStartMember(models.Model):

    url_token = models.CharField(u"url", max_length=255)
    is_valid = models.CharField(u"是否有效", default=True)