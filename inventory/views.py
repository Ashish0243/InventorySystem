from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes,permission_classes
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated,])
def CreateInventoryView(request,*args,**kwargs):
    serializer=InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ListInventoryView(request,*args,**kwargs):
    queryset=Inventory.objects.all()
    serializer=InventorySerializer(queryset,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteItemView(request,pk):
  item=Inventory.objects.get(id=pk)
  if item:
      item.delete()
      return Response({"message":"Item deleted"},status=status.HTTP_204_NO_CONTENT)
  else:
      return Response({"message":"No data found"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def DetailItemView(request,pk):
    item=Inventory.objects.get(id=pk)
    serializer=InventorySerializer(item)
    if serializer:
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({"message":"item not found"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def UpdateItemView(request,pk):
    item=Inventory.objects.get(id=pk)
    if item:
        serializer=InventorySerializer(item,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message":"item not found"},status=status.HTTP_404_NOT_FOUND)
    
    
