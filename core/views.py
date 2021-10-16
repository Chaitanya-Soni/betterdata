from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import modelData,realdata,syntheticdata,parameters,project
from .serializers import RealDataSerializer,SyntheticDataSerializer,ProjectSerializer,ModelDataSerializer,ParameterSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class Realdatalist(APIView):
    def get(self,request,idp):
        proj = project.objects.get(id=idp)
        real_data = realdata.objects.filter(proj=proj)
        serializer = RealDataSerializer(real_data,many=True)
        return Response(serializer.data)
    
    def post(self,request,idp):
        data = request.data
        d = {}
        proj = project.objects.get(id=idp)
        real_data = data['real_data']
        name = data['name']
        if(proj!=None and real_data!=None and name != None ):
            real = realdata.objects.create(proj=proj,name=name,real_data=real_data)
            real.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
class RealdataDetail(APIView):
    def get_object(self,id):
        try :
            articles = realdata.objects.get(id=id)
            return articles
        except :
            return "NOT FOUND"

    def get(self,request,id):
        articles=self.get_object(id)
        if(articles!="NOT FOUND"):
            serializer = RealDataSerializer(articles)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    def post(self,request,id):
        articles=self.get_object(id)
        serializer = RealDataSerializer(articles ,data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        articles=self.get_object(id)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    def update(self, request, pk):
        real_data = realdata.objects.get(pk=pk)
        serializer = RealDataSerializer(real_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Projectlist(APIView):
    def get(self,request):
        proj = project.objects.all()
        serializer = ProjectSerializer(proj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        obj = project.objects.create()
        obj.save()
        return Response(status=status.HTTP_201_CREATED)
class Projectdetail(APIView):
    def get_object(self,id):
        try :
            proj = project.objects.get(id=id)
            return proj
        except :
            return "NOT FOUND"
    def get(self,request,id):
        proj=self.get_object(id)
        if(proj!="NOT FOUND"):
            serializerProj = ProjectSerializer(instance=proj)
            modellist =  modelData.objects.filter(proj=proj)
            realdataslist =  realdata.objects.filter(proj=proj)
            d={}
            d['project']=serializerProj.data
            d['Models']=[]
            for modeltemp in modellist:
                serializer = ModelDataSerializer(instance=modeltemp)
                paramet=parameters.objects.get(name=modeltemp)
                s2 = ParameterSerializer(paramet)
                dtemp=serializer.data
                dtemp['parameter']=s2.data
                synthetic = syntheticdata.objects.filter(name=modeltemp)
                s3 = SyntheticDataSerializer(synthetic,many=True)
                dtemp['synthetic-data']=s3.data
                d['Models'].append(dtemp)
            d['real-datasets']=[]
            for realtemp in realdataslist:
                real_data = realdata.objects.all()
                serializer = RealDataSerializer(real_data,many=True)
                d['real-datasets'].append(serializer.data)
            return Response(d)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    def update(self, request, id):
        proj = project.objects.get(id=id)
        serializer = ProjectSerializer(proj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, id):
        proj = project.objects.get(id=id)
        serializer = ProjectSerializer(proj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        modeldata=self.get_object(id)
        modeldata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
class modellist(APIView):
    def get(self,request,idp):
        proj=project.objects.get(id=idp)
        modellist = modelData.objects.filter(proj=proj)
        serializer = ModelDataSerializer(modellist,many=True)
        return Response(serializer.data)
    
    def post(self,request,idp):
        proj=project.objects.get(id=idp)
        data= request.data
        name =  data['name']
        batchsize = data['parameter']['batch_size']
        trainingcycles = data['parameter']['training_cycles']
        if(name!= None and batchsize!=None and trainingcycles!=None):
            modeld = modelData.objects.create(proj=proj,name=name)
            modeld.save()
            para = parameters.objects.create(name=modeld,batch_size=batchsize,training_cycles=trainingcycles)
            para.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
class ModelDetail(APIView):
    def get_object(self,id):
        try :
            modledata = modelData.objects.get(id=id)
            return modledata
        except :
            return "NOT FOUND"
    def get(self,request,id):
        modeldata=self.get_object(id)
        if(modeldata!="NOT FOUND"):
            serializer = ModelDataSerializer(instance=modeldata)
            paramet=parameters.objects.get(name=modeldata)
            s2 = ParameterSerializer(paramet)
            d=serializer.data
            d['parameter']=s2.data
            synthetic = syntheticdata.objects.filter(name=modeldata)
            s3 = SyntheticDataSerializer(synthetic,many=True)
            d['synthetic-data']=s3.data
            print(s3.data)
            print(d)
            return Response(d)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    def delete(self,request,id):
        modeldata=self.get_object(id)
        modeldata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    def update(self, request, id):
        modeldata = modelData.objects.get(id=id)
        serializer = ModelDataSerializer(modeldata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, id):
        modeldata = modelData.objects.get(id=id)
        serializer = ModelDataSerializer(modeldata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SyntheticDatalist(APIView):
    def get(self,request,id1):
        modeld = modelData.objects.get(id=id1)
        synthetic = syntheticdata.objects.filter(name=modeld)
        serializer = SyntheticDataSerializer(synthetic,many=True)
        return Response(serializer.data)
    
    def post(self,request,id1):
        data= request.data
        modeld = modelData.objects.get(id=id1)
        synthetic_data = data['synthetic_data']
        if(synthetic_data!=None):
            synth = syntheticdata.objects.create(name=modeld,synthetic_data=synthetic_data)
            synth.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
class SyntheticDataDetail(APIView):
    def get_object(self,id1,id2):
        try :
            modledata = modelData.objects.get(id=id1)
            synthetic = syntheticdata.objects.get(name=modledata,id=id2)
            print(synthetic)
            return synthetic
        except :
            return "NOT FOUND"

    def get(self,request,id1,id2):
        synthetic=self.get_object(id1,id2)
        if(synthetic!="NOT FOUND"):
            serializer = SyntheticDataSerializer(synthetic)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    def delete(self,request,id1,id2):
        synthetic=self.get_object(id1,id2)
        synthetic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 