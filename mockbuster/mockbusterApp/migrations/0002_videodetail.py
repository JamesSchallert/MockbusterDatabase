# Generated by Django 2.2 on 2019-05-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockbusterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('vd_id', models.AutoField(db_column='VG_ID', primary_key=True, serialize=False)),
                ('vd_name', models.CharField(blank=True, db_column='VG_NAME', max_length=40, null=True)),
                ('vd_genre', models.CharField(blank=True, db_column='VG_GENRE', max_length=20, null=True)),
                ('vd_publisher', models.CharField(blank=True, db_column='VG_PUBLISHER', max_length=40, null=True)),
            ],
            options={
                'db_table': 'video_detail',
                'managed': False,
            },
        ),
    ]
