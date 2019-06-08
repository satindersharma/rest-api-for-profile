from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''serilisers a name field for testing our APIViews'''
    '''we describe the fields as class varialbel just like djangomodels'''

    name = serializers.CharField(max_length=10)
