from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('survey', '0001_initial')]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='choices',
                to='survey.Question',
            ),
        )
    ]
