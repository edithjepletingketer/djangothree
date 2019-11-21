from django.shortcuts import render


from .forms import CourseForm
from .models import Course
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest

def add_course(request):
	# form=CourseForm()
	# return render(request,"add_course.html",{"form":form})

	if request.method=="POST":
		form=CourseForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return HttpResponseBadRequest()
				
			# return redirect("list_course")
	else:
		form=CourseForm()
	return render(request,"add_course.html",{"form":form})

def list_course(request):
	courses = Course.objects.all
	return render(request,"list_course.html",
		{"courses":courses})

def edit_course(request,pk):
	course=Course.objects.get(pk=pk)
	
	if request.method=="POST":
		form=CourseForm(request.POST,instance=course)
		if form.is_valid():
			form.save()
			return redirect("add_course")

	else:
		form=CourseForm(instance=course)
		return render(request,"edit_course.html",{"form":form})


def edit_course(request,pk):
	course=Course.objects.get(pk=pk)
	
	if request.method=="POST":
		form=CourseForm(request.POST,instance=course)
		if form.is_valid():
			form.save()
			return redirect("list_course")

	else:
		form=CourseForm(instance=course)
		return render(request,"edit_course.html",{"form":form})		





# Create your views here.
