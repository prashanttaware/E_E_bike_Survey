from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('session_key', models.CharField(max_length=32)),
                ('date',
                 models.DateTimeField(default=django.utils.timezone.now)),
                ('choice',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='answers',
                                   to='survey.Choice')),
            ],
        ),
    ]
