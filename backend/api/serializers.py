from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from .models import Movie, Channel

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    re_pass = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    class Meta:
        model = User
        fields = ('email', 'password', 're_pass', 'full_name', 'username')
        extra_kwargs = {
            'full_name': {'required': True}
        }

    def validate(self, attrs):
        # Kiểm tra xem mật khẩu có khớp không
        if attrs['password'] != attrs['re_pass']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Kiểm tra xem mật khẩu có ít nhất một ký tự viết hoa không
        if not any(char.isupper() for char in attrs['password']):
            raise serializers.ValidationError({"password": "Password must contain at least one uppercase letter."})

        # Kiểm tra xem mật khẩu có ít nhất một ký tự đặc biệt không
        if not any(not char.isalnum() for char in attrs['password']):
            raise serializers.ValidationError({"password": "Password must contain at least one special character."})

        # Kiểm tra định dạng email
        if not re.match(self.email_regex, attrs['email']):
            raise serializers.ValidationError({"email": "Invalid email format."})

        return attrs
    
    def create(self, validated_data):
        validated_data.pop('re_pass')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'username','image')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'



       