# Generated by Django 4.0.5 on 2022-08-22 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0010_alter_tds_details_tan_alter_tds_details_tan_regno'),
    ]

    operations = [
        migrations.CreateModel(
            name='GST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=225)),
                ('reg_type', models.CharField(max_length=225)),
                ('assessee', models.CharField(max_length=225)),
                ('gst_applicable', models.CharField(max_length=225)),
                ('gstin', models.CharField(max_length=225)),
                ('periodicity', models.CharField(max_length=225)),
                ('gst_rate_details', models.CharField(max_length=225)),
                ('advance_receipts', models.CharField(max_length=225)),
                ('reverse_charge', models.CharField(max_length=225)),
                ('gst_classification', models.CharField(max_length=225)),
                ('bond_details', models.CharField(max_length=225)),
                ('eway_bill', models.CharField(max_length=225)),
                ('applicable_form', models.CharField(max_length=225)),
                ('threshold_includes', models.CharField(max_length=225)),
                ('threshold_limit', models.CharField(max_length=225)),
                ('intrastate', models.CharField(max_length=225)),
                ('threshold_limit2', models.CharField(max_length=225)),
                ('print_eway', models.CharField(max_length=225)),
                ('e_invoice', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='tds_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('son_daughter', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('pan', models.CharField(max_length=255)),
                ('flat_no', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('std', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='company',
        ),
        migrations.RenameField(
            model_name='tds_details',
            old_name='activate_tds',
            new_name='active_tds',
        ),
        migrations.RenameField(
            model_name='tds_details',
            old_name='excemption_limit',
            new_name='ignore_it',
        ),
        migrations.RemoveField(
            model_name='features',
            name='payroll_statutory',
        ),
        migrations.DeleteModel(
            name='Gst_Details',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]