from . views  import *
from django.urls import path


urlpatterns = [
    path('', home , name='home'),
    path('personal/', PersonalInfoCreateView.as_view(), name='personal_create'),
    path('personal/work/', WorkExperienceCreateView.as_view(), name='work_create'),
    path('personal/work/education/', EducationCreateView.as_view(), name='ducation_create'),

]