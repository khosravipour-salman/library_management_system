# Generated by Django 4.0.4 on 2022-06-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='author',
            field=models.ManyToManyField(to='author.authormodel'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='book_cover'),
        ),
    ]
