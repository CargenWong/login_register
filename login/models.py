from django.db import models


# class Gender(models.Model):
#     name = models.CharField(max_length=32)
#
#
# class userInfo(models.Model):
#     nid = models.AutoField(primary_key=True, verbose_name='ID')
#     name = models.CharField(max_length=30, verbose_name='用户名')
#     # password = models.CharField(max_length=30, verbose_name='密码')
#     email = models.EmailField(db_index=True, verbose_name='邮箱')
#     memo = models.TextField( verbose_name='备注')
#     img = models.ImageField(upload_to='upload', verbose_name='图像')
#     user_type = models.ForeignKey("UserType", null=True, blank=True, on_delete=models.CASCADE, verbose_name='用户类型' )
#     gender_choices = (
#         (0, "男"),
#         (1, "女"),
#     )
#     gender = models.IntegerField(choices=gender_choices, default=0, verbose_name='性别')
#
#
# class UserType(models.Model):
#     name = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.name

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
