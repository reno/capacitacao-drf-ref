from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import CustomUser


class UserListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users:detail')

    class Meta:
        model = CustomUser
        fields = ['url', 'username']


class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users:detail')

    class Meta:
        model = CustomUser
        fields = [
            'url', 'username', 'first_name', 'last_name', 'email',
            'bio', 'website_url',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name', 'username',
            'password', 'password2', 'bio', 'website_url',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'detail': "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # enviar email de confirmação
        return user
