import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampedModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class UserManager(BaseUserManager):
    def create_user(self, name, email, password, terms):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            terms=terms
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, ProjectModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    terms = models.BooleanField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class Session(ProjectModel):
    user = ''
