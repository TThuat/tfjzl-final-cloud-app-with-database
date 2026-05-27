from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


def home(request):
    return HttpResponse("Online Course Home Page")


def submit(request, course_id):

    course = get_object_or_404(
        Course,
        pk=course_id
    )

    return HttpResponse(
        "Submit successful"
    )


def show_exam_result(
    request,
    course_id,
    submission_id
):

    context = {
        'grade': 100
    }

    return render(
        request,
        'onlinecourse/exam_result.html',
        context
    )