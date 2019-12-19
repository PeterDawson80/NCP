# Generated by Django 2.2.9 on 2019-12-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('category', models.CharField(choices=[('cat1', 'Category1'), ('cat2', 'Category2'), ('cat3', 'Category3'), ('cat4', 'Category4'), ('cat5', 'Category5')], max_length=20)),
                ('body', models.CharField(max_length=2000)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]