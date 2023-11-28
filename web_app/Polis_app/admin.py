from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('Patient_indentificator', 'Patient_FIO', 'Patient_date_of_birth', 'Patient_gender', 'Patient_address', 'Patient_phone_number')

    search_fields = ('Patient_indentificator', 'Patient_FIO')

class DoctorAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('Doctor_identificator', 'Doctor_FIO', 'Doctor_specialization', 'Doctor_experience', 'Doctor_phone_number')

    search_fields = ('Doctor_identificator', 'Doctor_FIO')

class TreatmentAdmin(admin.ModelAdmin):
   # задаём методы для получения полей из связанных таблиц
    def my_patient(self, obj):
        return obj.Patient.Patient_identificator

    def my_doctor(self, obj):
        return obj.device.serial_number

    # задаём отображаемое название полей в админке
    my_patient.short_description = 'Пациент'
    my_doctor.short_description = 'Доктор'

    # поля для отображения
    list_display = ('Treatment_identificator', 'Patient_identificator', 'Doctor_identificator', 'Treatment_date_start', 'Treatment_date_end', 'Diagnosis', 'Prescribed_treatment')

    search_fields = ('Treatment_identificator', 'Patient_identificator', 'Doctor_identificator')

class PaymentAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблиц
    def my_patient(self, obj):
        return obj.Patient.Patient_identificator

    # задаём отображаемое название полей в админке
    my_patient.short_description = 'Пациент'

    # поля для отображения
    list_display = ('Payment_identificator', 'Patient_identificator', 'Payment_date', 'Payment_sum', 'Payment_status')

    search_fields = ('Payment_identificator', 'Patient_identificator')

class AssignmentAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблиц
    def my_patient(self, obj):
        return obj.Patient.Patient_identificator

    def my_doctor(self, obj):
        return obj.device.serial_number

    # задаём отображаемое название полей в админке
    my_patient.short_description = 'Пациент'
    my_doctor.short_description = 'Доктор'

    # поля для отображения
    list_display = ('Assignment_identificator', 'Patient_identificator', 'Doctor_identificator', 'Assignment_date', 'Assignment_description', 'Assignment_status')

    search_fields = ('Assignment_identificator', 'Patient_identificator', 'Doctor_identificator')

class PolisAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблиц
    def my_patient(self, obj):
        return obj.Patient.Patient_identificator

    # задаём отображаемое название полей в админке
    my_patient.short_description = 'Пациент'

    # поля для отображения
    list_display = ('Polis_identificator', 'Patient_identificator', 'Polis_date_start', 'Polis_date_end', 'Polis_status')

    search_fields = ('Polis_identificator', 'Patient_identificator')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Polis, PolisAdmin)
