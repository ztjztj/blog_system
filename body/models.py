from django.db import models
from django.core import validators


# Create your models here.


class UserInfo(models.Model):
    """用户表"""
    user_numbers = models.BigIntegerField(null=True,verbose_name='账号')
    user_password = models.CharField(max_length=20, null=True,verbose_name='密码')
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_sex = models.CharField(default='请修改', max_length=20,verbose_name='性别')
    user_sign = models.TextField(default='空空如也',verbose_name='个性签名')
    user_birth = models.DateField(auto_now_add=True,verbose_name='出生日期')
    user_city = models.CharField(default='请修改',max_length=20,verbose_name='所在地')
    user_one_level = models.IntegerField(default=1,verbose_name='用户等级')
    user_member_level = models.IntegerField(default=1,verbose_name='会员等级')
    user_PORT = models.IntegerField(default=0)
    user_jude = models.IntegerField(default=0)
    user_IP  = models.CharField(max_length=20,null=True,blank=True)
    userimg = models.TextField(default='data:image/jpg;base64,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',verbose_name='用户头像编码')

class levelsystem(models.Model):
    userid = models.ForeignKey(to='UserInfo', db_column='user_id', on_delete=models.CASCADE,verbose_name='用户id')
    signnumber = models.IntegerField(db_column='sign_num',verbose_name='登陆天数')
    memberopendata = models.DateField(null=True, db_column='member_open_data',verbose_name='会员充值日期')
    duedata = models.DateField(null=True, db_column='member_due_data',verbose_name='会员到期时间')
    sign = models.DateField(auto_now=True,null=True,verbose_name='最后签到日期')
    userimg = models.TextField(verbose_name='用户头像编码')

    class Meta:
        db_table = 'level_system'


# class PhotoAlbum(models.Model):
#     """用户相册字段"""
#     user_image = models.ImageField(upload_to='image',verbose_name='图片地址')
#     image_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
#     image_type = models.CharField(max_length=10,verbose_name='类型')
#     user_fk = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class DynamicStatus(models.Model):
    """用户动态表"""
    # 发表动态的时间
    d_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
    # 发表的动态内容
    d_content = models.TextField(verbose_name='内容')
    # 发表的图片
    d_picture = models.FileField(upload_to='picture', null=True,
                                 validators=[validators.FileExtensionValidator('jpg', 'png', 'txt')], max_length=1000,verbose_name='图片')
    # 点赞的数量
    d_num = models.IntegerField(default=0,verbose_name='点赞数')
    # 喜欢的数量
    # 转发数量
    d_move = models.IntegerField(default=0)
    d_like = models.IntegerField(default=0,verbose_name='喜欢数')
    # 转发之后附加内容
    new_content = models.TextField(null=True,verbose_name='转发')
    # 谁发表的动态
    user_id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class Move_text(models.Model):
    # 转发的时间
    d_b_time = models.DateTimeField(auto_now_add=True, null=True)
    # 被转发的用户的ID（也就是这篇文章是谁写的）
    d_user = models.IntegerField(null=True)
    # 转发的用户的ID（也就是谁转发的）
    d_z_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


# 点赞表
class Thumps_up(models.Model):
    # 谁点的赞
    u = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    # 赞的那个动态
    article = models.ForeignKey(DynamicStatus, on_delete=models.PROTECT)


# 喜欢表
class love(models.Model):
    # 谁喜欢这条动态
    u = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    # 喜欢那条动态
    U_Article = models.ForeignKey(DynamicStatus, on_delete=models.CASCADE)


class AttentionPerson(models.Model):
    """关注的人"""
    # 我====》关注
    a_user = models.IntegerField()

    # 被关注的人
    a_b_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class Comment(models.Model):
    """评论表"""
    # 评论的内容
    c_content = models.TextField(verbose_name='内容', null=True)
    # 被评论的文章
    c_b_dynamic = models.ForeignKey('DynamicStatus', on_delete=models.CASCADE, null=True)
    # 被评论的评论的ID
    c_b_commentID = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name='parent_comment')
    root = models.ForeignKey('Comment', related_name='root_comment', null=True, on_delete=models.DO_NOTHING)
    # 评论的时间
    comment_time = models.DateTimeField(auto_now_add=True, null=True)
    # 二级评论回复的人
    reply_to = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, null=True, related_name='replies')
    # 评论的用户
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name='comments', null=True)



# 访客表
class GuestLog(models.Model):
    g_b_user=models.IntegerField()
    # 被访问的用户
    g_user=models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    # 访问的用户
    g_date=models.DateTimeField(auto_now=True)

    g_num = models.IntegerField(default=0)
