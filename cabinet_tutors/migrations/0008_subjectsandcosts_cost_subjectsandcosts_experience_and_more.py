# Generated by Django 4.1.4 on 2023-01-09 19:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet_parents", "0011_alter_survey_student_area_alter_survey_tutor_area"),
        ("cabinet_tutors", "0007_tutorcabinets_rename_language_languages_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjectsandcosts",
            name="cost",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(499000),
                ],
                verbose_name="Cтоимость тг./час",
            ),
        ),
        migrations.AddField(
            model_name="subjectsandcosts",
            name="experience",
            field=models.DecimalField(
                decimal_places=1,
                default=0.0,
                max_digits=3,
                verbose_name="Опыт преподавания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subjectsandcosts",
            name="subject",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutors",
                to="cabinet_parents.subject",
                verbose_name="Предметы",
            ),
            preserve_default=False,
        ),
    ]
