# 任务

import traceback
from service.request import zhihu_req_get
from service.member import add_member, member_exists, add_member_follower, update_member_followers
import logging
import django_rq

logger = logging.getLogger(__name__)


def enqueue_rq(func, **kwargs):
    """
        进入 rq 队列
    :param func:
    :param queue_name:
    :param kwargs:
    :return:
    """
    django_rq.enqueue(func=func, **kwargs)


def generate_follower_url(url_token):
    """
        生成关注着 url
    :param url_token: 
    :return: 
    """
    return "http://www.zhihu.com/api/v4/members/%s/followers" % url_token


def zhihu_spider_followers_by_token(url_token="", first=False, type="f"):
    """
        知乎 爬虫
    :return:
    """
    try:
        follower_url = generate_follower_url(url_token=url_token)
        if first:
            # 初始阶段
            if not member_exists(url_token=url_token):
                raise Exception(u"first url_token should exists 。。。")
        result = zhihu_req_get(url=follower_url)
        paging = result.get("paging", {})
        update_member_followers(
            url_token=url_token,
            totals=paging.get("totals"))
        zhihu_spider_followers_next(paging=paging, url_token=url_token)
        followers = result.get("data", [])
        for follower in followers:
            follower_member = add_member(data=follower)
            add_member_follower(
                member_url_token=url_token,
                follower_id=follower_member.id)
            enqueue_rq(func=zhihu_spider_followers_by_token, url_token=url_token)
    except Exception as e:
        print("error %s" % traceback.format_exc())
        logger.error("error %s" % traceback.format_exc())


def zhihu_spider_followers_by_url(next_url, url_token, type="f"):
    """
        知乎 爬虫
    :return:
    """
    try:
        print("url_token %s in follow by next" % url_token)
        result = zhihu_req_get(url=next_url)
        paging = result.get("paging", {})
        zhihu_spider_followers_next(paging=paging, url_token=url_token)
        followers = result.get("data", [])
        for follower in followers:
            follower_member = add_member(data=follower)
            add_member_follower(
                member_url_token=url_token,
                follower_id=follower_member.id)
    except Exception as e:
        logger.error("error %s" % traceback.format_exc())


def zhihu_spider_followers_next(paging, url_token):
    """
        知乎爬虫分页
    :param paging:
    :return:
    """
    print("url %s in next" % url_token)
    if paging.get("is_end", False):
        return
    next_url = paging.get("next")
    enqueue_rq(func=zhihu_spider_followers_by_url, next_url=next_url, url_token=url_token)
