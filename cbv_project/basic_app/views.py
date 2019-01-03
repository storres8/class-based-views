from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from basic_app.models import School, Student


class CBView(View):
    def get(self,request):
        return HttpResponse("CBV!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = ''
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'basic_app/school_list1.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_detail.html'
