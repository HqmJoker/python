# 如何自己触发一个错误并进行错误消息解析

try:
    # 手工触发错误
    raise(NameError(300))
except NameError as msg:
    print(msg)