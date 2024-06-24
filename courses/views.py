from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render 
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

from .models import Course , Module , Subject
# Create your views here.

class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner_id = self.request.user)

class OwnerEditMixin:
    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form )
# The default behavior for this method is saving the instance (for model forms) and redirecting the user
# to success_url. You override this method to automatically set the current user in the owner attribute
# of the object being saved. By doing so, you set the owner for an object automatically when it is saved.

class OwnerCourseMixin(OwnerMixin,LoginRequiredMixin , PermissionRequiredMixin):
    model = Course
    fields =  ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin , OwnerEditMixin):
    template_name = "courses/manage/course/form.html"

class ManageCourseListView(OwnerCourseMixin,ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'

    # def get_queryset(self) -> QuerySet[Any]:
    #     qs = super().get_queryset()
    #     return qs.filter(owner_id = self.request.user)

class CourseCreateView(OwnerCourseEditMixin , CreateView):
    permission_required = 'courses.add_course'

class CourseUpdateView(OwnerCourseEditMixin , UpdateView):
    permission_required = 'courses.change_course'

class CourseDeleteView(OwnerCourseEditMixin , DeleteView):
    template_name = "courses/manage/course/delete.html"
    permission_required = 'courses.delete_course'