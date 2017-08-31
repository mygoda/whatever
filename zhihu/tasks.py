# 任务

import celery
from service.request import zhihu_req_get


@celery.task
def zhihu_spider(url=""):
    """
        知乎 爬虫
    :return: 
    """
    result = zhihu_req_get(url=url)
    