import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175)),
                ('image', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175)),
                ('description', models.TextField(max_length=275)),
                ('image', models.CharField(max_length=250)),
                ('borough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.borough')),
            ],
        ),
        migrations.CreateModel(
            name='Point_of_Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='SightSeeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(max_length=275)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('season', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=275)),
                ('description', models.TextField(max_length=375)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cuisine', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),

                ('image', models.CharField(max_length=350)),
                ('description', models.TextField(max_length=350)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=275)),
                ('type_of', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(max_length=275)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
        migrations.CreateModel(
            name='Art_Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', models.CharField(max_length=350)),
                ('description', models.TextField(max_length=350)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('type_of', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=350)),
                ('description', models.TextField(max_length=350)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest')),
            ],
        ),
    ]
