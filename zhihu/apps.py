from django.apps import AppConfig


class ZhihuConfig(AppConfig):
    name = 'zhihu'


    def ready(self):
        """
            信号处理设置
        :return: 
        """
        import zhihu.signals

