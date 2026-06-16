from django.urls import path

from . import views

urlpatterns = [
    path("employees/", views.employee_list),
    path("employees/<int:employee_id>/", views.employee_detail),
    path("salary/calculate/", views.calculate_salary),
    path("salary/slips/", views.salary_slips),
]
