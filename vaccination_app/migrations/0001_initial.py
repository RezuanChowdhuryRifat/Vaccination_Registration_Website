# Generated by Django 3.2.6 on 2021-08-22 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('house_no', models.IntegerField(db_column='House_No')),
                ('upazilla_city_corporation', models.CharField(db_column='Upazilla_City_Corporation', max_length=50)),
                ('ward_no', models.IntegerField(db_column='Ward_No')),
                ('district', models.CharField(db_column='District', max_length=50)),
                ('unionn', models.CharField(blank=True, db_column='Unionn', max_length=50, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('center_id', models.IntegerField(db_column='Center_ID', primary_key=True, serialize=False)),
                ('center_name', models.CharField(db_column='Center_Name', max_length=300)),
            ],
            options={
                'db_table': 'center',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CenterAddress',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('house_no', models.IntegerField(db_column='House_No')),
                ('upazilla_city_corporation', models.CharField(db_column='Upazilla_City_Corporation', max_length=50)),
                ('ward_no', models.IntegerField(db_column='Ward_No')),
                ('district', models.CharField(db_column='District', max_length=50)),
                ('unionn', models.CharField(blank=True, db_column='Unionn', max_length=50, null=True)),
            ],
            options={
                'db_table': 'center_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nid',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, db_column='FName', max_length=100, null=True)),
                ('lname', models.CharField(blank=True, db_column='LName', max_length=100, null=True)),
                ('dob', models.DateField()),
                ('fathers_name', models.CharField(blank=True, db_column='Fathers_Name', max_length=150, null=True)),
                ('mothers_name', models.CharField(blank=True, db_column='Mothers_Name', max_length=150, null=True)),
            ],
            options={
                'db_table': 'nid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('nid', models.OneToOneField(db_column='NID_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('occupation', models.CharField(db_column='Occupation', max_length=200)),
                ('job_title', models.CharField(blank=True, db_column='Job_Title', max_length=100, null=True)),
            ],
            options={
                'db_table': 'citizen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GovernmentEmployee',
            fields=[
                ('nid', models.OneToOneField(db_column='NID_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('department', models.CharField(db_column='Department', max_length=150)),
                ('job_title', models.CharField(db_column='Job_Title', max_length=100)),
            ],
            options={
                'db_table': 'government_employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalPersonel',
            fields=[
                ('nid', models.OneToOneField(db_column='NID_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('medical_institution_name', models.CharField(db_column='Medical_Institution_Name', max_length=200)),
            ],
            options={
                'db_table': 'medical_personel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('nid', models.OneToOneField(db_column='NID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('date', models.DateTimeField(db_column='Date')),
                ('mobile_no', models.IntegerField(blank=True, db_column='Mobile_No', null=True)),
                ('age', models.IntegerField(db_column='Age')),
            ],
            options={
                'db_table': 'registration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nid', models.OneToOneField(db_column='NID_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('university_name', models.CharField(db_column='University_Name', max_length=200)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('nid', models.OneToOneField(db_column='NID_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vaccination_app.nid')),
                ('organization', models.CharField(db_column='Organization', max_length=150)),
                ('job_title', models.CharField(db_column='Job_Title', max_length=100)),
            ],
            options={
                'db_table': 'volunteering',
                'managed': False,
            },
        ),
    ]
