# Generated by Django 4.0.4 on 2022-05-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_photographer_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=1234)),
                ('name', models.CharField(default='Alumni Event', max_length=30)),
                ('Location', models.CharField(default='Nairobi,Kenya', max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('status', models.BooleanField()),
                ('noOfPhotos', models.IntegerField(default=5)),
            ],
        ),
    ]