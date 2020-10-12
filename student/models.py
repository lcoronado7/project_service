from django.db import models
from django.utils import timezone
from django.urls import reverse
from decimal import Decimal

# Create your models here.
class Student(models.Model):
    
    id = models.AutoField(primary_key = True)
    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    cedula = models.CharField('Cedula', max_length=100)
    sex = models.CharField('Sexo', max_length=100)
    born_date = models.DateField('Fecha de nacimiento', default=timezone.now())
    birth_place = models.CharField('Lugar de nacimiento', max_length=100)
    city = models.CharField('Ciudad de nacimiento', max_length=100)
    state = models.CharField('Estado de nacimiento', max_length=100)
    civil_state = models.CharField('Estado civil', max_length=50)
    home_address = models.TextField('Direccion de domicilio')
    phone = models.CharField('telefono', max_length=50)
    home_phone = models.CharField('telefono de casa', max_length=50)
    email = models.EmailField('Correo electronico', max_length=254)
    live_with = models.CharField('Vives cob', max_length=255)
    disability = models.CharField('Discapacidad que posee', max_length=100)
    certificate_number = models.IntegerField('Numero de certificado de discapacidad')
    disability_grade = models.CharField('Gravedad de la discapacidad', max_length=100)
    tecnic_help = models.CharField('Tipo de ayuda tecnica', max_length=100)
    medical_diagnostic = models.TextField('Diagnostico medico')
    disability_causes = models.TextField('Causas de la discapacidad')
    independent = models.BooleanField('Independencia en actividades cotidianas', default=True)
    free_time_activities = models.TextField('Actividades de tiempo libre', null=True, blank=True)

    contact_name = models.CharField('Nombre de contacto', max_length=100)
    contact_relationship = models.CharField('Parentesco de contacto', max_length=100)
    contact_phone = models.CharField('numero de contacto', max_length=50)
    contact_address = models.TextField('Direccion de contacto')
    contact_emergency_address = models.TextField('Direccion de traslado de emergencia')

    surgical_treatment = models.TextField('Tratamiento quirurjico')
    permanent_treatment = models.TextField('Tratamiento permanente')

    def __str__(self):
        return f'{self.first_name}. C.I: {self.cedula}'

    class Meta:
        db_table = 'student'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def get_absolute_url(self):
        return reverse("student_update", kwargs={"pk": self.pk})


