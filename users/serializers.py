# users/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUserModel
class CustomUserRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=CustomUserModel.roles)

    def custom_signup(self, request, user):
        # Customize signup logic if needed
        user.role = self.validated_data['role']
        user.save()
