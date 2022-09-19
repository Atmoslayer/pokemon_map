from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]