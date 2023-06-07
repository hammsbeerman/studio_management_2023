# Generated by Django 3.2.12 on 2023-06-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_auto_20230607_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_NCR_compound',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_number',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_perf',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_print_mailmerge',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_print_side_1',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_print_side_2',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_send_mailmerge_to_press',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_send_to_press',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_set_to_number',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_set_to_perf',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_trim_to_size',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_wear_and_tear',
        ),
        migrations.RemoveField(
            model_name='kruegerjobdetail',
            name='step_white_compound',
        ),
        migrations.AlterField(
            model_name='kruegerjobdetail',
            name='number_price_to_number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price / Piece to Number'),
        ),
        migrations.AlterField(
            model_name='kruegerjobdetail',
            name='perf_price_per_piece',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price per Piece to Perf'),
        ),
        migrations.AlterField(
            model_name='kruegerjobdetail',
            name='price_per_m',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Paper Stock Price per M'),
        ),
    ]