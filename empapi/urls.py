from django.urls import path, include
from .  views import ListEmployeeView, CreateEmployeeView, DeleteEmployeeView, EmployeeFilterAPIView
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'employees',ListEmployeeView)
urlpatterns = [
        path('list_emp/', ListEmployeeView.as_view(), name='list_emp'),
        # path('', include(router.urls)),
        path('create_emp/', CreateEmployeeView.as_view(), name='create_emp'),
        path('delete_emp/', DeleteEmployeeView.as_view(), name='delete_emp'),
        path('emp_filter/', EmployeeFilterAPIView.as_view(), name='filter_emp'),



]
