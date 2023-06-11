from django.core.validators import RegexValidator
from django.contrib.auth import password_validation

from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from apps.utils.objects_init import get_object_user

obj = get_object_user()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = obj.user_init()
        fields = [
            "username",
            'first_name',
            'last_name',
            'email',
        ]


class UserSignupSerializer(serializers.Serializer):

    email = serializers.EmailField(validators=[UniqueValidator(obj.get_users())])
    username = serializers.CharField(min_length=4, max_length=16, validators=[UniqueValidator(obj.get_users())])
    phone_regex = RegexValidator(regex=r'\+?1?\d{10}$', message='Phone number must be entered in the format: +5555555555')
    password = serializers.CharField(min_length=8, max_length=20)
    password_confirmation = serializers.CharField(min_length=8, max_length=20)
    first_name = serializers.CharField(min_length=2, max_length=34)
    last_name = serializers.CharField(min_length=2, max_length=34)

    def validate(self, data):

        password = data['password']
        pasw_conf = data['password_confirmation']
        if password != pasw_conf:
            raise serializers.ValidationError("Password don't match")
        password_validation.validate_password(password)
        return data
    
    def create(self, data):

        data.pop('password_confirmation')
        user = obj.user_init().objects.create_user(**data, is_verified=False, is_client=True)
        return user