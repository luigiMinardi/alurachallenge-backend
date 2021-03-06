# Generated by Django 3.2.5 on 2021-07-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Coloque o título do vídeo', max_length=30)),
                ('descricao', models.CharField(help_text='Coloque a descrição do vídeo', max_length=300)),
                ('url', models.URLField(help_text='Coloque o link para o vídeo')),
            ],
        ),
    ]
