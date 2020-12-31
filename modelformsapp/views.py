from django.shortcuts import render
from modelformsapp.models import Projects
from modelformsapp.forms import ProjectForm
# Create your views here.
def index(request):
    return render(request,'modelformsapp/index.html')

def ListProject(request):
    form=Projects.objects.all()
    return render(request,'modelformsapp/listprojects.html',{'form':form})

def AddProject(request):
    list=ProjectForm()
    if request.method=='POST':
        list=ProjectForm(request.POST)
        if list.is_valid():
            list.save()
        return index(request)
    return render(request,'modelformsapp/addprojects.html',{'list':list})
