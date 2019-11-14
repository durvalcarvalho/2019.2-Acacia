<<<<<<< HEAD
# Generated by Django 2.2.4 on 2019-11-14 19:33
=======
# Generated by Django 2.2.4 on 2019-11-14 17:09
>>>>>>> d7328e8fa09ee59ade16b75966c0c00a328d2203

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_type', models.CharField(choices=[('Avocado', 'Avocado'), ('Pineapple', 'Pineapple'), ('Banana', 'Banana'), ('Persimmon', 'Persimmon'), ('Coconut', 'Coconut'), ('FIG', 'FIG'), ('Guava', 'Guava'), ('Jabuticaba', 'Jabuticaba'), ('Orange', 'Orange'), ('Lemon', 'Lemon'), ('Apple', 'Apple'), ('Papaya', 'Papaya'), ('Mango', 'Mango'), ('Passion Fruit', 'Passion Fruit'), ('Quince', 'Quince'), ('Nectarine', 'Nectarine'), ('Loquat', 'Loquat'), ('Pear', 'Pear'), ('Pequizeiro', 'Pequizeiro'), ('Tangerine', 'Tangerine'), ('Peach', 'Peach'), ('Vine', 'Vine')], max_length=13, verbose_name='Tree of type')),
                ('number_of_tree', models.IntegerField(verbose_name='Number of tree')),
                ('tree_height', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Average tree height')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/trees')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to='property.Property', verbose_name='Property trees')),
            ],
            options={
                'unique_together': {('property', 'tree_type')},
            },
        ),
        migrations.CreateModel(
            name='HarvestMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=9, verbose_name='Harvest month')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvest_months', to='tree.Tree')),
            ],
            options={
                'verbose_name_plural': 'Harvest Months',
                'unique_together': {('tree', 'harvest_month')},
            },
        ),
    ]
