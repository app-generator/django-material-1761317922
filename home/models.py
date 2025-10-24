# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employees(models.Model):

    #__Employees_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    empid = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Employees_FIELDS__END

    class Meta:
        verbose_name        = _("Employees")
        verbose_name_plural = _("Employees")


class Departments(models.Model):

    #__Departments_FIELDS__
    empid = models.ForeignKey(employees, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    manager = models.CharField(max_length=255, null=True, blank=True)

    #__Departments_FIELDS__END

    class Meta:
        verbose_name        = _("Departments")
        verbose_name_plural = _("Departments")



#__MODELS__END
