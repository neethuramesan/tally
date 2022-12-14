# Generated by Django 4.0.5 on 2022-08-01 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gst_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=225)),
                ('reg_type', models.CharField(max_length=225)),
                ('assessee', models.CharField(max_length=225)),
                ('app_form', models.CharField(max_length=225)),
                ('gstin', models.CharField(max_length=225)),
                ('gstr1', models.CharField(max_length=225)),
                ('rate_details', models.CharField(max_length=225)),
                ('advance_receipts', models.CharField(max_length=225)),
                ('reverse_charge', models.CharField(max_length=225)),
                ('classifications', models.CharField(max_length=225)),
                ('bond_details', models.CharField(max_length=225)),
                ('eway_bill', models.CharField(max_length=225)),
                ('applicable_form', models.CharField(max_length=225)),
                ('threshold_includes', models.CharField(max_length=225)),
                ('threshold_limit1', models.CharField(max_length=225)),
                ('intrastate', models.CharField(max_length=225)),
                ('threshold_limit2', models.CharField(max_length=225)),
                ('print_eway', models.CharField(max_length=225)),
                ('e_invoice', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
    ]
