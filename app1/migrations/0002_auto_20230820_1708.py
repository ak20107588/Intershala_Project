# Generated by Django 2.2 on 2023-08-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Image', models.ImageField(upload_to='Image')),
                ('Category', models.CharField(max_length=250)),
                ('Summary', models.CharField(max_length=1000)),
                ('Content', models.CharField(max_length=1000)),
                ('IsDraft', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='ProfilePicture',
            field=models.ImageField(upload_to='Image'),
        ),
    ]
