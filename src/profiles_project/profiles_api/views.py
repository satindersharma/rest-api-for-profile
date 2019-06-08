from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
'''here status contain the differnt status code list'''

# Create your views here.
class HelloAPI(APIView):
    '''test api views'''

    serializer_class = serializers.HelloSerializer
    '''this tels djanfo rest framework serializer_class for this HelloAPI APIView is HelloSerializer in serializers'''

    def get(self, request, format=None):
        '''this is usedwhenever you wanna list of object from a spesfic api'''
        '''return a list of APIView features'''

        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'GIves you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        '''Response is to be dictionary which is converted to json which the output to the screen'''
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    '''after discribing a calss serializer_class lest crate a post function
    
    '''
    def post(self, request):
        '''create a hello message with our name
        we  gona return a message that include he name that was posted to the api'''
        serializer = serializers.HelloSerializer(data=request.data)
        '''vaiddate the data'''
        if serializer.is_valid():
            '''this will get the name data'''
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        '''hanles updating an objects'''
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        '''patch request, only updates fields provies in the request'''
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        '''delete an objects'''
        return Response({'method':'delete'})
