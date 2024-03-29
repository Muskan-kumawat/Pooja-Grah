# Generated by Django 3.2.6 on 2022-04-24 16:43

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220419_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pandit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imageUrl', models.URLField(max_length=500, verbose_name='Pandit Img Url')),
                ('nameOfPandit', models.CharField(max_length=50)),
                ('experience', models.IntegerField(default=0, validators=[main.models.minMax])),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='bookingDoneAt',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puja',
            name='panditName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='puja',
            name='price',
            field=models.IntegerField(default=0, validators=[main.models.minMax2]),
        ),
    ]
