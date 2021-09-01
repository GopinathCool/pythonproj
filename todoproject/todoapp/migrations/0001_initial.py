# Generated by Django 3.2.6 on 2021-08-31 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TodoListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todolist')),
            ],
        ),
    ]