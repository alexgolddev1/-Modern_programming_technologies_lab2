from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("oid", models.IntegerField(unique=True, verbose_name="Order ID")),
                ("fname", models.CharField(max_length=20, verbose_name="First Name")),
                ("lname", models.CharField(max_length=20, verbose_name="Last Name")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Price")),
                ("mail", models.EmailField(max_length=254, verbose_name="Email ID")),
                ("addr", models.CharField(max_length=50, verbose_name="Address")),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
                "ordering": ["oid"],
            },
        ),
    ]
