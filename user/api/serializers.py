from rest_framework import serializers
from user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'profile_image')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if profile_image:
            user.profile_image.save(profile_image.name, profile_image, save=True) 
        return user
