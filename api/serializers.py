from rest_framework import serializers
from api.models import Task
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        # def update(self,*args,**kwargs):


# class Taskserializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'