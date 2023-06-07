# Generated by Django 3.2.12 on 2023-06-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_kruegerjobdetail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='fold_number_to_fold',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Pieces to Fold'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='fold_price_per_fold',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price / Fold'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='mailmerge_price_per_piece',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Mailmerge Price/Piece'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='mailmerge_qty',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Mailmerge Qty'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='material_cost',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Material Cost'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='material_markup',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Material Markup Percent'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='material_markup_percentage',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Material Markup Percent'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='number_number_of_pieces',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Pieces to Number'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='number_price_to_number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price / Piece'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='perf_number_of_pieces',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Pieces to Perf'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='perf_price_per_piece',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price per Piece'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='price_total',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Total Price'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='price_total_per_m',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Price / M'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='staple_number_of_pieces',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Number of pieces'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='staple_price_per_staple',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price per staple'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='staple_staples_per_piece',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Staples per piece'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_NCR_compound',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='NCR Compound'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_NCR_compound_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='NCR Compound'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_bulk_mail_tray_sort_paperwork',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Prepare Bulk Mailing'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_bulk_mail_tray_sort_paperwork_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Prepare Bulk Mailing'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_count_package',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Count / Package'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_count_package_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Count / Package'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_delivery',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Delivery'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_delivery_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Delivery'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_fold',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Fold'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_fold_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Fold'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_id_count',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='ID / Count'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_id_count_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='ID / Count'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_chip_divider',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Chip Divider'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_chip_divider_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Chip Divider'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_frontback_cover',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Front / Back Cover'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_frontback_cover_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Front / Back Cover'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_wrap_around',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Wrap Around'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_insert_wrap_around_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Insert Wrap Around'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Number'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_number_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Number'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_packing_slip',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Packing Slip'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_packing_slip_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Packing Slip'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_perf',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Perf'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_perf_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Perf'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_cost_side_1',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Side 1 Price / Click'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_cost_side_1_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Print Cost Side 1'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_cost_side_2',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Side 2 Price / Click'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_cost_side_2_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Printing Cost Side 1'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_mailmerge',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Print Mailmerge'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_mailmerge_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Mailmerge'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_side_1',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Print Side 1'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_print_side_2',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Print Side 2'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_reclaim_artwork',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Reclaim Artwork'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_reclaim_artwork_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Reclaim Artwork'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_send_mailmerge_to_press',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Send Mailmerge to press'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_send_mailmerge_to_press_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Send Mailmerge to press'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_send_to_press',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Send to Press'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_send_to_press_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Send to Press'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_folder',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set Folder'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_folder_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set Folder'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_drill',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Drill'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_drill_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Drill'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Number'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_number_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Number'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_perf',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Perf'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_perf_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Perf'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_staple',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Staple'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_set_to_staple_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Set to Staple'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_staple',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Staple'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_staple_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Staple'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_tab_for_mailing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Tab for Mailing'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_tab_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Tab for Mailing'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_trim_to_size',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Trim to Size'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_trim_to_size_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Trim to Size'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_wear_and_tear',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Wear and Tear'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_wear_and_tear_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Wear and Tear'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_white_compound',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='White Compound'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_white_compound_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='White Compound'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_workorder',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Create Workorder'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='step_workorder_price',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Create Workorder'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='tabs_number_of_pieces',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Number of Pieces'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='tabs_per_piece',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Tabs / Piece'),
        ),
        migrations.AddField(
            model_name='kruegerjobdetail',
            name='taps_price_per_tab',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Price / Tab'),
        ),
    ]