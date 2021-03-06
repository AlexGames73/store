# Generated by Django 2.0.7 on 2018-07-13 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('author', models.CharField(max_length=16)),
                ('date_created', models.DateTimeField()),
                ('text', models.TextField(max_length=1024)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('dislikes', models.IntegerField(blank=True, null=True)),
                ('reply_rating', models.IntegerField(blank=True, null=True)),
                ('reply', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('sale', models.BooleanField()),
                ('sale_price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('characteristics', models.TextField()),
                ('country', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.Comment')),
                ('advantages', models.TextField(blank=True, max_length=256, null=True)),
                ('disadvantages', models.TextField(blank=True, max_length=256, null=True)),
            ],
            bases=('store.comment',),
        ),
        migrations.AddField(
            model_name='comment',
            name='product_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]
