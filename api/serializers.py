from dataclasses import fields
from rest_framework import serializers

from api.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
        'id',
        'name',
        'birth',
        'email',
        'cellphone',
        'street',
        'house_number',
        'address_complement',
        'district',
        'city',
        'state',
        'DDD',
        )