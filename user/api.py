from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from lib.http import render_json
from lib.sms import send_sms

from common import keys
from common import errors


def submit_phone(request):
    """提交手机号，发送验证码"""
    phone = request.POST.get("phone")
    send_sms(phone)
    return render_json(None)


def submit_vcode(request):
    """提交验证码 登录"""
    phone = request.POST.get("phone")
    vcode = request.POST.get("vcode")

    cache_vcode = cache.get(keys.VCODE_KEY % phone)
    if vcode == cache_vcode:
        #登录
        pass
    else:
        return render_json("验证码错误", errors.VCODE_ERR)
    return None

def get_profile(request):
    """获取个人资料"""
    return None

def set_profile(request):
    """设置个人资料"""
    return None

def upload_avatar(request):
    """上传头像"""
    return None