from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models as m

class Usuario(m.Model):
    username = User.username
    