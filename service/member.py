from zhihu.models import ZhihuMember, MemberFans


def member_exists(url_token):
    """
        用户是否已经存在
    :param user_token:
    :return:
    """
    return ZhihuMember.objects.filter(url_token=url_token).exists()


def add_member(data):
    """
        添加成员
    :param data:
    :return:
    """
    url_token = data.get("url_token")
    member = {
        "name": data.get("name"),
        "avatar_url": data.get("avatar_url"),
        "gender": data.get("gender"),
        "headline": data.get("headline"),
        "zhihu_id": data.get("id"),
        "user_type": data.get("user_type"),
        "url_token": data.get("url_token"),
        "is_org": data.get("is_org"),
        "type": data.get("type"),
        "is_advertiser": data.get("is_advertiser")
    }
    if member_exists(url_token):
        update_count = ZhihuMember.objects.filter(url_token=url_token).update(**member)
        return ZhihuMember.objects.get(url_token=url_token)
    member_item = ZhihuMember(**member)
    member_item.save()
    return member_item


def update_member_followers(url_token, totals):
    """
        更新用户追随者信息
    :param member:
    :return:
    """
    member = ZhihuMember.objects.get(url_token=url_token)
    member.followers = totals
    member.save()


def update_member_followees(url_token, totals):
    """
        更新用户关注了信息
    :param member:
    :return:
    """
    member = ZhihuMember.objects.get(url_token=url_token)
    member.followees = totals
    member.save()


def add_member_follower(member_url_token, follower_id):
    """
        添加关注关系
    :param member_url_token: 
    :param follower_id: 
    :return: 
    """
    member = ZhihuMember.objects.get(url_token=member_url_token)
    member_fans, created = MemberFans.objects.get_or_create(member_id=member.id, fans_id=follower_id)


