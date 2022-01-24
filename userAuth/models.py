import re
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class Island(models.Model):

    name = models.CharField(max_length=100, db_column='island_name')
    last_number = models.IntegerField()
    is_active = models.BooleanField('Aktif', default=True, db_column='is_active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MASTER PULAU'

class Province (models.Model):
    name = models.CharField(max_length=100, db_column='province_name')
    pulau = models.ForeignKey(Island, blank=True, null=True,on_delete=models.SET_NULL, db_column='id_pulau')
    is_active = models.BooleanField('Aktif', blank=True, null=True, default=True, db_column='is_active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MASTER PROVINSI'

class Regencies(models.Model):

    name = models.CharField(max_length=100, db_column='district_name')
    id_prov = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL, db_column='id_prov')
    is_active = models.BooleanField('Aktif', blank=True, null=True, default=True, db_column='is_active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MASTER KABUPATEN/KOTA'

class Districts(models.Model):

    name = models.CharField(max_length=100, db_column='sub_district_name')
    district = models.ForeignKey(Regencies, blank=True, null=True, on_delete=models.SET_NULL, db_column='district_id')
    is_active = models.BooleanField('Aktif', blank=True, null=True, default=True, db_column='is_active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MASTER KECAMATAN'

class Villages(models.Model):

    name = models.CharField(max_length=100, db_column='kel_name')
    village = models.ForeignKey(Districts, blank=True, null=True, on_delete=models.SET_NULL, db_column='village_id')
    is_active = models.BooleanField('Aktif', blank=True, null=True, default=True, db_column='is_active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'MASTER KELURAHAN/DESA'

class Roles(models.Model):
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Master Role'

class CustomUser(AbstractUser):
    USER_TYPE = (
        (0, 'Belum Terdaftar'),
        (1, 'Admin'),
        (2, 'Verifikator Data'),
        (3, 'Pusdatin'),
        (4, 'Dinas Kesehatan'),
        (5, 'Puskesmas'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    roles = models.ManyToManyField(Roles)
    role = models.IntegerField(default=0, choices=USER_TYPE)
    is_email_confirm = models.BooleanField(default=False)
    phone =  models.CharField(max_length=14, blank=True, null=True)
    nik = models.CharField(max_length=16, blank=True, null=True)
    province = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL)
    regencies = models.ForeignKey(Regencies, blank=True, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(Districts, blank=True, null=True, on_delete=models.SET_NULL)
    village = models.ForeignKey(Villages, blank=True, null=True, on_delete=models.SET_NULL)
    nmpimp = models.CharField(max_length=100, blank=True, null=True)
    telpimp = models.CharField(max_length=13, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name