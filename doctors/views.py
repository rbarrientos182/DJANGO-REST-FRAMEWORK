from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   

@api_view(['GET','POST'])
def list_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def detail_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)