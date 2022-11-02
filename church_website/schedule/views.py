from django.urls import reverse_lazy
from .forms import ScheduleForm
from .models import Schedule
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from .handlers import get_data
import json


# class ScheduleListView(ListView):
#     model = Schedule
#     queryset = Schedule.objects.all().filter(is_visible=True).last()
#     context_object_name = 'schedule'
#     template_name = 'schedule_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         schedule = self.queryset
#         data_dict = json.loads(schedule.data)
#         lst = []
#         for _, value_start in data_dict.items():
#             title_table = value_start['title_table']
#             for k, v in value_start['tables'].items():
#                 lst.append({title_table: v})
#         context['data'] = lst
#         return context


class ScheduleListView(ListView):
    model = Schedule
    queryset = Schedule.objects.all().filter(is_visible=True).order_by('-pk')
    context_object_name = 'schedule'
    template_name = 'schedule_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     schedule = self.queryset
    #     data_dict = json.loads(schedule.data)
    #     lst = []
    #     for _, value_start in data_dict.items():
    #         title_table = value_start['title_table']
    #         for k, v in value_start['tables'].items():
    #             lst.append({title_table: v})
    #     context['data'] = lst
    #     return context


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_dict = json.loads(context['schedule'].data)
        lst = []
        for _, value_start in data_dict.items():
            title_table = value_start['title_table']
            for k, v in value_start['tables'].items():
                lst.append({title_table: v})
        context['data'] = lst
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class ScheduleCreateView(LoginRequiredMixin, FormView):
    form_class = ScheduleForm
    template_name = 'schedule_create.html'
    success_url = reverse_lazy('schedule:schedule')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        document = request.FILES.get('file')
        if form.is_valid():
            title = form.cleaned_data['title']
            is_visible = form.cleaned_data['is_visible']
            data = get_data(document)
            Schedule.objects.create(title=title, is_visible=is_visible, data=data)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ScheduleUpdateView(LoginRequiredMixin, UpdateView):
    model = Schedule
    template_name = 'schedule_update.html'
    fields = '__all__'
    raise_exception = True


class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedule_delete.html'
    success_url = reverse_lazy('schedule:list')
