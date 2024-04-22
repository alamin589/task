# forms.py
from django import forms
from .models import SocialMediaAccount, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SocialMediaForm(forms.ModelForm):
    platform = forms.ChoiceField(choices=SocialMediaAccount.PLATFORM_CHOICES)

    class Meta:
        model = SocialMediaAccount
        fields = ['platform', 'username']

SocialMediaFormSet = forms.inlineformset_factory(
    parent_model=UserProfile,  # Replace YourParentModel with the model you are associating the social media accounts with
    model=SocialMediaAccount,
    form=SocialMediaForm,
    extra=1,  
    can_delete=True,  # Allow deletion of forms
    can_order=False,  # Disable reordering of forms
    min_num=1,  # Minimum number of forms required
    validate_min=True,  # Ensure minimum number of forms are present
    max_num=10,  # Maximum number of forms allowed
    validate_max=True,  # Ensure maximum number of forms are not exceeded
)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user'] 