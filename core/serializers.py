from rest_framework import serializers
from rest_framework import serializers
from .models import User
from core.models import (
    User,
)

# class MeSerializer(serializers.ModelSerializer):

#      class Meta:
#         model = User
#         fields = [
#             'id',
#             'first_name',
#             'last_name',
#             'emial'
#         ]    



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

