from django.urls import path
from .views import StudentCreateView, StudentListView, StudentUpdateView, student_menu, index, search, delete_student
from .views import AcademicCreateView, AcademicUpdateView
from .views import Socio_economicCreateView, Socio_economicUpdateView
from .views import Family_groupCreateView, family_list, Family_groupUpdateView,delete_family_group
from .views import Discapacity_relationCreateView, discapacity_list, Discapacity_relationUpdateView, delete_discapacity_relation
from .views import Financial_assistanceCreateView, financial_list, Financial_assistanceUpdateView, delete_financial_assistance
from .views import Uneg_assistanceCreateView, uneg_list, Uneg_assistanceUpdateView, delete_uneg_assistance

urlpatterns = [
    path('', index , name='home'),
    path('student-list', StudentListView.as_view(), name='student_list'),
    path('student_search', search, name='student_search'),
    path('student-register', StudentCreateView.as_view(), name='student_register'),
    path('student_delete/<pk>', delete_student, name='student_delete'),
    path('student-menu/<pk>', student_menu, name='student_menu'),
    path('student-update/<pk>', StudentUpdateView.as_view(), name='student_update'),
    path('academic-register/<pk>', AcademicCreateView.as_view(), name='academic_create'),
    path('academic-update/<pk>', AcademicUpdateView.as_view(), name='academic_update'),
    path('socio-register/<pk>', Socio_economicCreateView.as_view(), name='socio_register'),
    path('socio-update/<pk>', Socio_economicUpdateView.as_view(), name='socio_update'),
    path('family-register/<pk>', Family_groupCreateView.as_view(), name='family_register'),
    path('family-list/<pk>', family_list, name='family_list'),
    path('family-update/<pk>', Family_groupUpdateView.as_view(), name='family_update'),
    path('family-delete/<pk>', delete_family_group, name='family_delete'),
    path('discapacity-register/<pk>', Discapacity_relationCreateView.as_view(), name='discapacity_register'),
    path('discapacity-list/<pk>', discapacity_list, name='discapacity_list'),
    path('discapacity-update/<pk>', Discapacity_relationUpdateView.as_view(), name='discapacity_update'),
    path('discapacity-delete/<pk>', delete_discapacity_relation, name='discapacity_delete'),
    path('financial-register/<pk>', Financial_assistanceCreateView.as_view(), name='financial_register'),
    path('financial-list/<pk>', financial_list, name='financial_list'),
    path('financial-update/<pk>', Financial_assistanceUpdateView.as_view(), name='financial_update'),
    path('financial-delete/<pk>', delete_financial_assistance, name='financial_delete'),
    path('uneg-register/<pk>', Uneg_assistanceCreateView.as_view(), name='uneg_register'),
    path('uneg-list/<pk>', uneg_list, name='uneg_list'),
    path('uneg-update/<pk>', Uneg_assistanceUpdateView.as_view(), name='uneg_update'),
    path('uneg-delete/<pk>', delete_uneg_assistance, name='uneg_delete'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)