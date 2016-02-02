from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks import send_activation_mail


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_superuser=False):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_active=is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email=email,
            username=username,
            password=password,
            is_superuser=True
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = CustomUserManager()


class SecretKey(models.Model):
    user = models.ForeignKey(User)
    secretkey = models.UUIDField(primary_key=True, editable=False,
                                 default=uuid4)


@receiver(post_save, sender=User)
def send_mail(sender, instance, **kwargs):
    if not instance.is_active:
        sk = SecretKey.objects.filter(user=instance)
        if sk.exists():
            key = sk[0].secretkey
        else:
            sk = SecretKey.objects.create(
                user=instance
            )
            sk.save()
            key = sk.secretkey
        send_activation_mail.apply_async((instance.id, str(key)))