class Academic(models.Model):
    
    id = models.AutoField(primary_key = True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    institution_name = models.CharField('Nombre de la institucion', max_length=100)
    address = models.TextField('Direccion de la institucion')
    city_state = models.CharField('Ciudad y estado', max_length=100)
    graduation_year = models.CharField('Año de graduacion', max_length=4)
    graduate_mention = models.CharField('Bachiller en', max_length=100)
    institution_type = models.CharField('Tipo de institicion', max_length=50)
    grade_point_average = models.DecimalField('Promedio de notas', max_digits=4, decimal_places=2)
    
    uneg_headquarters = models.CharField('Nombre de la sede', max_length=50)
    carrer_procject = models.CharField('Proyecto de carrera', max_length=50)
    admission_date = models.DateField('Fecha de admision', default = timezone.now())
    entry_mode = models.CharField('Modalidad de ingreso', max_length=100)
    academic_period = models.CharField('Periodo academico que cursa', max_length=100)
    semester_level = models.IntegerField('Nivel de semestre')
    academic_index = models.DecimalField('Indice academico', max_digits=4, decimal_places=2)
    status = models.CharField('Estatus', max_length=50)
    additional_resources = models.CharField('Recursos adicionales', max_length=255)
    university_conditions = models.TextField('Condiciones de la universidad necesarias')
    extracurricular_activities = models.TextField('Le gustaria participar en actividades extracurriculares')


    def get_absolute_url(self):
        return reverse("academic_update", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'academic'
        managed = True
        verbose_name = 'Academic'
        verbose_name_plural = 'Academics'

class Socio_economic(models.Model):
    
    id = models.AutoField(primary_key = True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    family_head_name = models.CharField('Nombre del responsable de la falimia', max_length=100)
    family_head_relationship = models.CharField('Relacion con el responsable de la familia', max_length=50)
    house_type = models.CharField('tipo de vivienda', max_length=100)
    house_condition = models.CharField('condicion de vivienda', max_length=100)
    average_amount_received = models.DecimalField('monto promedio recibido', max_digits=50, decimal_places=2)
    use_dinning_hall = models.CharField('Usa el comedor, especifique el porque', max_length=255)
    schedule = models.CharField('horario para usar el comedor', max_length=50)
    transport = models.CharField('medio de trasporte, especifique', max_length=255)

    company_name = models.CharField('Nombre de la empresa', max_length=100)
    job_perform = models.CharField('Trabajo que desempeña', max_length=100)
    work_address = models.TextField('Direccion')
    work_phone = models.CharField('telefono', max_length=50)
    salary = models.DecimalField('Sueldo', max_digits=50, decimal_places=2, default=Decimal(0))

    def get_absolute_url(self):
        return reverse("socio_update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.student

    class Meta:
        db_table = 'socio_economic'
        managed = True
        verbose_name = 'Socio_economic'
        verbose_name_plural = 'Socio_economics'

class Family_group(models.Model):
    
    id = models.AutoField(primary_key = True)
    socio_economic = models.ForeignKey(Socio_economic, on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=100)
    relationship = models.CharField('Relacion', max_length=100)
    age = models.IntegerField('Edad')
    institute_grade = models.CharField('Grado de institucion', max_length=100)
    occupation = models.CharField('Ocupacion u oficio', max_length=100)
    family_income = models.DecimalField('Ingreso familiar', max_digits=50, decimal_places=2)
    live_at_home = models.BooleanField('Vive en el hogar', default=True)

    def __str__(self):
        return self.socio_economic

    def get_absolute_url(self):
        return reverse("family_group_update", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'family_group'
        managed = True
        verbose_name = 'Family_group'
        verbose_name_plural = 'Family_groups'

class Discapacity_relation(models.Model):
    
    id = models.AutoField(primary_key = True)
    socio_economic = models.ForeignKey(Socio_economic, on_delete=models.CASCADE)
    relationship = models.CharField('Relacion', max_length=100)
    consists = models.TextField('Consiste')

    def __str__(self):
        return self.socio_economic

    def get_absolute_url(self):
        return reverse("discapacity_update", kwargs={"pk": self.pk})

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Discapacity_relation'
        verbose_name_plural = 'Discapacity_relations'
        
class Financial_assistance(models.Model):
    
    id = models.AutoField(primary_key = True)
    socio_economic = models.ForeignKey(Socio_economic, on_delete=models.CASCADE)
    institution_name = models.CharField('Nombre de la institucion', max_length=100)
    monthly_amount = models.DecimalField('Monto mensual', max_digits=50, decimal_places=2)

    def __str__(self):
        return self.socio_economic

    def get_absolute_url(self):
        return reverse("financial_update", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'financial_assistance'
        managed = True
        verbose_name = 'Financial_assistance'
        verbose_name_plural = 'Financial_assistances'

class Uneg_assistance(models.Model):

    id = models.AutoField(primary_key = True)
    socio_economic = models.ForeignKey(Socio_economic, on_delete=models.CASCADE)
    benefit_type = models.CharField('tipo de beneficio', max_length=100)
    income_date = models.CharField('fecha de ingreso', max_length=100)
    last_assigned_area = models.CharField('ultima area asignada', max_length=100)
    last_supervisor = models.CharField('ultimo supervisor', max_length=100)

    def __str__(self):
        return self.socio_economic

    def get_absolute_url(self):
        return reverse("uneg_update", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'uneg_assistance'
        managed = True
        verbose_name = 'Uneg_assistance'
        verbose_name_plural = 'Uneg_assistances'