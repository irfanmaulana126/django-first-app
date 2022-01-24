from enum import Flag
from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from userAuth.models import *
import uuid
# Create your models here.
class MasterDataFaskes(models.Model):
    
    user = models.ForeignKey(CustomUser, blank=True,null=True, on_delete=models.SET_NULL, db_column='user_id')
    kode_pkmlama= models.CharField(max_length=12, null=True, blank=True)
    nama_pkm = models.CharField(max_length=200, null=True,blank=True)
    kode_pkm = models.CharField(max_length=7)
    telp = models.CharField(max_length=13, null=True, blank=True)
    provinsi = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL, db_column='provinsi_id')
    kabupaten = models.ForeignKey(Regencies, blank=True, null=True, on_delete=models.SET_NULL, db_column='kabupaten_id')
    kecamatan = models.ForeignKey(Districts, blank=True, null=True, on_delete=models.SET_NULL, db_column='kecamatan_id')
    alamat = models.TextField(blank=True, null=True)
    kode_kp = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=5, blank=True,null=True)
    is_sync = models.BooleanField('Synced', blank=True, null=True)

class RegisFaskes(models.Model):
    KARAKTER_WILAYAH = (
        (1, 'TERPENCIL'),
        (2, 'PERKOTAAN'),
        (3, 'SANGAT TERPENCIL'),
        (4, 'PEDESAAN')
    )
    STATUS = (
        ('RAWAT INAP', 'RAWAT INAP'),
        ('NON RAWAT INAP', 'NON RAWAT INAP'),   
    )
    STATUS_PENDAPATAN = (
        ('BLUD', 'BLUD'),
        ('NON BLUD', 'NON BLUD'),   
    )
    id_regis = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode_pkm = models.CharField(max_length=11, unique=True, blank=True, null=True)
    nama_pkm = models.CharField(max_length=200, blank=True, null=True)
    no_surat = models.CharField(max_length=50, blank=True, null=True)
    prihal_surat = models.CharField(max_length=50, blank=True, null=True)
    tgl_surat = models.DateField(blank=True, null=True)
    telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    pendaftaran = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='RAWAT INAP', blank=False, null=True,choices=STATUS)
    status_pendapatan = models.CharField(max_length=50, default='NON BLUD', blank=False, null=True,choices=STATUS_PENDAPATAN)
    karakterwilayah = models.IntegerField(default=2,blank=False, null=True, choices=KARAKTER_WILAYAH)
    keldes_id = models.ManyToManyField(Villages)
    foto = models.ImageField('Media Pict', upload_to="foto/%Y-%m-%d/",blank=True, null=True)
    file_suratkedinasan_kabupaten =  models.FileField('Dokumen',upload_to='dokumen/f1/%y-%m-%d/',blank=True, null=True)
    is_file_suratkepdinas_kabupaten = models.BooleanField(blank=True, null=True)
    kom_file_suratkepdinas_kabupaten = models.TextField(blank=True, null=True)
    file_suratizinpuskesmas = models.FileField('Dokumen', upload_to="dokumen/f2/%Y-%m-%d/")
    is_file_suratizinpuskesmas = models.BooleanField(blank=True, null=True)
    kom_file_suratizinpuskesmas = models.TextField(blank=True, null=True)
    file_skbupati = models.FileField('Dokumen', upload_to="dokumen/f3/%Y-%m-%d/")
    is_file_skbupati = models.BooleanField(blank=True, null=True)
    kom_file_skbupati = models.TextField(blank=True, null=True)
    file_rekomendasikepdinas_provinsi = models.FileField('Dokumen', upload_to="dokumen/f4/%Y-%m-%d/")
    is_file_rekomendasikepdinas_provinsi = models.BooleanField(blank=True, null=True)
    kom_rekomendasikepdinas_provinsi = models.TextField(blank=True, null=True)
    file_verifikasipenilaian = models.FileField('Dokumen', upload_to="dokumen/f5/%Y-%m-%d/")
    is_file_verifikasipenilaian = models.BooleanField(blank=True, null=True)
    kom_verifikasipenilaian = models.TextField(blank=True, null=True)
    verif = models.IntegerField(default=0)
    verified_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL ,blank=True, null=True)
    provinsi = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL, db_column='provinsi_id')
    kabupaten = models.ForeignKey(Regencies, blank=True, null=True, on_delete=models.SET_NULL, db_column='kabupaten_id')
    kecamatan = models.ForeignKey(Districts, blank=True, null=True, on_delete=models.SET_NULL, db_column='kecamatan_id')
    alamat = models.TextField(blank=True, null=True)
    kode_kp = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_column='created_by', related_name='has_created_by' , blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_column='updated_by', related_name='has_updated_by' , blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_req_del = models.BooleanField(default=False)
    is_rej_del = models.BooleanField(default=False)
    file1_del = models.FileField('Dokumen', upload_to="dokumen/del/f1/%Y-%m-%d/", null=True, blank=True)
    file2_del = models.FileField('Dokumen', upload_to="dokumen/del/f2/%Y-%m-%d/", null=True, blank=True)
    comment_del = models.CharField(max_length=150, null=True, blank=True)
    comment_rej_del = models.CharField(max_length=150, null=True, blank=True)

