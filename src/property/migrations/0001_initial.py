# Generated by Django 2.2.4 on 2019-11-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_address', models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Farm', 'Farm'), ('Other', 'Other')], max_length=9, verbose_name='Type of address')),
                ('BRZipCode', models.CharField(max_length=8, verbose_name='Brazilian ZIP code')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('district', models.CharField(max_length=100, verbose_name='District')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address complement')),
                ('reference_point', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reference point')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]
