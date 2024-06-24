from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 

from .fields import OrderField


# Create your models here.

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ['title']
    def __str__(self) -> str:
        return self.title

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User ,
                              related_name='courses_created',
                              on_delete=models.CASCADE,
                              null=True)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE,
                                null=True)


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    def __str__(self) -> str:
        return self.title

class Module(models.Model):
    id = models.AutoField(primary_key=True)

    course = models.ForeignKey(Course , 
                               related_name='modules',
                               on_delete=models.CASCADE,
                               null=True)
    order = OrderField(blank=True , for_fields=['course'])
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.order}.{self.title}'
    class Meta:
        ordering = ['order']


class Content(models.Model):
    """
    We define an OrderedContent model that is a proxy model for the Content model. This model
    provides a default ordering for QuerySets and an additional created_delta() method. Both models,
    Content and OrderedContent, operate on the same database table, and objects are accessible via the
    ORM through either model.
    """
    id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Module ,
                              related_name='contents',
                              on_delete=models.CASCADE,
                              null=True)
    order = OrderField(blank=True , for_fields=['module'])
    content_type = models.ForeignKey(ContentType,
                                on_delete=models.CASCADE,
                                null=True,
                                limit_choices_to={'model_in':(
                                    'text',
                                    'video',
                                    'image',
                                    'file',
                                )})


    object_id = models.PositiveIntegerField()
 

    item = GenericForeignKey('content_type','object_id')
    class Meta:
        ordering = ['order']

class ItemBase(models.Model):

    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def __str__(self) -> str:
        return self.title

class Text(ItemBase):
    body = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()

