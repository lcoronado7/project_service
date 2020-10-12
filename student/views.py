from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import *
from .forms import StudentForm, AcademicForm, Socio_economicForm, Family_groupForm
from .forms import Discapacity_relationForm, Financial_assistanceForm, Uneg_assistanceForm
from django.http import HttpResponseRedirect

# Create your views here.
##------>Student
#####################################################################
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    
    return render(
        request,
        'index.html'
    )

def search(request):
    url="/"
    if request.method == 'POST':
        print(str(request.POST.get('cedula')))
        queryset=request.POST.get('cedula')
        if queryset:
            print(str(request.POST))
            print(queryset)
            #student=Student.objects.filter(
            #    Q(cedula = queryset)
            #)
            try:
                student=Student.objects.get(cedula=queryset)
                print("student"+str(student))
                if student:
                    print(str(student.id))
                    url="/student-menu/"+str(student.id)
                    print(url)
                    return redirect(url)
            except:
                pass
    return redirect(url)

def delete_student(request,pk):
    try:
        instancia = Student.objects.get(id=pk)
        instancia.delete()
    except:
        pass
    return redirect('student_list')

def student_menu(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, "student/menu.html", {"student":student,"pk":pk})

class StudentViewSet(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(CreateView):
    model = Student
    template_name = "student/register.html"
    form_class = StudentForm

class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student/update.html"
    form_class = StudentForm
    def post(self, request, pk):
        student= Student.objects.get(id=pk)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("/student-menu/"+pk)
    
class StudentListView(ListView):
    model = Student
    template_name = "student/list.html"


##------>Academic
######################################################################
class AcademicCreateView(CreateView):
    model = Academic
    form_class = AcademicForm
    template_name = "academic/register.html"

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            academic = form.save(commit=False)
            academic.student = Student.objects.get(pk=pk)
            academic.save()
            return redirect("/student-menu/"+pk)

class AcademicUpdateView(UpdateView):
    model = Academic
    template_name = "academic/update.html"
    form_class = AcademicForm

    def post(self, request, pk):
        id_student=request.POST.get("student")
        print(str(id_student))
        form = self.form_class(request.POST)
        if form.is_valid():
            aux = Academic.objects.get(pk=pk)
            academic = form.save(commit=False)
            academic.id = aux.id
            academic.student = aux.student
            academic.save()
            return redirect("/student-menu/"+id_student)


##------>SocioEconomic
#####################################################################
class Socio_economicCreateView(CreateView):
    model = Socio_economic
    form_class = Socio_economicForm
    template_name = "socioeconomic/register.html"

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            socio = form.save(commit=False)
            socio.student = Student.objects.get(pk=pk)
            socio.save()
            return redirect("/student-menu/"+pk)

class Socio_economicUpdateView(UpdateView):
    model = Socio_economic
    form_class = Socio_economicForm
    template_name = "socioeconomic/update.html"

    def post(self, request, pk):
        id_student=request.POST.get("student")
        form = self.form_class(request.POST)
        if form.is_valid():
            aux = Socio_economic.objects.get(pk=pk)
            obj = form.save(commit=False)
            obj.id = aux.id
            obj.student = aux.student
            obj.save()
            return redirect("/student-menu/"+id_student)



##------>Family-group
#####################################################################
def family_list(request, pk):
    object_list = Family_group.objects.filter(socio_economic=pk)
    socio_economic=Socio_economic.objects.get(id=pk)
    student_object=socio_economic.id
    print("socio_economic id "+str(student_object))
    context = {'object_list': object_list, 'pk':pk,'socio_economic':socio_economic}
    return render(request, 'familygroup/list.html', context)

class Family_groupCreateView(CreateView):
    model = Family_group
    form_class = Family_groupForm
    template_name = "familygroup/register.html"
 
    def post(self, request, pk):
        
        print("socio_economic "+str(pk))
        form = self.form_class(request.POST)
        if(form.is_valid()):
            socio_economic=Socio_economic.objects.get(id=pk)
            student_id=socio_economic.student.id
            #aux = Family_group.objects.get(pk=pk)
            obj = form.save(commit=False)
            #obj.id = aux.id
            obj.socio_economic = socio_economic
            obj.save()
            return redirect("/student-menu/"+str(student_id))
    

class Family_groupUpdateView(UpdateView):
    model = Family_group
    template_name = "familygroup/update.html"
    form_class = Family_groupForm

    def post(self, request, pk):
        print(str(pk))
        form = self.form_class(request.POST)
        if(form.is_valid()):
            aux = Family_group.objects.get(id=pk)
            socio_economic=Socio_economic.objects.get(id=aux.socio_economic.id)
            student_id=socio_economic.student.id
            obj = form.save(commit=False)
            obj.id = aux.id
            obj.socio_economic =aux.socio_economic
            obj.save()
            return redirect("/student-menu/"+str(student_id))

def delete_family_group(request,pk):
    try:
        instancia = Family_group.objects.get(id=pk)
        socio_economic=Socio_economic.objects.get(id=instancia.socio_economic.id)
        student_id=socio_economic.student.id
        instancia.delete()
    except:
        pass
    return redirect("/student-menu/"+str(student_id))

##--------------->Discapacity
#############################################################################
def discapacity_list(request, pk):
    object_list = Discapacity_relation.objects.filter(socio_economic=pk)
    context = {'object_list': object_list, 'pk':pk}
    return render(request, 'discapacity/list.html', context)

class Discapacity_relationCreateView(CreateView):
    model = Discapacity_relation
    form_class = Discapacity_relationForm
    template_name = "discapacity/register.html"

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            socio_economic=Socio_economic.objects.get(id=pk)
            student_id=socio_economic.student.id
            obj.socio_economic = socio_economic

            obj.save()
            return redirect("/student-menu/"+str(student_id))

class Discapacity_relationUpdateView(UpdateView):
    model = Discapacity_relation
    template_name = "discapacity/update.html"
    form_class = Discapacity_relationForm

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            aux = Discapacity_relation.objects.get(id=pk)
            obj = form.save(commit=False)
            obj.id = aux.id
            obj.socio_economic = aux.socio_economic
            socio_economic=aux.socio_economic
            student_id=socio_economic.student.id
            obj.save()
            return redirect("/student-menu/"+str(student_id))

def delete_discapacity_relation(request,pk):
    try:
        instancia = Discapacity_relation.objects.get(id=pk)
        socio_economic=Socio_economic.objects.get(id=instancia.socio_economic.id)
        student_id=socio_economic.student.id
        instancia.delete()
    except:
        pass
    return redirect("/student-menu/"+str(student_id))

##-------->Financial_assistance
################################################################################
def financial_list(request, pk):
    object_list = Financial_assistance.objects.filter(socio_economic=pk)
    context = {'object_list': object_list, 'pk':pk}
    return render(request, 'financial_assistance/list.html', context)

class Financial_assistanceCreateView(CreateView):
    model = Financial_assistance
    form_class = Financial_assistanceForm
    template_name = "financial_assistance/register.html"

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            socio_economic=Socio_economic.objects.get(id=pk)
            student_id=socio_economic.student.id
            obj.socio_economic = socio_economic
            
            obj.save()
            return redirect("/student-menu/"+str(student_id))

class Financial_assistanceUpdateView(UpdateView):
    model = Financial_assistance
    template_name = "financial_assistance/update.html"
    form_class = Financial_assistanceForm

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            aux = Financial_assistance.objects.get(id=pk)
            obj = form.save(commit=False)
            obj.id = aux.id
            obj.socio_economic = aux.socio_economic
            socio_economic=aux.socio_economic
            student_id=socio_economic.student.id
            obj.save()
            return redirect("/student-menu/"+str(student_id))

def delete_financial_assistance(request,pk):
    try:
        instancia = Financial_assistance.objects.get(id=pk)
        socio_economic=Socio_economic.objects.get(id=instancia.socio_economic.id)
        student_id=socio_economic.student.id
        instancia.delete()
    except:
        pass
    return redirect("/student-menu/"+str(student_id))

##----------->UNEG_assistance
##########################################################################
def uneg_list(request, pk):
    object_list = Uneg_assistance.objects.filter(socio_economic=pk)
    context = {'object_list': object_list, 'pk':pk}
    return render(request, 'uneg_assistance/list.html', context)

class Uneg_assistanceCreateView(CreateView):
    model = Uneg_assistance
    form_class = Uneg_assistanceForm
    template_name = "uneg_assistance/register.html"

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            socio_economic=Socio_economic.objects.get(id=pk)
            student_id=socio_economic.student.id
            obj.socio_economic = socio_economic
            obj.save()
            return redirect("/student-menu/"+str(student_id))

class Uneg_assistanceUpdateView(UpdateView):
    model = Uneg_assistance
    template_name = "uneg_assistance/update.html"
    form_class = Uneg_assistanceForm

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            aux = Uneg_assistance.objects.get(id=pk)
            obj = form.save(commit=False)
            obj.id = aux.id
            obj.socio_economic = aux.socio_economic
            socio_economic=aux.socio_economic
            student_id=socio_economic.student.id
            obj.save()
            return redirect("/student-menu/"+str(student_id))    

def delete_uneg_assistance(request,pk):
    try:
        instancia = Uneg_assistance.objects.get(id=pk)
        socio_economic=instancia.socio_economic
        student_id=socio_economic.student.id
        instancia.delete()
    except:
        pass
    return redirect("/student-menu/"+str(student_id))
