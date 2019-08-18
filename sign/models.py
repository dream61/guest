from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit = models.IntegerField() #参加人数
    status = models.BooleanField() #状态
    address = models.CharField(max_length=300) #地址
    start_time = models.DateTimeField('events time') #发布会开始时间
    create_time = models.DateTimeField(auto_now=True) #创建时间（自动获取当前时间）
    def __str__(self):
        return self.name
#嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event) #关联发布会id
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField() #签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）
class Meta:
    unique_together = {"event","phone"}
def __str__(self):
    return self.realname