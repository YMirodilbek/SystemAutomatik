from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SuperUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]