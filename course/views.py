from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSer
# Create your views here.


class StudentViewset(ViewSet):

    def create(self,request,*args,**kwargs):
        ser=StudentSer(data=request.data)
        if ser.is_valid():
            ser.save()
            print(ser)
            return Response({"msg":"created"})
        return Response({"msg":"failed"})
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        ob=Student.objects.get(id=id)
        dser=StudentSer(ob)
        return Response(dser.data)
    
    def list(self,request,*args,**kwargs):
        ob=Student.objects.all()
        dser=StudentSer(ob,many=True)
        return Response(dser.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ob=Student.objects.get(id=id)
        ob.delete()
        return Response({"msg":"deleted"})