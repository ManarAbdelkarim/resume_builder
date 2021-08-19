from django.shortcuts import render
from django.views.generic import CreateView 
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request, 'index.html',{})

class PersonalInfoCreateView(CreateView):
    template_name = "personal_create.html"
    model = PersonalInfo
    fields = '__all__'

class WorkExperienceCreateView(CreateView):
    template_name = "work_create.html"
    model = WorkExperience
    fields = ['job_title','company','personal_info','description']

class EducationCreateView(CreateView):
    template_name = "education_create.html"
    model = Education
    fields =['major','personal_info','description']

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