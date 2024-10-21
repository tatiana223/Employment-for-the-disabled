# Generated by Django 4.2.7 on 2024-10-19 23:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id_response', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Действующая'), (2, 'Удалена')], default=1)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('formed_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_requests', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderated_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'responses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id_vacancies', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('money_from', models.IntegerField(default=0)),
                ('money_to', models.IntegerField(default=0)),
                ('image', models.TextField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(default='Неизвестно', max_length=255)),
                ('name_company', models.CharField(default='Default company name', max_length=255)),
                ('peculiarities', models.TextField(default='Default company name')),
            ],
            options={
                'db_table': 'vacancies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResponsesVacancies',
            fields=[
                ('mm_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.IntegerField(default=1)),
                ('is_main', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.responses')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vacancies')),
            ],
            options={
                'db_table': 'responses_vacancies',
                'managed': True,
                'unique_together': {('request', 'vacancy')},
            },
        ),
    ]
