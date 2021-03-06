# Generated by Django 2.0.5 on 2018-05-14 11:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('email', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='images/clients/profiles')),
                ('website', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('github_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('ACTIVE', 'Active'), ('DISABLED', 'Disabled')], default='NEW', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FundingMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('token_id', models.CharField(help_text='This has to match the Exchange', max_length=4)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('amount_held', models.DecimalField(blank=True, decimal_places=18, default=0, max_digits=30)),
            ],
            options={
                'verbose_name': 'Funding Method',
                'verbose_name_plural': 'Funding Methods',
            },
        ),
        migrations.CreateModel(
            name='Fundings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=18, max_digits=30)),
                ('memo', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Funding',
                'verbose_name_plural': 'Fundings',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('blurb', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'New'), ('ACTIVE', 'Active'), ('DISABLED', 'Disabled')], default='NEW', max_length=10)),
                ('thumbnail', models.ImageField(blank=True, upload_to='images/projects')),
                ('featured', models.BooleanField(default=0)),
                ('reference', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Categories')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Client')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Categories')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=100)),
                ('reference', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('long_description', models.TextField(blank=True)),
                ('budget', models.DecimalField(decimal_places=18, default=0, max_digits=30)),
                ('funding', models.DecimalField(blank=True, decimal_places=18, default=0, max_digits=30)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.DO_NOTHING, to='projects.SubCategories'),
        ),
        migrations.AddField(
            model_name='fundings',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='fundings',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Tasks'),
        ),
        migrations.AddField(
            model_name='fundings',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.FundingMethods'),
        ),
    ]