class PerubahanFaskes(models.Model):
    KARAKTER_WILAYAH = (
        (1, 'TERPENCIL'),
        (2, 'PERKOTAAN'),
        (3, 'SANGAT TERPENCIL'),
        (4, 'PEDESAAN')
    )
    STATUS = (
        ('RAWAT INAP', 'RAWAT INAP'),
        ('NON RAWAT INAP', 'NON RAWAT INAP'),
        
    )
    STATUS_PENDAPATAN = (
        ('BLUD', 'BLUD'),
        ('NON BLUD', 'NON BLUD'),   
    )
    id_perubahan = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regis = models.ForeignKey(RegisFaskes, related_name='has_changed', on_delete=models.CASCADE)
    nama_pkm = models.CharField(max_length=200, null=True, blank=True)
    no_surat = models.CharField(max_length=50, blank=True, null=True)
    perihal_surat = models.CharField(max_length=50, blank=True, null=True)
    tgl_surat = models.DateField(blank=True, null=True)
    telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    pendaftaran = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, default="RAWAT INAP", blank=False, null=True, choices=STATUS)
    status_pendapatan = models.CharField(max_length=50, default='NON BLUD', blank=False, null=True,choices=STATUS_PENDAPATAN)
    karakterwilayah = models.IntegerField(default=2,blank=False, null=True, choices=KARAKTER_WILAYAH)
    keldes_id = models.ManyToManyField(Villages)
    foto = models.ImageField('Media Pict',upload_to="foto/%Y-%m-%d/", blank=True, null=True)
    file_suratkepdinas_kabupaten = models.FileField('Dokumen', upload_to="dokumen/f1/%Y-%m-%d/")
    is_file_suratkepdinas_kabupaten = models.BooleanField(blank=True, null=True)
    kom_file_suratkepdinas_kabupaten = models.TextField(blank=True, null=True)
    file_skbupati = models.FileField('Dokumen', upload_to="dokumen/f3/%Y-%m-%d/")
    is_file_skbupati = models.BooleanField(blank=True, null=True)
    kom_file_skbupati = models.TextField(blank=True, null=True)
    verif = models.IntegerField(default=0)
    verified_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL ,blank=True, null=True)
    provinsi = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL, db_column='provinsi_id')
    kabupaten = models.ForeignKey(Regencies, blank=True, null=True, on_delete=models.SET_NULL, db_column='kabupaten_id')
    kecamatan = models.ForeignKey(Districts, blank=True, null=True, on_delete=models.SET_NULL, db_column='kecamatan_id')
    alamat = models.TextField(blank=True, null=True)
    kode_kp = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_column='created_by', related_name='has_created_by_changed' , blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, db_column='updated_by', related_name='has_updated_by_changed' , blank=True, null=True) 

    def get_villages (self, obj):
        return "\n , ".join([p.name for p in obj.Villages.all()])   

    def get_villages_values(self):
        ret = ''
        for dept in self.keldes_id.all():
            ret = ret + dept.name + ','

        return ret[:-1]

class Fodals(models.Model):
    regis_id = models.ForeignKey(RegisFaskes, related_name='has_fodals', on_delete=models.CASCADE)
    nama_foto = models.ImageField('Media Fodals',upload_to="foto/fodals/%Y-%m-%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

class FodalsChanged(models.Model):
    regis_id = models.ForeignKey(PerubahanFaskes, related_name='has_fodals_changed', on_delete=models.CASCADE)
    nama_foto = models.ImageField('Media Fodals',upload_to="foto/fodals/%Y-%m-%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

class Wilkers(models.Model):
    regis_id = models.ForeignKey(RegisFaskes, related_name='has_wilkers', on_delete=models.CASCADE)
    kelurahan_id = models.ForeignKey(Villages, related_name='has_kel_wilkers', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)