from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from forms import ProjectForm
from models import Project,Pics,Tech
from django.views.decorators.cache import never_cache
# Create your views here.

def show_resume(request):
  pass

attribs = ['year','title','role','teamsize','company','desc','pics','tech','img']

def populate_default_form(proj):
  form = ProjectForm(initial={ 'year': proj.year,
                               'title': proj.title,
                               'role': proj.role,
                               'teamsize': proj.teamsize,
                               'company': proj.company,
                               'desc': proj.desc })
  return form

@never_cache
def project_list(request):
  projects = [(x,Pics.objects.filter(project=x.id),Tech.objects.filter(project=x.id)) for x in Project.objects.all().order_by("year")]
  return render(request,"resume_view/list.html",{'ps': projects})


@never_cache
def update_project(request, pid):
  try:
    proj = Project.objects.get(pk=int(pid))
  except:
    return HttpResponseRedirect("/resume/project/")

  if request.method == 'GET':
    form = populate_default_form(proj)
    return render(request,"resume_view/update.html",{"form": form,
                                                     "idslash": "{0}/".format(pid),
                                                     "btntext": "Update"})
  elif request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      proj = copy_project_details(form,proj)
      proj.save()
      return HttpResponseRedirect("/resume/project/{0}/".format(proj.id))
   
def copy_project_details(form, proj):
  proj.year = form.cleaned_data['year']
  proj.title = form.cleaned_data['title']
  proj.role = form.cleaned_data['role']
  proj.teamsize = form.cleaned_data['teamsize']
  proj.company = form.cleaned_data['company']
  proj.desc = form.cleaned_data['desc']
  return proj

@never_cache
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
      proj = copy_project_details(form,Project())
      proj.save()
      return HttpResponseRedirect("/resume/project/{0}/".format(proj.id))
    else:
      return render(request,"resume_view/update.html",{"form": form,
                                                     "idslash": "",
                                                     "btntext": "Save"})

@never_cache
def data(request,year):
  pass
