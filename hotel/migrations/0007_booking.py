# Generated by Django 5.1.1 on 2024-09-30 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0006_alter_hotel_hotelid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "booking_status",
                    models.CharField(
                        choices=[
                            ("confirmed", "Confirmed"),
                            ("canceled", "Canceled"),
                            ("pending", "Pending"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="hotel.room",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="hotel.user",
                    ),
                ),
            ],
        ),
    ]
