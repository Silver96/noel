# Generated by Django 2.1.7 on 2019-02-16 14:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='original', max_length=20)),
                ('status', models.CharField(blank=True, default='waiting to be processed', max_length=40, null=True)),
                ('ext', models.CharField(default='.jpg', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PictureCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('label', models.CharField(max_length=20)),
                ('original', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(regex='^.{64}$')])),
                ('status', models.CharField(max_length=50)),
                ('progress', models.IntegerField(default=0)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=300)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Session')),
            ],
        ),
        migrations.AddField(
            model_name='picturecluster',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Session'),
        ),
        migrations.AddField(
            model_name='picture',
            name='cluster',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.PictureCluster'),
        ),
        migrations.AddField(
            model_name='picture',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Session'),
        ),
    ]