# Generated by Django 4.0.3 on 2022-03-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Eingereicht'), ('Accepted', 'Akzeptiert'), ('Denied', 'Abgelehnt'), ('On Hold', 'Im Wartezustand')], default='Submitted', max_length=128),
        ),
    ]
