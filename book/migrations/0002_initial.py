# Generated by Django 4.0.4 on 2022-05-26 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extra', '0001_initial'),
        ('accounting', '0002_initial'),
        ('loan', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='category',
            field=models.ManyToManyField(to='extra.categorymodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='loan.loanmodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='extra.publishermodel'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='accounting.customusermodel'),
        ),
        migrations.AddField(
            model_name='bookmarkmodel',
            name='book',
            field=models.ManyToManyField(to='book.bookmodel'),
        ),
        migrations.AddField(
            model_name='bookmarkmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounting.customusermodel'),
        ),
    ]