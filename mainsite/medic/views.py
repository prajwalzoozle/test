from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django import forms
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.detail import SingleObjectMixin

# Create your views here.


def register_patient(request):
    return render(request,'medic/register.html', {'form':RegisterForm})


def register_patient_validation(request):
    form = RegisterForm(request.POST, request.FILES)
    if form.is_valid():
        name = form.cleaned_data["name"]
        phone_no = form.cleaned_data["phone_no"]
        password = form.cleaned_data["password"]
        patient_obj = Patient(name=name, phone_no=phone_no, password=password)
        patient_obj.save()
        patient_obj.photo = form.cleaned_data['picture']
        patient_obj.save()

        return render(request,'medic/login.html',{})
    else:
        return render(request,'medic/register.html',{'form':form})


def add_medicine(request):
    if request.POST:
        med = Medicine()
        form = MedicineForm(request.POST, instance=med)
        if form.is_valid:
            form.save()
            return render(request, 'Medic/login.html', {})
        else:
            return render(request, 'Medic/login.html', {'form': form})
    else:
        return render(request, 'Medic/addmed.html', {'form':MedicineForm})


class ListDoctors(View):
    '''
    Listing Doctors with Builtin View
    '''

    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        return render(request,'Medic/listing.html',{'doctors': doctors})


class DetailMedicine(DetailView):
    model = Medicine

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListMedicine(ListView):
    model = Medicine
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class EditPatient(UpdateView):
    model = Patient
    fields = ['name','phone_no','photo','password']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.id
        return context


class DeletePatient(DeleteView):
    model = Patient
    success_url = reverse_lazy('medic:index')


class WardFillings(SingleObjectMixin, ListView):
    paginate_by = 3
    template_name = 'Medic/ward_fillings.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Ward.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ward'] = self.object
        return context

    def get_queryset(self):
        return self.object.patient_set.all()


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]