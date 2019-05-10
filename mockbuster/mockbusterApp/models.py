from django.db import models

# Create your models here.
from django.urls import reverse
import datetime

class Mockbuster(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mockbuster_edit', kwargs={'pk': self.pk})


class Branch(models.Model):
    br_id = models.AutoField(db_column='BR_ID', primary_key=True)  # Field name made lowercase.
    br_address = models.CharField(db_column='BR_ADDRESS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    br_phone_num = models.CharField(db_column='BR_PHONE_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ma = models.ForeignKey('Manager', models.DO_NOTHING, db_column='MA_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class Customer(models.Model):
    cu_id = models.AutoField(db_column='CU_ID', primary_key=True)  # Field name made lowercase.
    cu_first_name = models.CharField(db_column='CU_FIRST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cu_last_name = models.CharField(db_column='CU_LAST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cu_phone_num = models.CharField(db_column='CU_PHONE_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cu_address = models.CharField(db_column='CU_ADDRESS', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'
		

class Employee(models.Model):
    em_id = models.AutoField(db_column='EM_ID', primary_key=True)  # Field name made lowercase.
    em_first_name = models.CharField(db_column='EM_FIRST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_last_name = models.CharField(db_column='EM_LAST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_pay_rate = models.DecimalField(db_column='EM_PAY_RATE', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    em_phone_num = models.CharField(db_column='EM_PHONE_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_dob = models.DateField(db_column='EM_DOB', blank=True, null=True)  # Field name made lowercase.
    em_ss_num = models.CharField(db_column='EM_SS_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_address = models.CharField(db_column='EM_ADDRESS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class PurchaseHist(models.Model):
    ph_id = models.AutoField(db_column='PH_ID', primary_key=True)  # Field name made lowercase.
    ph_date = models.DateField(db_column='PH_DATE', blank=True, null=True)  # Field name made lowercase.
    vg = models.ForeignKey('VideoGame', models.DO_NOTHING, db_column='VG_ID')  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.
    num_purchased = models.IntegerField(db_column='NUM_PURCHASED', blank=True, null=True)  # Field name made lowercase.
    ind_cost = models.DecimalField(db_column='IND_COST', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ve = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='VE_ID')  # Field name made lowercase.
    ma = models.ForeignKey('Manager', models.DO_NOTHING, db_column='MA_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase_hist'



class Manager(models.Model):
    ma_id = models.AutoField(db_column='MA_ID', primary_key=True)  # Field name made lowercase.
    em = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EM_ID')  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Rental(models.Model):
    re_id = models.AutoField(db_column='RE_ID', primary_key=True)  # Field name made lowercase.
    re_date = models.DateField(db_column='RE_DATE',auto_now_add=True)  # Field name made lowercase.
    vg = models.ForeignKey('VideoGame', models.DO_NOTHING, db_column='VG_ID')  # Field name made lowercase.
    em = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EM_ID')  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.
    cu = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CU_ID')  # Field name made lowercase.
    due_date = models.DateField(db_column='DUE_DATE',default=(datetime.date.today()+datetime.timedelta(days=5)))  # Field name made lowercase.
	
	
    class Meta:
        managed = False
        db_table = 'rental'


class RentalHist(models.Model):
    rh_id = models.AutoField(db_column='RH_ID', primary_key=True)  # Field name made lowercase.
    rh_date = models.DateField(db_column='RH_DATE', blank=True, null=True)  # Field name made lowercase.
    vg = models.ForeignKey('VideoGame', models.DO_NOTHING, db_column='VG_ID')  # Field name made lowercase.
    cu = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CU_ID')  # Field name made lowercase.
    em = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EM_ID')  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rental_hist'


class Vendor(models.Model):
    ve_id = models.AutoField(db_column='VE_ID', primary_key=True)  # Field name made lowercase.
    ve_name = models.CharField(db_column='VE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ve_phone_num = models.CharField(db_column='VE_PHONE_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ve_address = models.CharField(db_column='VE_ADDRESS', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendor'


class VideoGame(models.Model):
    vg_id = models.AutoField(db_column='VG_ID', primary_key=True)  # Field name made lowercase.
    vd = models.ForeignKey('VideoDetail', models.DO_NOTHING, db_column='VD_ID')  # Field name made lowercase.  # Field name made lowercase.
    vg_copies_owned = models.IntegerField(db_column='VG_COPIES_OWNED', blank=True, null=True)  # Field name made lowercase.
    vg_copies_rented = models.IntegerField(db_column='VG_COPIES_RENTED', blank=True, null=True)  # Field name made lowercase.
    br = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video_game'

class VideoDetail(models.Model):
    vd_id = models.AutoField(db_column='VD_ID', primary_key=True)  # Field name made lowercase.
    vd_name = models.CharField(db_column='VD_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    vd_genre = models.CharField(db_column='VD_GENRE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vd_publisher = models.CharField(db_column='VD_PUBLISHER', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video_detail'


