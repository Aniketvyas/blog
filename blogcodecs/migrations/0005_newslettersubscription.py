# Generated by Django 3.2 on 2021-06-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcodecs', '0004_alter_blogs_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletterSubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('subscribedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
