# Generated by Django 3.2.5 on 2021-07-29 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('accepted', 'Accepted'), ('denied', 'Denied')], max_length=10, null=True)),
                ('master_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hired_master', to='services.masterservice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'quotations',
            },
        ),
    ]
