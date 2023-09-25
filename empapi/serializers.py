from rest_framework import serializers
from emplapp.models import Employee, Role, Department

class ListEmployeeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'


class CreateEmployeeSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    dept = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    salary = serializers.IntegerField(default=0)
    bonus = serializers.IntegerField(default=0)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    phone = serializers.IntegerField(default=0)
    hire_date = serializers.DateField()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'salary', 'dept', 'role', 'bonus', 'phone', 'hire_date')

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    

class EmployeeFilterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    dept = serializers.CharField(max_length=100, required=False)
    role = serializers.CharField(max_length=100, required=False)



class EmployeeFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ('first_name', 'last_name', 'salary', 'dept', 'role', 'bonus', 'phone', 'hire_date')
