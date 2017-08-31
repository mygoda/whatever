
# 请求封装
import requests
from common.models import ZhihuAuthorization
import json
import logging


logger = logging.getLogger(__name__)


def zhihu_req_result(response):
    """
        知乎返回是否成功
    :param response: 
    :return: 
    """
    if response.ok:
        content = response.content
        result = json.loads(content)
        if result.get("error"):
            logger.error("get zhihu response error %s" % result)
            raise Exception("error %s" % result)
        return result


def zhihu_req_get(url):
    """
        知乎
    :param methed: 
    :param url: 
    :param data: 
    :return: 
    """
    headers = {"authorization": ZhihuAuthorization.header_value()}
    response = requests.get(url, headers=headers)
    result = zhihu_req_result(response=response)
    return result



