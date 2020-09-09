# Generated by Django 3.1.1 on 2020-09-08 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_employee_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('total_leaves', models.PositiveSmallIntegerField(default=15)),
                ('leave_status', models.BooleanField(default=False)),
                ('employee_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employees')),
                ('manager_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='manager',
            name='emp_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='manager_name',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]