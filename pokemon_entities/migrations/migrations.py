from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0001_initial')
    ]

    operations = [
        migrations.CreteModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]