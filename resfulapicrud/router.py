from django.db import router
from employeeapi.viewset import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)