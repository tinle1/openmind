# Generated by Django 2.0.7 on 2019-03-11 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.TextField()),
                ('tags', models.TextField(blank=True, default='')),
                ('desc', models.TextField()),
                ('cover_photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'author',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('book_title', models.CharField(max_length=200)),
                ('tags', models.TextField()),
                ('content', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('image_file', models.TextField()),
                ('audio_file', models.TextField()),
                ('video_file', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
            ],
            options={
                'db_table': 'book',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
            options={
                'db_table': 'book_category',
            },
        ),
        migrations.CreateModel(
            name='BookSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_title', models.TextField()),
                ('tags', models.TextField(blank=True, default='')),
                ('desc', models.TextField(blank=True, default='')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'book_set',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.TextField()),
                ('tags', models.TextField(blank=True, default='')),
                ('desc', models.TextField(blank=True, default='')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_title', models.TextField()),
                ('tags', models.TextField(blank=True, default='')),
                ('desc', models.TextField(blank=True, default='')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'collection',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('event_name', models.CharField(max_length=200)),
                ('tags', models.TextField()),
                ('content', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('address', models.TextField()),
                ('image_file', models.TextField()),
                ('audio_file', models.TextField()),
                ('video_file', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
            options={
                'db_table': 'event',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('audio', 'Audio'), ('video', 'Video')], max_length=20)),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'media_file',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.TextField()),
                ('desc', models.TextField()),
                ('cover_photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'publisher',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('quote_title', models.CharField(max_length=200)),
                ('tags', models.TextField()),
                ('content', models.TextField()),
                ('image_file', models.TextField()),
                ('audio_file', models.TextField()),
                ('video_file', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('book_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher')),
            ],
            options={
                'db_table': 'quotes',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.TextField()),
                ('thumbnail_photo', models.TextField()),
                ('story_title', models.CharField(max_length=200)),
                ('tags', models.TextField()),
                ('content', models.TextField()),
                ('image_file', models.TextField()),
                ('audio_file', models.TextField()),
                ('video_file', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
                ('book_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher')),
            ],
            options={
                'db_table': 'story',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='YearPublished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('tags', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'year',
            },
        ),
        migrations.AddField(
            model_name='story',
            name='year_published',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.YearPublished'),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='year_published',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.YearPublished'),
        ),
    ]
