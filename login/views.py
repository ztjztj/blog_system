from django.shortcuts import render, HttpResponse, reverse, redirect
from body.models import *
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

from VerificationCode import send_sms, get_code
from django.http import JsonResponse


# Create your views here.


# 写登陆
def login(request):
    if request.method == "GET":
        return render(request, 'register1.html')
    else:
        user_numbers = request.POST.get('tel')
        user_password = request.POST.get('pwd')
        print(user_numbers, user_password)
        try:
            jud = UserInfo.objects.get(user_numbers=user_numbers, user_password=user_password)
            if jud:
                request.session['user_id'] = jud.id
                request.session['user_numbers'] = user_numbers
                return JsonResponse({"res": 1})
        except Exception:
            return JsonResponse({"res": 0})


def register(request):
    if request.method == "GET":
        return render(request, 'register1.html')
    else:
        # 第一个页面，获取到用户注册的手机号和密码(用手机号作为账户)
        user_tel = request.POST.get('tel')

        a = get_code(6, False)
        send_sms(user_tel, a)
        request.session['lyzm'] = a
        request.session['rtel'] = user_tel
        if user_tel:
            return JsonResponse({"res": 1})
        else:
            return JsonResponse({"res": 0})


def zhuce(request):
    # 获取到验证码
    yzm = request.session.get('lyzm')
    # 获取到手机号
    tel = request.session.get('rtel')
    # 获取到名称
    name = request.POST.get('name')
    # 获取到密码
    pwd = request.POST.get('pwd')
    # 获取到验证码
    uyzm = request.POST.get('yzm')

    try:
        a = UserInfo.objects.get(user_numbers=tel)
        if a:
            return JsonResponse({"res": '用户名已经存在'})

    except UserInfo.DoesNotExist:
        if yzm == uyzm:
            UserInfo.objects.create(user_numbers=tel, user_password=pwd, user_name=name)
            return JsonResponse({"res": "注册成功"})
        else:
            return JsonResponse({"res": "验证码错误"})


# 图片验证码
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('F:/code/xiwang/blog_system/login/FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# 忘记密码
# 返回页面
def forgetpassword(request):
    if request.method == "GET":
        return render(request, 'forgetpassword.html')
    else:
        tel = request.POST.get('tel')
        if UserInfo.objects.get(user_numbers=tel):
            request.session['tel'] = tel
            return redirect(reverse('logins:change'))
        else:
            render(request, 'forgetpassword.html')


def change(request):
    if request.method == "GET":
        a = request.session.get('tel')

        b = get_code(6, False)
        request.session['code'] = b
        send_sms(a, b)

        return render(request, 'forget_1.html')
    else:
        c = request.session.get('code')
        tel = request.session.get('tel')
        yzm = request.POST.get('yzm')
        pwd = request.POST.get('pwd')
        if c == yzm:
            user = UserInfo.objects.get(user_numbers=tel)
            user.user_password = pwd
            user.save()
            return redirect(reverse('logins:login'))
        else:
            return redirect(reverse('logins:forget'))
