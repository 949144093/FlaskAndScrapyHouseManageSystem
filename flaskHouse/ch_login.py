from flask import url_for,redirect,session
from functools import wraps


#管理员登录状态检查装饰器
def is_admin_login(func):
    @wraps(func)
    def check_login(*args,**kwargs):
        user=session.get('user')
        if user=='admin':
            return func(*args,**kwargs)
        else:
            return redirect('/login')
    return check_login

#任意用户登录状态检查装饰器
def is_user_login(func):
    @wraps(func)
    def check_login(*args,**kwargs):
        user=session.get('user')
        if user:
            return func(*args,**kwargs)
        else:
            return redirect('/login')
    return check_login