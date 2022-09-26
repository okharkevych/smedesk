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
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, ProjectModel):
    # This is here only not to crash Django.
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
