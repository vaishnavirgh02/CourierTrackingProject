# Generated by Django 2.2.2 on 2019-08-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0003_auto_20190812_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(choices=[('BGT', 'Balaghat (BGT)')], max_length=30)),
                ('office_pincode', models.IntegerField(choices=[(481001, 'Balaghat (BGT)')], max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Consignment',
        ),
    ]