from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserType, Profile


class AccountSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=225)
    password = serializers.CharField(max_length=225)
    email = serializers.EmailField(max_length=225)
    is_superuser = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=225)
    last_name = serializers.CharField(max_length=225)
    # dokita = serializers.CharField(max_length=100)
    # user_type = serializers.IntegerField()
    # profile = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
        )
        user.set_password(validated_data['password'])
        # user_type = UserType.objects.get(pk=validated_data['user_type'])
        # profile = Profile.objects.create(
        #     user=user,
        #     user_type=user_type,
        #     dokita=validated_data["dokita"]
        # )
        return user
#
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        try:
            if validated_data['password']:
                instance.set_password(validated_data['password'])
        except:
            pass
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Profile
