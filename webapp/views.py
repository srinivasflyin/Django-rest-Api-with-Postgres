from django.shortcuts import render;
from .models import author, airlines, cookbook, customuser;
from django.http import HttpResponse, JsonResponse;
from .serializers import AirlineSerializer, AuthUserSerializer;
from rest_framework.parsers import JSONParser;
from django.core.exceptions import ObjectDoesNotExist;
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view;
from django.core.paginator import Paginator;
import datetime;
from django.utils import timezone;
from .services import AirlineService, UserService;
# Create your views here.
# method to create or update data.
@csrf_exempt
@api_view(['POST'])
def createorupdateairline(request):
    response = AirlineService.createorupdateairline(request.data);
    status = response['status'];
    del response['status'];
    return JsonResponse(response,status=status)

 # method to get the all airlines data.
@csrf_exempt
@api_view(['GET'])
def getairlines(request):
    response =  AirlineService.getairlines(request.GET);
    status = response['status'];
    del response['status'];
    return JsonResponse(response,status=status)

# method to get the all airline data.
# description: parameter is id to get the data;
@csrf_exempt
@api_view(['GET'])
def getsingleairline(request, id):
    response = AirlineService.getsingleairline(id);
    status = response['status'];
    del response['status'];
    return JsonResponse(response,status=status)

@csrf_exempt
@api_view(['GET'])
def deleteairline(request, id):
    response = AirlineService.deleteairline(id);
    status = response['status'];
    del response['status'];
    return JsonResponse(response,status=status)


# method to create or update user.
@csrf_exempt
@api_view(['POST'])
def createorupdateuser(request):
    response = UserService.createorupdateuser(request.data);
    status = response['status'];
    del response['status'];
    return JsonResponse(response,status=status)