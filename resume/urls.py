from . views  import *
from django.urls import path


urlpatterns = [
    path('cv/<int:id>', cv_maker , name='cv'),
    path('', PersonalInfoCreateView.as_view(), name='personal_create'),
    # path('personal/work/', WorkExperienceCreateView.as_view(), name='work_create'),
    # path('personal/work/education/', EducationCreateView.as_view(), name='ducation_create'),

]