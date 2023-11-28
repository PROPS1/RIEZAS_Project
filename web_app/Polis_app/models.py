from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Patient(models.Model):
    """Информация о пациентах"""

    class Meta:
        db_table = "Patient"
        verbose_name = "Информация о пациентах"
        verbose_name_plural = "Информация о пациентах"

    Patient_indentificator = models.AutoField(primary_key=True, verbose_name="Идентификатор пациента")
    Patient_FIO = models.CharField(max_length=50, verbose_name="ФИО пациента")
    Patient_date_of_birth = models.DateTimeField(verbose_name="Дата рождения пациента")
    Patient_gender = models.CharField(max_length=50, verbose_name="Пол пациента")
    Patient_address = models.CharField(max_length=50, verbose_name="Адрес пациента")
    Patient_phone_number = models.CharField(max_length=50, verbose_name="Номер телефона пациента")

    def __str__(self):
        return self.Patient_indentificator


class Doctor(models.Model):
    """Информация о врачах"""

    class Meta:
        db_table = "Doctor"
        verbose_name = "Информация о врачах"
        verbose_name_plural = "Информация о врачах"

    Doctor_identificator = models.AutoField(primary_key=True, verbose_name="Идентификатор доктора")
    Doctor_FIO = models.CharField(max_length=50, verbose_name="ФИО доктора")
    Doctor_specialization = models.CharField(max_length=50, verbose_name="Специализация доктора")
    Doctor_experience = models.IntegerField(verbose_name="Опыт работы врача")
    Doctor_phone_number = models.CharField(max_length=50, verbose_name="Номер телефона врача")

    def __str__(self):
        return self.Doctor_identificator


class Treatment(models.Model):
    """Информация о лечении"""

    class Meta:
        db_table = "Treatment"
        verbose_name = "Информация о лечении"
        verbose_name_plural = "Информация о лечении"
    
    Treatment_identificator = models.AutoField(primary_key=True, verbose_name="Идентификатор лечения")
    Patient_identificator = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Идентификатор пациента")
    Doctor_identificator = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Идентификатор врача")
    Treatment_date_start = models.DateTimeField(verbose_name="Дата начала лечения")
    Treatment_date_end = models.DateTimeField(verbose_name="Дата окончания лечения")
    Diagnosis = models.CharField(max_length=100, verbose_name="Диагноз")
    Prescribed_treatment = models.CharField(max_length=100, verbose_name="Назначенные процедуры и лекарства")

    def __str__(self):
        return f"{self.Treatment_identificator} {self.Patient_identificator} {self.Doctor_identificator}"


class Payment(models.Model):
    """Информация о платежах"""

    class Meta:
        db_table = "Payment"
        verbose_name = "Информация о платежах"
        verbose_name_plural = "Информация о платежах"

    Payment_identificator = models.AutoField(primary_key=True, verbose_name="Идентификатор платежа") 
    Patient_identificator = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Идентификатор пациента")
    Payment_date = models.DateTimeField(verbose_name="Дата платежа")
    Payment_sum = models.IntegerField(verbose_name="Сумма платежа")
    Payment_status = models.CharField(max_length=50, verbose_name="Статус платежа")
    
    def __str__(self):
        return f"{self.Payment_identificator} {self.Patient_identificator}"


class Assignment(models.Model):
    """Информация о назначениях"""

    class Meta:
        db_table = "Assignment"
        verbose_name = "Информация о назначениях"
        verbose_name_plural = "Информация о назначениях"

    Assignment_identificator = models.AutoField(primary_key=True, verbose_name="Идентификатор назначения")
    Patient_identificator = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Идентификатор пациента")
    Doctor_identificator = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Идентификатор врача")
    Assignment_date = models.DateTimeField(verbose_name="Дата назначения")
    Assignment_description = models.CharField(max_length=100, verbose_name="Описание назначения")
    Assignment_status = models.CharField(max_length=50, verbose_name="Статус назначения")
        
    def __str__(self):
        return f"{self.Assignment_identificator} {self.Patient_identificator} {self.Doctor_identificator}"


class Polis(models.Model):
    """Информация о полисах"""

    class Meta:
        db_table = "Polis"
        verbose_name = "Информация о полисах"
        verbose_name_plural = "Информация о полисах"

    Polis_identificator = models.AutoField(primary_key=True, verbose_name="Идентификатор полиса")
    Patient_identificator = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Идентификатор пациента")
    Polis_date_start = models.DateTimeField(verbose_name="Дата начала действия полиса")
    Polis_date_end = models.DateTimeField(verbose_name="Дата окончания действия полиса")
    Polis_status = models.CharField(max_length=50, verbose_name="Статус полиса")
        
    def __str__(self):
        return f"{self.Polis_identificator} {self.Patient_identificator}"
