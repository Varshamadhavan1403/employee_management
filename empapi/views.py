from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from . serializers import ListEmployeeSerializers, CreateEmployeeSerializers, EmployeeFilterSerializer, EmployeeFilterSerializers
from emplapp.models import Employee, Department, Role
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.


# class ListEmployeeView(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = ListEmployeeSerializers


class ListEmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = ListEmployeeSerializers


class CreateEmployeeView(CreateAPIView):
    serializer_class = CreateEmployeeSerializers
    def post(self, request, format=None):
        serializer = CreateEmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class DeleteEmployeeView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     lookup_field='pk'
#     def delete(self, request, *args, **kwargs):
#         employee= self.get_object()
#         employee.delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteEmployeeView(APIView):
    # def delete(self, request, emp_id=0, format=None):
    #     if emp_id:
    #         try:
    #             emp_to_be_removed = Employee.objects.get(id=emp_id)
    #             emp_to_be_removed.delete()
    #             return Response("Employee Removed Successfully", status=status.HTTP_204_NO_CONTENT)
    #         except Employee.DoesNotExist:
    #             return Response("Please Enter A Valid EMP ID", status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response("Please Provide an EMP ID", status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        id = request.data.get('id')  

        if not id:
            return Response({'message': "No users selected"}, status=status.HTTP_400_BAD_REQUEST)
        for emp_id in id:
            try:
                employee = Employee.objects.get(id=emp_id)
                employee.delete()
                response = {
                    'success': True,
                    'message': 'The Employee is deleted.',
                    'status_code': status.HTTP_200_OK
                }
            except Employee.DoesNotExist:
                 response = {
                    'success': True,
                    'message': 'The Employee does not exist.',
                    'status_code': status.HTTP_404_NOT_FOUND
                }

        return Response(response)


class EmployeeFilterAPIView(APIView):
    def post(self, request, format=None):
        serializer = EmployeeFilterSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            dept = serializer.validated_data.get('dept')
            role = serializer.validated_data.get('role')

            employees = Employee.objects.all()

            if name:
                employees = employees.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
            
            if dept:
                employees = employees.filter(dept__name__icontains=dept)

            if role:
                employees = employees.filter(role__name__icontains=role)
            
            #return Response(EmployeeFilterSerializer(employees, many=True).data)
            return Response(EmployeeFilterSerializers(employees, many=True).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        return Response("Please use POST request for filtering.", status=status.HTTP_405_METHOD_NOT_ALLOWED)