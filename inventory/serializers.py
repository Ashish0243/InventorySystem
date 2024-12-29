from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=["item","description","image","quantity_available","quantity_claimable"]

        