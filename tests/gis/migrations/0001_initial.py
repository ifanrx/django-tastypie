# Generated by Django 2.2.1 on 2019-05-28 22:29

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import tastypie.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('updated', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('points', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
                ('lines', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('polys', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnnotatedGeoNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotations', models.TextField()),
                ('note', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotated', to='gis.GeoNote')),
            ],
        ),
    ]
