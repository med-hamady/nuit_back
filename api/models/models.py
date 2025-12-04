from django.db import models
from django.utils import timezone
from datetime import timedelta
import binascii
import os
import uuid
import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password
import random


class APILog(models.Model):
    request_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_params = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    response_status = models.IntegerField()
    response_body = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.response_status} - {self.path} - {self.user_email} - {self.request_date.day}/{self.request_date.month}/{self.request_date.year} {self.request_date.hour}:{self.request_date.minute}:{self.request_date.second}"
    
    class Meta:
        db_table = "LOGS"
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "CATEGORIES"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['order']


class Option(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    impact_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    impact_ecology = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    impact_autonomy = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    impact_inclusion = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    class Meta:
        db_table = "OPTIONS"
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class QuizQuestion(models.Model):
    question_text = models.TextField()
    is_true = models.BooleanField(default=True)
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]

    class Meta:
        db_table = "QUIZ_QUESTIONS"
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'


class SimulationRun(models.Model):
    score_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    score_ecology = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    score_autonomy = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    score_inclusion = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    choices = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulation - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        db_table = "SIMULATION_RUNS"
        verbose_name = 'Simulation Run'
        verbose_name_plural = 'Simulation Runs'
        ordering = ['-created_at']


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "IDEAS"
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'
        ordering = ['-created_at']


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('video', 'Video'),
        ('article', 'Article'),
        ('site', 'Site'),
    ]

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "RESOURCES"
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
        ordering = ['-created_at']


class CustomAccountManager(BaseUserManager):

    def create_superuser(self,  password, **other_fields):
        random_phone = random.randint(10_000_000, 99_999_999)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('telephone', random_phone)
        other_fields.setdefault('email', f"{random_phone}@layers.com")
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(password, **other_fields)

    def create_user(self,  password, **other_fields):

        user = self.model( **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username= models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    telephone = models.IntegerField(unique=True)
    is_blocked= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_paused = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    
    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
        
    class Meta:
        db_table = "USERS"
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

