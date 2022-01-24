# Generated by Django 4.0 on 2021-12-15 01:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisFaskes',
            fields=[
                ('id_regis', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_pkm', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('nama_pkm', models.CharField(blank=True, max_length=200, null=True)),
                ('no_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('prihal_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_surat', models.DateField(blank=True, null=True)),
                ('telp', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('pendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('RAWAT INAP', 'RAWAT INAP'), ('NON RAWAT INAP', 'NON RAWAT INAP')], default='RAWAT INAP', max_length=50, null=True)),
                ('status_pendapatan', models.CharField(choices=[('BLUD', 'BLUD'), ('NON BLUD', 'NON BLUD')], default='NON BLUD', max_length=50, null=True)),
                ('karakterwilayah', models.IntegerField(choices=[(1, 'TERPENCIL'), (2, 'PERKOTAAN'), (3, 'SANGAT TERPENCIL'), (4, 'PEDESAAN')], default=2, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto/%Y-%m-%d/', verbose_name='Media Pict')),
                ('file_suratkedinasan_kabupaten', models.FileField(blank=True, null=True, upload_to='dokumen/f1/%y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_suratkepdinas_kabupaten', models.BooleanField(blank=True, null=True)),
                ('kom_file_suratkepdinas_kabupaten', models.TextField(blank=True, null=True)),
                ('file_suratizinpuskesmas', models.FileField(upload_to='dokumen/f2/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_suratizinpuskesmas', models.BooleanField(blank=True, null=True)),
                ('kom_file_suratizinpuskesmas', models.TextField(blank=True, null=True)),
                ('file_skbupati', models.FileField(upload_to='dokumen/f3/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_skbupati', models.BooleanField(blank=True, null=True)),
                ('kom_file_skbupati', models.TextField(blank=True, null=True)),
                ('file_rekomendasikepdinas_provinsi', models.FileField(upload_to='dokumen/f4/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_rekomendasikepdinas_provinsi', models.BooleanField(blank=True, null=True)),
                ('kom_rekomendasikepdinas_provinsi', models.TextField(blank=True, null=True)),
                ('file_verifikasipenilaian', models.FileField(upload_to='dokumen/f5/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_verifikasipenilaian', models.BooleanField(blank=True, null=True)),
                ('kom_verifikasipenilaian', models.TextField(blank=True, null=True)),
                ('verif', models.IntegerField(default=0)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kode_kp', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_req_del', models.BooleanField(default=False)),
                ('is_rej_del', models.BooleanField(default=False)),
                ('file1_del', models.FileField(blank=True, null=True, upload_to='dokumen/del/f1/%Y-%m-%d/', verbose_name='Dokumen')),
                ('file2_del', models.FileField(blank=True, null=True, upload_to='dokumen/del/f2/%Y-%m-%d/', verbose_name='Dokumen')),
                ('comment_del', models.CharField(blank=True, max_length=150, null=True)),
                ('comment_rej_del', models.CharField(blank=True, max_length=150, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_created_by', to='userAuth.customuser')),
                ('kabupaten', models.ForeignKey(blank=True, db_column='kabupaten_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.regencies')),
                ('kecamatan', models.ForeignKey(blank=True, db_column='kecamatan_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.districts')),
                ('keldes_id', models.ManyToManyField(to='userAuth.Villages')),
                ('provinsi', models.ForeignKey(blank=True, db_column='provinsi_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.province')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_updated_by', to='userAuth.customuser')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Wilkers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('kelurahan_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_kel_wilkers', to='userAuth.villages')),
                ('regis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_wilkers', to='regpus.regisfaskes')),
            ],
        ),
        migrations.CreateModel(
            name='PerubahanFaskes',
            fields=[
                ('id_perubahan', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_pkm', models.CharField(blank=True, max_length=200, null=True)),
                ('no_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('perihal_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_surat', models.DateField(blank=True, null=True)),
                ('telp', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('pendaftaran', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('RAWAT INAP', 'RAWAT INAP'), ('NON RAWAT INAP', 'NON RAWAT INAP')], default='RAWAT INAP', max_length=50, null=True)),
                ('status_pendapatan', models.CharField(choices=[('BLUD', 'BLUD'), ('NON BLUD', 'NON BLUD')], default='NON BLUD', max_length=50, null=True)),
                ('karakterwilayah', models.IntegerField(choices=[(1, 'TERPENCIL'), (2, 'PERKOTAAN'), (3, 'SANGAT TERPENCIL'), (4, 'PEDESAAN')], default=2, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto/%Y-%m-%d/', verbose_name='Media Pict')),
                ('file_suratkepdinas_kabupaten', models.FileField(upload_to='dokumen/f1/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_suratkepdinas_kabupaten', models.BooleanField(blank=True, null=True)),
                ('kom_file_suratkepdinas_kabupaten', models.TextField(blank=True, null=True)),
                ('file_skbupati', models.FileField(upload_to='dokumen/f3/%Y-%m-%d/', verbose_name='Dokumen')),
                ('is_file_skbupati', models.BooleanField(blank=True, null=True)),
                ('kom_file_skbupati', models.TextField(blank=True, null=True)),
                ('verif', models.IntegerField(default=0)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kode_kp', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_created_by_changed', to='userAuth.customuser')),
                ('kabupaten', models.ForeignKey(blank=True, db_column='kabupaten_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.regencies')),
                ('kecamatan', models.ForeignKey(blank=True, db_column='kecamatan_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.districts')),
                ('keldes_id', models.ManyToManyField(to='userAuth.Villages')),
                ('provinsi', models.ForeignKey(blank=True, db_column='provinsi_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.province')),
                ('regis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_changed', to='regpus.regisfaskes')),
                ('updated_by', models.ForeignKey(blank=True, db_column='updated_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_updated_by_changed', to='userAuth.customuser')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='MasterDataFaskes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_pkmlama', models.CharField(blank=True, max_length=12, null=True)),
                ('nama_pkm', models.CharField(blank=True, max_length=200, null=True)),
                ('kode_pkm', models.CharField(max_length=7)),
                ('telp', models.CharField(blank=True, max_length=13, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kode_kp', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('is_sync', models.BooleanField(blank=True, null=True, verbose_name='Synced')),
                ('kabupaten', models.ForeignKey(blank=True, db_column='kabupaten_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.regencies')),
                ('kecamatan', models.ForeignKey(blank=True, db_column='kecamatan_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.districts')),
                ('provinsi', models.ForeignKey(blank=True, db_column='provinsi_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.province')),
                ('user', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='FodalsChanged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_foto', models.ImageField(blank=True, null=True, upload_to='foto/fodals/%Y-%m-%d/', verbose_name='Media Fodals')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('regis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_fodals_changed', to='regpus.perubahanfaskes')),
            ],
        ),
        migrations.CreateModel(
            name='Fodals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_foto', models.ImageField(blank=True, null=True, upload_to='foto/fodals/%Y-%m-%d/', verbose_name='Media Fodals')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('regis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_fodals', to='regpus.regisfaskes')),
            ],
        ),
    ]
