# Generated by Django 4.1.3 on 2022-11-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(verbose_name='Дата и время начала рассылки')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('phone_code_filter', models.PositiveIntegerField(blank=True, verbose_name='Код мобильного оператора')),
                ('tag_filter', models.CharField(blank=True, max_length=50, verbose_name='Тeг')),
                ('end_datetaime', models.DateTimeField(verbose_name='Дата и время окончания рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]