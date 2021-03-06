from django.db import models
from django.contrib.auth.models import User

from mdeditor.fields import MDTextField

from read_counter.models import ReadNumExpandMethod

# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=12)

    # 返回博文分类对应的博文数量
    def blog_count(self):
        # blog_set是反向获取被关联外键的model，模型名称小写加_set。
        return self.blog_set.count()

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = '文章类型'


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = MDTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        ordering = ['-created_time', '-last_updated_time']
        verbose_name_plural = '文章'
