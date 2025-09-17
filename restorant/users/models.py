from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        if not username:
            raise ValueError("El nombre de usuario es obligatorio")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # In this case, we'll use the email for the username as well
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # In this case, we'll use the email for the username as well
        return self._create_user(email, email, password, **extra_fields)

class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    You can add additional fields here if needed.
    """
    # Example of adding a custom field
    # bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
