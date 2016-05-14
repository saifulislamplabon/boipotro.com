# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

# from django.utils.text import slugify

#A function for creating simple unicode slug
def sslugify(line):
    ret="";
    temp= line.strip()
    for i in range(0,len(temp)):
        if temp[i]==' ':
            ret=ret+'-'
        else:
            ret=ret+temp[i]

    return ret




def upload_location(instance, filename):

    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.slug, instance.slug,extension)

    # BookModel = instance.__class__
    # new_id = BookModel.objects.order_by("id").last().id + 1
    # new_id=""
    # """
    # instance.__class__ gets the model Post. We must use this method because the model is defined below.
    # Then create a queryset ordered by the "id"s of each object,
    # Then we get the last object in the queryset with `.last()`
    # Which will give us the most recently created Model instance
    # We add 1 to it, so we get what should be the same id as the the post we are creating.
    # """
    # return "%s/%s" %(new_id, filename)

class Author(models.Model):
    author_name=models.CharField(max_length=255)

    #EXTRA
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=upload_location,null=True) ##NEED TO CHANGE

    def __unicode__(self):
        return self.author_name

    def __str__(self):
        return self.author_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author', blank=True)
    slug = models.CharField(unique=True, max_length=255)
    category = models.CharField(max_length=120,null=True,blank=True) ##Type In catalog
    subject = models.CharField(max_length=120, null=True,blank=True)
    #Files
    cover = models.ImageField(upload_to=upload_location,null=True,blank=True)
    book_file = models.FileField(upload_to=upload_location,null=True,blank=True)
    book_type = models.CharField( max_length=120, default="ebook",blank=True)

    #Times
    published = models.DateField(auto_now=False, auto_now_add=False, null=True,blank=True) #will be CHANGE
    added = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,blank=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,blank=True)
    #Price
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True,blank=True)
    free = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



def create_slug(instance, new_slug=None):
    slug = sslugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Book.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_book_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_book_receiver, sender=Book)
