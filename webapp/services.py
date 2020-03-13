from django.shortcuts import render;
from .models import author, airlines, cookbook, customuser;
from .serializers import AirlineSerializer, AuthUserSerializer;
from rest_framework.parsers import JSONParser;
from django.core.exceptions import ObjectDoesNotExist;
from django.views.decorators.csrf import csrf_exempt;
from rest_framework.decorators import api_view;
from django.core.paginator import Paginator;
import datetime;
from django.utils import timezone;
# Create your views here.
# method to create or update data.
class AirlineService:
    def createorupdateairline(reqBody):
        try:
            idCheck = False;
            if reqBody and reqBody.get('id') not in ['', None]:
                idCheck = True;
                tmpAirline = airlines.objects.get(id=reqBody.get('id'));
                if tmpAirline:
                    tmpAirline.name = reqBody.get('name');
                    tmpAirline.type = reqBody.get('type');
                    newAirline = tmpAirline;
                else:
                    # return JsonResponse({
                    #     'message': 'Something went wrong'
                    # }, status=500);
                    return {
                        'message': 'Something went wrong',
                        'status': 500
                    };
            else:
                newAirline = AirlineSerializer(data=reqBody);
                if newAirline.is_valid() is False:
                    # return JsonResponse({
                    #     'message': 'Validation got failed'
                    # });
                    return {
                        'message': 'Validation got failed',
                        'status': 400
                    };
            newAirline.save();
            data = newAirline.data if (idCheck is False) else AirlineSerializer(newAirline).data;
            # return JsonResponse({'message': 'done', 'data': data}, status=200);
            return {'message': 'done', 'data': data,'status': 200};
        except:
            # return JsonResponse({'message': 'something went wrong'}, status=500);
            return {'message': 'something went wrong', 'status': 500};

    # method to get the all airlines data.
    def getairlines(reqQuery):
        airlinesData = airlines.objects.order_by('id').all();
        paginator = Paginator(airlinesData, 5);
        page = reqQuery.get('page');
        if page in [None, '']:
            page = 1;
        finalData = AirlineSerializer(paginator.get_page(page), many=True);
        # return JsonResponse({
        #     'message': 'Records got successfully',
        #     'data': finalData.data,
        #     'total': paginator.count
        # }, status=200);
        return {
            'message': 'Records got successfully',
            'data': finalData.data,
            'total': paginator.count,
            'status': 200
        };

    # method to get the all airline data.
    # description: parameter is id to get the data;
    def getsingleairline(id):
        if id not in [None, '']:
            try:
                singleAirline = airlines.objects.get(id=id);
                # return JsonResponse({
                #     'message': 'Record got successfully',
                #     'data': AirlineSerializer(singleAirline).data
                # }, status=200);
                return {
                    'message': 'Record got successfully',
                    'data': AirlineSerializer(singleAirline).data,
                    'status': 200
                };
            except ObjectDoesNotExist:
                # return JsonResponse({
                #     'message': 'Record not found'
                # }, status=200);
                return {
                    'message': 'Record not found',
                    'status': 200
                };
        else:
            # return JsonResponse({
            #     'message': 'Id is requred'
            # }, status=400)
            return {
                'message': 'Id is required',
                'status': 400
            }

    def deleteairline(id):
        if id not in [None, '']:
            try:
                airObj = airlines.objects.get(id=id);
                if airObj:
                    airObj.delete();
                else:
                    # return JsonResponse({'message': 'Record not found'});
                    return {'message': 'Record not found', 'status': 404};
            except ObjectDoesNotExist:
                # return JsonResponse({'message': 'Object does not exist'});
                return {'message': 'Object does not exist', 'status': 404};
        else:
            # return JsonResponse({'message': 'id is required'});
             return {'message': 'id is required', 'status': 400};

class UserService:
    # method to create or update user.
    def createorupdateuser(reqBody):
        try:
            idCheck = False;
            newUser = {};
            reqBody['is_staff'] = reqBody.get('is_staff');
            reqBody['is_superuser'] = reqBody.get('is_superuser');
            reqBody['last_login'] = timezone.now();
            reqBody['date_joined'] = timezone.now();
            reqBody['delete_date'] = timezone.now();
            print('111111111111111111111111111111')
            if reqBody and reqBody.get('id') not in ['', None]:
                idCheck = True;
                tmpUser = customuser.objects.get(id=reqBody.get('id'));
                if tmpUser:
                    print('done=====================')
                    tmpUser.first_name = reqBody.get('first_name');
                    tmpUser.last_name = reqBody.get('last_name');
                    tmpUser.password = reqBody.get('password');
                    tmpUser.last_login = reqBody.get('last_login');
                    tmpUser.is_superuser = reqBody.get('is_superuser');
                    tmpUser.username = reqBody.get('username');
                    tmpUser.is_staff = reqBody.get('is_staff');
                    tmpUser.date_joined = reqBody.get('date_joined');
                    tmpUser.email = reqBody.get('email');
                    tmpUser.delete_date = reqBody.get('delete_date');
                    print('666666666666666666666666')
                    newUser = tmpUser;
                else:
                    # return JsonResponse({
                    #     'message': 'Something went wrong in else'
                    # }, status=500);
                     return {
                         'message': 'User does not exist',
                         'status': 400
                     }
            else:
                print('99999999999999999999')
                data = {};
                data['id'] = '';
                data['first_name'] = reqBody.get('first_name');
                data['last_name'] = reqBody.get('last_name');
                data['password'] = reqBody.get('password');
                data['last_login'] = reqBody.get('last_login');
                data['is_superuser'] = reqBody.get('is_superuser');
                data['username'] = reqBody.get('username');
                data['is_staff'] = reqBody.get('is_staff');
                data['date_joined'] = reqBody.get('date_joined');
                data['email'] = reqBody.get('email');
                data['delete_date'] = reqBody.get('delete_date');
                newUser = AuthUserSerializer(data=data);
                print('777777777', newUser.default_error_messages)
                if newUser.is_valid() is False:
                    # return JsonResponse({
                    #     'message': 'Validation got failed'
                    # });
                     return {
                         'message': 'Validation got failed',
                         'status': 400
                     }
            print('coming here')
            newUser.save();
            # print('coming here 2222222222222', newUser, idCheck)
            # data = newUser.data if (idCheck is False) else AuthUserSerializer(newUser).data;
            data = AuthUserSerializer(newUser);
            print('coming here failing',newUser ,'2222222222222222', data)
            # return JsonResponse({'message': 'done', 'data': {}}, status=200);
            return {
                 'message': 'done',
                 'status': 200,
                 'data': {}
            };
        except:
            # return JsonResponse({'message': 'something went wrong in exception'}, status=500);
             return {'message': 'something went wrong in exception', 'status': 500};