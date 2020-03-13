from .models import airlines, author, cookbook, customuser;
from rest_framework import serializers;
from django.core.exceptions import ObjectDoesNotExist;
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = airlines;
        fields = ('id', 'name', 'type');
        depth = 1;


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customuser;
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff',
                  'is_active', 'date_joined', 'email', 'delete_date');
        depth =1;