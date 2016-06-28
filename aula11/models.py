# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class AuditModel(models.Model):

    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Category(AuditModel):                                                   
                                                                                
    name = models.CharField(                                                    
        u'Nome',                                                                
        max_length=100                                                          
    )                                                                           
                                                                                                                                                         
    published = models.BooleanField(                                            
        u'Publicado',                                                           
        default=True                                                            
    )                                                                                
                                                                                
    def __unicode__(self):                                                      
        return self.name                                                        
                                                                                
    class Meta:                                                                 
        verbose_name = u'Categoria'                                             
        verbose_name_plural = u'Categorias'                                     
        ordering = ['name']

class PublishedManager(models.Manager):
    
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(published=True)
		
class Post(AuditModel):                                                       
                                                                                
    user = models.ForeignKey(                                                   
        User,                                                                   
        verbose_name=u'Postado por',                                                                                             
    )                                                                           
                                                                                
    title = models.CharField(                                                   
        u'Título',                                                              
        max_length=100                                                          
    )                                                                           
                                                                      
    body = models.TextField(                                                    
        u'Texto',                                                               
    )                                                                           
                                                                                
    category = models.ForeignKey(                                        
        Category,                                                               
        verbose_name=u'categoria',                                             
        related_name='posts'                                                    
    )                                                                           
                                                                                
    published = models.BooleanField(                                            
        u'Publicado',                                                           
        default=True                                                            
    )       
                                                                                
    def __unicode__(self):                                                      
        return self.title                                                       
                                                                                
    class Meta:                                                                 
        verbose_name = u'Post'                                                  
        verbose_name_plural = u'Posts'                                          
        ordering = ['-created_on']

    # manager = models.Manager()
    objects = models.Manager()
    published_objects = PublishedManager()


class UserInfo(User):

    age = models.IntegerField(
        u'Idade',
        default=0,
    )

    def __unicode__(self):                                                      
        return self.user.username

    class Meta:                                                                 
        verbose_name = u'User info'                                                  
        verbose_name_plural = u'User infos'     


class MyUserManager(models.Manager):

    def get_query_set(self):
        return super(MyUserManager, self).get_query_set().filter(is_active=True)

class MyUser(User):
    
    objects = MyUserManager()

    class Meta:
        proxy = True
        ordering = ['-username']

    def do_something(self):
        return True          
