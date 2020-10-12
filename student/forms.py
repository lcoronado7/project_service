from django import forms
from .models import Student, Academic
from .models import Socio_economic, Family_group, Discapacity_relation
from .models import Financial_assistance, Uneg_assistance


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'cedula', 'sex', 'born_date', 'birth_place',
                'city', 'state', 'civil_state', 'home_address', 'phone', 'home_phone',
                'email', 'live_with', 'disability', 'certificate_number', 'disability_grade',
                'tecnic_help', 'medical_diagnostic', 'disability_causes', 'independent',
                'free_time_activities', 'contact_name', 'contact_relationship', 'contact_phone',
                'contact_address', 'contact_emergency_address', 'surgical_treatment',
                'permanent_treatment'
        )

class AcademicForm(forms.ModelForm):
    
    class Meta:
        model = Academic
        fields = ('institution_name','address', 'city_state', 'graduation_year', 'graduate_mention',
                'institution_type', 'grade_point_average', 'uneg_headquarters', 'uneg_headquarters', 'carrer_procject',
                'admission_date', 'entry_mode', 'academic_period', 'semester_level', 'academic_index',
                'status', 'additional_resources', 'university_conditions', 'extracurricular_activities'
        )

class Socio_economicForm(forms.ModelForm):
    
    class Meta:
        model = Socio_economic
        fields = ('family_head_name', 'family_head_relationship', 'house_type', 'house_condition',
                'average_amount_received', 'use_dinning_hall', 'schedule', 'transport',
                'company_name', 'job_perform', 'work_address', 'work_phone', 'salary'
        )

class Family_groupForm(forms.ModelForm):
    
    class Meta:
        model = Family_group
        fields = ('name','relationship', 'age', 'institute_grade', 'occupation', 'family_income',
                'live_at_home'
        )

class Discapacity_relationForm(forms.ModelForm):
    
    class Meta:
        model = Discapacity_relation
        fields = ('relationship', 'consists')

class Financial_assistanceForm(forms.ModelForm):
    
    class Meta:
        model = Financial_assistance
        fields = ('institution_name', 'monthly_amount')

class Uneg_assistanceForm(forms.ModelForm):
    
    class Meta:
        model = Uneg_assistance
        fields = ('benefit_type', 'income_date', 'last_assigned_area', 'last_supervisor')
