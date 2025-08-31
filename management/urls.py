from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),  # <-- Home page

    path('students/', views.StudentListView.as_view(), name='students_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-course/', views.add_course, name='add_course'),
    path('search-student/', views.SearchStudentView.as_view(), name='search_student')

]
