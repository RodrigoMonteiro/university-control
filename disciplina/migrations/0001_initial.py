# Generated by Django 4.2.6 on 2023-11-07 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('carga_horaria', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curso.curso')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='professor.professor')),
            ],
        ),
    ]
