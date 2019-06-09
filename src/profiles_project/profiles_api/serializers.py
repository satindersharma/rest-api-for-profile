from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    '''serilisers a name field for testing our APIViews'''
    '''we describe the fields as class varialbel just like djangomodels'''

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    ''' a serializer for our user profile objects.'''

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        '''create an return a new user'''
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
