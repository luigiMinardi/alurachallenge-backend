# Generated by Django 3.2.5 on 2021-07-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeflix_back', '0004_alter_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='descricao',
            field=models.CharField(error_messages={'max_length': 'O máximo de caracteres que uma descrição pode ter são 300!'}, help_text='Coloque a descrição do vídeo', max_length=300),
        ),
        migrations.AlterField(
            model_name='video',
            name='titulo',
            field=models.CharField(error_messages={'max_length': 'O máximo de caracteres que um titulo pode ter são 30!'}, help_text='Coloque o título do vídeo', max_length=30),
        ),
    ]
