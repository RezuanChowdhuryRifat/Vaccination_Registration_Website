from django.db import models


class Address(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    street_address = models.CharField(db_column='Street_Address', max_length=300)  # Field name made lowercase.
    upazilla_city_corporation = models.CharField(db_column='Upazilla_City_Corporation', max_length=50)  # Field name made lowercase.
    ward_no = models.IntegerField(db_column='Ward_No')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    unionn = models.CharField(db_column='Unionn', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Center(models.Model):
    center_id = models.IntegerField(db_column='Center_ID', primary_key=True)  # Field name made lowercase.
    center_name = models.CharField(db_column='Center_Name', max_length=300)  # Field name made lowercase.
    center_address = models.ForeignKey('CenterAddress', models.DO_NOTHING, db_column='Center_Address_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'center'


class CenterAddress(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    street_address = models.CharField(db_column='Street_Address', max_length=300)  # Field name made lowercase.
    upazilla_city_corporation = models.CharField(db_column='Upazilla_City_Corporation', max_length=50)  # Field name made lowercase.
    ward_no = models.IntegerField(db_column='Ward_No')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    unionn = models.CharField(db_column='Unionn', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'center_address'


class Citizen(models.Model):
    nid = models.OneToOneField('Nid', models.DO_NOTHING, db_column='NID_ID', primary_key=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=200)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citizen'


class GovernmentEmployee(models.Model):
    nid = models.OneToOneField('Nid', models.DO_NOTHING, db_column='NID_ID', primary_key=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=150)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'government_employee'


class MedicalPersonel(models.Model):
    nid = models.OneToOneField('Nid', models.DO_NOTHING, db_column='NID_ID', primary_key=True)  # Field name made lowercase.
    medical_institution_name = models.CharField(db_column='Medical_Institution_Name', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medical_personel'


class Nid(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fname = models.CharField(db_column='FName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField()
    fathers_name = models.CharField(db_column='Fathers_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    mothers_name = models.CharField(db_column='Mothers_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='Address_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nid'


class Otp(models.Model):
    otpkey = models.IntegerField(blank=True, null=True)     

    class Meta:
        managed = False
        db_table = 'otp'

class Categorylist(models.Model):
    list = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorylist'


class Registration(models.Model):
    nid = models.OneToOneField(Nid, models.DO_NOTHING, db_column='NID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    center = models.ForeignKey(Center, models.DO_NOTHING, db_column='Center_ID', blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.BigIntegerField(db_column='Mobile_no', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registration'
        unique_together = (('mobile_no', 'center'),)


class Student(models.Model):
    nid = models.OneToOneField(Nid, models.DO_NOTHING, db_column='NID_ID', primary_key=True)  # Field name made lowercase.
    university_name = models.CharField(db_column='University_Name', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Volunteering(models.Model):
    nid = models.OneToOneField(Nid, models.DO_NOTHING, db_column='NID_ID', primary_key=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=150)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volunteering'