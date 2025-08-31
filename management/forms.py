from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'photo']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']
class StudentSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
