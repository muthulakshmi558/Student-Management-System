from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View,FormView
from .models import Student, Course
from .forms import StudentForm, CourseForm, StudentSearchForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


@method_decorator(staff_member_required, name='dispatch')
class AddCourseView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'add_course.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():



            
            form.save()
            return redirect('students_list')
        return render(request, 'add_course.html', {'form': form})
# CBVs

class HomeView(TemplateView):
    template_name = 'management/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Latest 5 students
        context['latest_students'] = Student.objects.all().order_by('-id')[:5]
        # Latest 5 courses
        context['latest_courses'] = Course.objects.all().order_by('-id')[:5]
        return context

class StudentListView(ListView):
    model = Student
    template_name = 'management/students_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'management/student_detail.html'
    context_object_name = 'student'

# Add student/course
def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('students_list')
    return render(request, 'management/add_student.html', {'form': form})

def add_course(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('students_list')
    return render(request, 'management/add_course.html', {'form': form})

class SearchStudentView(FormView):
    template_name = 'management/search_student.html'
    form_class = StudentSearchForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        students = Student.objects.all()
        if name:
            students = students.filter(name__icontains=name)
        return self.render_to_response(self.get_context_data(form=form, students=students))
