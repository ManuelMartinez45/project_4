from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accomodation',
            new_name='Accommodation',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='point_of_interest',
        ),
        migrations.RemoveField(
            model_name='art_culture',
            name='point_of_interest',
        ),
        migrations.RemoveField(
            model_name='entertainment',
            name='point_of_interest',
        ),
        migrations.RemoveField(
            model_name='food',
            name='point_of_interest',
        ),
        migrations.RemoveField(
            model_name='nature',
            name='point_of_interest',
        ),
        migrations.RemoveField(
            model_name='sightseeing',
            name='point_of_interest',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='neighborhood',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='art_culture',
            name='neighborhood',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entertainment',
            name='neighborhood',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
        ),
        migrations.AddField(
            model_name='nature',
            name='neighborhood',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sightseeing',
            name='name',
            field=models.CharField(default=1, max_length=275),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sightseeing',
            name='neighborhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.neighborhood'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Point_of_Interest',
        ),
    ]
