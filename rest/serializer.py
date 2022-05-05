from unittest.util import _MAX_LENGTH
from rest_framework import fields, serializers
from rest.models import Info


class InfoSerializers(serializers.ModelSerializer):
    class Meta :
        model = Info
        fields = ['checked','name','Type','Age', 'Description', 'date']
 
    
    checked = serializers.BooleanField()
    name = serializers.CharField(max_length=20)
    Type = serializers.CharField(max_length=100)
    Age = serializers.IntegerField()
    Description = serializers.CharField(max_length=200)
    date =  serializers.DateField()
     

    def create(self, validated_data):
        return Info.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.checked = validated_data.get('checked', instance.Title)
        instance.name = validated_data.get('name', instance.name)
        instance.Type = validated_data.get('Type', instance.Type)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.date = validated_data.get('date',instance.date)
        instance.save()
        return instance