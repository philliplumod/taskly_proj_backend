from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    url = serializers.HyperlinkedIdentityField(
        view_name='users-detail',
        lookup_field='user_id'
    )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'user_id', 'username', 'email', 'first_name', 'last_name', 'password']
