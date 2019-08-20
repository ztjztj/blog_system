'''
短信下发核心方法
1. send_sms 发短信
2. get_code 生成验证码
'''
# coding=utf-8
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

'''发送短信(手机,6位验证码)'''


def send_sms(phone, code):
    client = AcsClient('LTAIEx3Gbdbceg2C', 'MsCoWUm3x2iXaIcvtqhQLi9yj6nHxX', 'cn-hangzhou')

    # phone = '17600950805'
    # aa= '222222'
    code = "{'code':%s}" % (code)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', 'cn-hangzhou')
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', '北网实训组')
    request.add_query_param('TemplateCode', 'SMS_165745016')
    request.add_query_param('TemplateParam', code)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

    return str(response, encoding='utf-8')


'''生成随机验证码: 数字表示生成几位,   True表示生成带有字母的  False不带字母的'''


def get_code(n=6, alpha=True):
    s = ''  # 创建字符串变量,存储生成的验证码
    for i in range(n):  # 通过for循环控制验证码位数
        num = random.randint(0, 9)  # 生成随机数字0-9
        if alpha:  # 需要字母验证码,不用传参,如果不需要字母的,关键字alpha=False
            upper_alpha = chr(random.randint(65, 90))
            lower_alpha = chr(random.randint(97, 122))
            num = random.choice([num, upper_alpha, lower_alpha])
        s = s + str(num)
    return s


