from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name="Dashboard"),
   path('GraphData/<int:id>/',views.GraphData,name="Graphdata"), # Url for graph

   # Url paths for student model:
   path('student',views.student,name="Stud_Dashboard"),
   path('<int:id>/details/',views.student_details,name="Stud_details"),
   path('<int:id>/delete/',views.student_delete,name="Stud_delete"),
   path('<int:id>/edit_student/',views.student_edit,name="Stud_edit"),
   path('Add_student',views.Add_student,name="Add_student"),
   path('student_search',views.student_search,name="student_search"),

   # Url paths for trainer model:
   path('trainer',views.trainer,name="trainer_Dashboard"),
   path('Add_trainer',views.Add_trainer,name="Add_trainer"),
   path('<int:id>/Trdetails/',views.trainer_details,name="Tr_details"),
   path('<int:id>/Trdelete/',views.trainer_delete,name="Tr_delete"),
   path('<int:id>/edit_trainer/',views.trainer_edit,name="Tr_edit"),
   path('trainer_search',views.trainer_search,name="trainer_search"),

   #Url paths for Referrer Model:
   path('referrer',views.referrer,name="referrer_Dashboard"),
   path('<int:id>/Rfdetails/',views.referrer_details,name="Rf_details"),
   path('Add_referrer',views.Add_referrer,name="Add_referrer"),
   path('<int:id>/Rfdelete/',views.referrer_delete,name="Rf_delete"),
   path('<int:id>/edit_referrer/',views.referrer_edit,name="Rf_edit"),
   path('referrer_search',views.referrer_search,name="referrer_search"),

]