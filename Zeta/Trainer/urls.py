from django.urls import path
from .import views

urlpatterns = [
  path('Tdashboard',views.index,name="Dashboard"), # Trainers Dashboard
  # Urls for trainers
  path('Trdetails',views.trainerdetails,name="Trainerdetails"),
  path('<int:id>/Trdata/',views.trainer_data,name="Tr_data"),
  path('Trsearch',views.trainer_search,name="trainer_search"),
  # Urls for Student
  path('studetails',views.studentdetails,name="Studentsdetails"),
  path('<int:id>/studata/',views.student_data,name="stud_data"),
  path('studsearch',views.student_search,name="student_search"),
]