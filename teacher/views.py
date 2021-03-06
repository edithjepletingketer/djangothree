from django.shortcuts import render

from .forms import TeacherForm
from .models import Teacher
from django.shortcuts import redirect


def add_teacher(request):
	# form=TeacherForm()
	# return render(request,"add_teacher.html",{"form":form})

	if request.method=="POST":
		form=TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list_teacher")
	else:
		form=TeacherForm()
	return render(request,"add_teacher.html",{"form":form})


def list_teacher(request):
	teachers = Teacher.objects.all
	return render(request,"list_teacher.html",
		{"teachers":teachers})

def teacher_detail(request,pk):
	teacher=Teacher.objects.get(pk=pk)
	return render(request,"teacher_detail.html",{"teacher":teacher})	
     
def edit_teacher(request,pk):
	teacher=Teacher.objects.get(pk=pk)
	
	if request.method=="POST":
		form=TeacherForm(request.POST,instance=teacher)
		if form.is_valid():
			form.save()
			return redirect("add_teacher")
	else:
		form=TeacherForm(instance=teacher)
		return render(request,"edit_teacher.html",{"form":form})


def edit_teacher(request,pk):
	teacher=Teacher.objects.get(pk=pk)
	
	if request.method=="POST":
		form=TeacherForm(request.POST,instance=teacher)
		if form.is_valid():
			form.save()
			return redirect("list_teacher")
	else:
		form=TeacherForm(instance=teacher)
		return render(request,"edit_teacher.html",{"form":form})

# Create your views here.
