# Generated by Django 5.0.3 on 2024-04-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("voiceData", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="soundfeature",
            name="avg_pitch",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="chroma_stft_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="chroma_stft_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="max_note",
            field=models.CharField(default="", max_length=5),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="max_pitch",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="min_note",
            field=models.CharField(default="", max_length=5),
        ),
        migrations.AddField(
            model_name="soundfeature",
            name="min_pitch",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="harmony_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="harmony_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc0_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc0_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc10_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc10_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc11_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc11_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc12_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc12_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc13_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc13_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc14_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc14_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc15_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc15_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc16_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc16_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc17_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc17_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc18_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc18_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc19_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc19_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc1_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc1_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc2_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc2_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc3_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc3_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc4_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc4_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc5_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc5_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc6_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc6_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc7_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc7_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc8_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc8_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc9_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="mfcc9_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="perceptr_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="perceptr_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="rolloff_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="rolloff_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="spectral_bandwidth_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="spectral_bandwidth_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="spectral_centroid_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="spectral_centroid_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="tempo",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="zero_crossing_rate_mean",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soundfeature",
            name="zero_crossing_rate_var",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterModelTable(
            name="soundfeature",
            table="sound_features",
        ),
    ]
