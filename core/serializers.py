from rest_framework import serializers
from .models import realdata,syntheticdata,project,parameters,modelData
class RealDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = realdata
        fields = ["id","proj","real_data","name"]
class SyntheticDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = syntheticdata
        fields = ["id","synthetic_data"]
class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = project
        fields = ["id","proj"]
class ParameterSerializer(serializers.ModelSerializer):
    class Meta :
        model = parameters
        fields = ["id","batch_size","training_cycles"]
class ModelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelData
        fields = ['id','proj' ,'name']