from django import template
from datetime import datetime
register = template.Library()

@register.filter
def time_since(value):
    #距离现在的时间间隔 用秒来对比
    #如果时间小于1分钟 刚刚
    #小于一个小时  几分钟之前
    #小于24小时  几小时之前
    #小于30天 几天之前
    #其余就是显示年月日

    if not isinstance(value,datetime):
        return value

    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif timestamp >= 60 and timestamp < 60*60:
        minutes = int(timestamp/60)
        return "%s分钟以前" % minutes
    elif timestamp >= 60*60 and timestamp < 60*60*24:
        minutes = int(timestamp/60/60)
        return "%s小时以前" % minutes
    elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
        minutes = int(timestamp/60/60/24)
        return "%s天以前" % minutes
    else:
        return value.strftime("%Y/%m/%d %H/%M ")
