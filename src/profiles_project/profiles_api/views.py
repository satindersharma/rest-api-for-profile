from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloAPI(APIView):
    '''test api views'''
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