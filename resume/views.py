from django.shortcuts import render
from django.views.generic import CreateView 
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request, 'cv.html',{})

class PersonalInfoCreateView(CreateView):
    template_name = "index.html"
    model = PersonalInfo
    fields = '__all__'

def cv_maker(request,id):
    user_id = id
    personal = PersonalInfo.objects.get(id=user_id)
    info = {
    'full_name' :  personal.full_name,
    'job_title' :  personal.job_title,
    'email' : personal.email,
    'website' : personal.website,
    'phone_number' : personal.phone_number,
    'personal_info' : personal.personal_info,
    'key_skills' : personal.key_skills,
    'job_title_c' : personal.job_title,
    'company' : personal.company,
    'description_c' : personal.description_c,
    'university_name' : personal.university_name,
    'major' : personal.major,
    'description_u' : personal.description_u,
    'user_image' : personal.user_image
    }
    
    return render(request, 'cv.html',{'info': info})
   

# class WorkExperienceCreateView(CreateView):
#     template_name = "work_create.html"
#     model = WorkExperience
#     fields = ['job_title','company','personal_info','description']

# class EducationCreateView(CreateView):
#     template_name = "education_create.html"
#     model = Education
#     fields =['major','personal_info','description']

# @api_view(['GET'])
# def is_passed(request):
#     '''
#     check if a relation between the user and a problem "the user solved the problem" exist
#     '''
#     problem = request.GET['problem']
#     try:
#         Passed.objects.get(user_id=request.user.id, problem_id=problem)
#         return HttpResponse(True,content_type="application/json")
#     except:
#         return HttpResponse(False,content_type="application/json")