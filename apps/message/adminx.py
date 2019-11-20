########################################################################################################################
## Django 自带模块导入
########################################################################################################################

########################################################################################################################
## 系统自带模块导入
########################################################################################################################
import xadmin

########################################################################################################################
## 自建模块导入
########################################################################################################################
from .models import *


########################################################################################################################
## 注册反馈消息到后台
########################################################################################################################
class UserFeedbackMessageAdmin(object):
    list_display = ['user', 'add_time']
    search_fields = ['user', 'message']
    list_filter = ['user', 'add_time']

xadmin.site.register(UserFeedbackMessage, UserFeedbackMessageAdmin)


########################################################################################################################
## 注册用户消息到后台
########################################################################################################################
class UserMessageAdmin(object):
    list_display = ['send_user', 'send_to', 'add_time']
    search_fields = ['send_user', 'send_to', 'msg_content']
    list_filter = ['send_user', 'send_to', 'add_time']

xadmin.site.register(UserMessage, UserMessageAdmin)


########################################################################################################################
## 注册用户评论到后台
########################################################################################################################
class UserCommentAdmin(object):
    list_display = ['send_user', 'user_msg', 'add_time']
    search_fields = ['send_user', 'user_msg', 'cmt_content']
    list_filter = ['send_user', 'add_time']

xadmin.site.register(UserComment, UserCommentAdmin)


########################################################################################################################
## 注册用户是的读取到后台
########################################################################################################################
class UserReadMessageAdmin(object):
    list_display = ['user', 'msg', 'is_read', 'add_time']
    search_fields = ['user', 'msg', 'is_read']
    list_filter = ['user', 'is_read', 'add_time']

xadmin.site.register(UserReadMessage, UserReadMessageAdmin)






