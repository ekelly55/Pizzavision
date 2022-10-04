# Generated by Django 4.1.1 on 2022-10-04 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='main_app.pizza'),
        ),
        migrations.CreateModel(
            name='PizzaClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=150)),
                ('characters', models.ManyToManyField(to='main_app.character')),
            ],
        ),
    ]