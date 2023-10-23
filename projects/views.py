from django.shortcuts import render
from projects.models import Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProjectFilter

# Create your views here.
def project_index(request):
    projects = Project.objects.all()

    page_num = request.GET.get("page")
    paginator = Paginator(projects, 3)

    project_filter = ProjectFilter(request.GET, queryset=projects)
    

    try:
        projects = paginator.page(page_num)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        "projects": projects,
        "project_filter": project_filter,
        "projects" : project_filter.qs,
    }
    return render(request,"projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request,"projects/project_detail.html", context)