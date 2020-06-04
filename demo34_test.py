# 需要调用user这个package中的user_center.py模块中的一个方法
# import demo33_order
# import demo33_order as order
# form demo33_order import *
# from demo33_order import cala

# import user.user_center
# user.user_center.login()
# from user.user_center import *
# login()

# 以下用法需要__all__导出模块
# import user
# user.user_center.login()
from user import *
user_center.login()
import user
user.user_center.login()
