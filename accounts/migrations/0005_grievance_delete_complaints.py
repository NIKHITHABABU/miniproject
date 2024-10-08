# Generated by Django 5.0.8 on 2024-09-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('grievance_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='complaints',
        ),
    ]
