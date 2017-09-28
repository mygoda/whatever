from django.db.models.signals import pre_save
from django.dispatch import receiver
import logging
from zhihu.models import MemberFans, ZhihuMember

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=ZhihuMember)
def add_member_signal(sender, **kwargs):
    """
      生成调度器
    :param sender: 
    :param kwargs: 
    :return: 
    """
    member = kwargs['instance']
    created = kwargs['created']
    logger.info("member %s in schedule signal created %s ..." % (member.id, created))