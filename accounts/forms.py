from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "name")  # Explicitly list fields
        field_classes = None  # Ensure no unexpected field classes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove any unexpected fields
        if "usable_password" in self.fields:
            del self.fields["usable_password"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "last_login",
            "date_joined",
        )
        field_classes = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove any unexpected fields
        if "usable_password" in self.fields:
            del self.fields["usable_password"]
