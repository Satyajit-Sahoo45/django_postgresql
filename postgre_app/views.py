from django.shortcuts import render
from .models import *

def home(request):
    dept_data = People.objects.all()
    people_courses = People.objects.prefetch_related('courses')

    person_course_data = {}

    for data in people_courses:
        course_titles = ', '.join(course.title for course in data.courses.all())
        person_course_data[data.name] = course_titles
        
    return render(request, "home.html", {'person_course_data':person_course_data})
