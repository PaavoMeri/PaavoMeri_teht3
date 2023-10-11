from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('hallintasivusto', '0002_rename_laitteet_laitekategoria_alter_laite_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaiteKategoria',
            new_name='Kategoria',
        ),
        migrations.AlterModelOptions(
            name='kategoria',
            options={'verbose_name_plural': 'Kategoriat'},
        ),
        migrations.CreateModel(
            name='Kohde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Kohteet',
            },
        ),
        migrations.DeleteModel(
            name='Laite',
        ),
        migrations.AddField(
            model_name='kohde',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallintasivusto.kategoria'),
        ),
    ]
