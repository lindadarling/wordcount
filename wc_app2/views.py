import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from wc_app2.models import Student


def index(request):
    return HttpResponse("wc_app2index")


def add_student(request):
    for i in range(100):
        student=Student()
        flag=random.randrange(100)
        student.s_name="Allen %d" % flag
        student.s_age=flag
        student.save()
    return HttpResponse("%s  Add Sucessflly" % student.s_name)

def del_student(request):
    students=Student.objects.filter(s_age=2)
    for student in students:
        student.delete()

    return HttpResponse("%s  del Sucessflly" % student.s_name)




def get_student(request):
    #students = Student.objects.filter(s_age__gt=90).filter(s_age__lt=95)
    students=Student.objects.filter(s_age__lte=91).order_by("-s_age")
    #for student in students:
        #print(student.s_name)
    context={
        "hobby":"Play Games",
        "eat":"meat",
        "students":students,
    }
    #return HttpResponse("Student List")

    return render(request, "student_list.html", context=context)


