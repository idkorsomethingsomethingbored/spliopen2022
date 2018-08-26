# Generated by Django 2.0.5 on 2018-07-23 02:10

from django.db import migrations, models
import django.db.models.deletion


def populate_roundmotions(apps, schema_editor):
    Motion = apps.get_model("motions", "Motion")
    RoundMotions = apps.get_model("motions", "RoundMotions")

    for mm in Motion.objects.all():
        RoundMotions(round=mm.round, motion=mm, seq=mm.seq).save()


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_remove_tournament_welcome_msg'),
        ('motions', '0003_auto_20180402_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoundMotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=1, help_text='The order in which motions are displayed', verbose_name='sequence number')),
            ],
            options={
                'verbose_name': 'round motion',
                'verbose_name_plural': 'round motions',
                'ordering': ('motion', 'seq'),
            },
        ),
        migrations.AddField(
            model_name='motion',
            name='rounds',
            field=models.ManyToManyField(through='motions.RoundMotions', to='tournaments.Round', verbose_name='rounds'),
        ),
        migrations.AlterModelOptions(
            name='motion',
            options={'verbose_name': 'motion', 'verbose_name_plural': 'motions'},
        ),
        migrations.AddField(
            model_name='roundmotions',
            name='motion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.Motion', verbose_name='motion'),
        ),
        migrations.AddField(
            model_name='roundmotions',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round', verbose_name='round'),
        ),
        migrations.AlterUniqueTogether(
            name='roundmotions',
            unique_together={('round', 'seq')},
        ),
        migrations.RunPython(populate_roundmotions),
        migrations.RemoveField(
            model_name='motion',
            name='round',
        ),
        migrations.RemoveField(
            model_name='motion',
            name='seq',
        ),
    ]
