from django.db import models


class Order(models.Model):
    oid = models.IntegerField("Order ID", unique=True)
    fname = models.CharField("First Name", max_length=20)
    lname = models.CharField("Last Name", max_length=20)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    mail = models.EmailField("Email ID")
    addr = models.CharField("Address", max_length=50)

    class Meta:
        ordering = ["oid"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"#{self.oid} {self.fname} {self.lname}"
