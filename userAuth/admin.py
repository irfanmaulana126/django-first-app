from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','nik','phone', 'is_verified','province','regencies')
    search_fields = ('username','email','nik','phone', 'is_verified','province__name','regencies__name')

@admin.register(models.Island)
class IslandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'pulau')

@admin.register(models.Regencies)
class RegenciesAdmin(admin.ModelAdmin):
    list_display = ('name','id_prov')

@admin.register(models.Districts)
class DistrictsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Villages)
class VillagesAdmin(admin.ModelAdmin):
    pass
