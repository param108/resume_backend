from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from forms import ProjectForm
# Create your views here.

def show_resume(request):
  pass

attribs = ['year','title','role','teamsize','company','desc','pics','tech','img']

def update_project(request, pid):
  pass

def manage_project(request):
  if request.method == "GET":
    form = ProjectForm()
    return render(request,"resume_view/update.html",{"form": form,
                                                     "idslash": "",
                                                     "btntext": "Save"})
  # no fall through
  if request.method == "POST":
    form = ProjectForm(request.POST)
    if form.is_valid():
      pass
    else:
      return render(request,"resume_view/update.html",{"form": form,
                                                     "idslash": "",
                                                     "btntext": "Save"})

def data(request,year):
  pass
