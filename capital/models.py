
from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.CharField(max_length=50, null=True)
    product_id = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0 ,null=True)
    quantity = models.IntegerField(null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    initial_quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.product} {self.price}"

    class Meta:
        db_table = 'ice'

class Purchase(models.Model):
    quantity_bought = models.IntegerField(default=0)
    amount = models.IntegerField()
    sold_by = models.CharField(max_length=50, null=True)
    bought_by = models.CharField(max_length=50, null=True)
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE) # stocks is the id renamed as stocks and also incharge of deleting all data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.stocks.product} -{self.amount}"




    class Meta:
        db_table = 'lemon'
class Returned(models.Model):
    product = models.CharField(max_length=50, null=True)
    returned_date = models.DateField()
    returned_product=models.CharField(max_length=50)
    returned_by = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.returned_product} -{self.returned_date}"
    class Meta:
        db_table = 'returned'
class Restock(models.Model):
    product = models.CharField(max_length=50, null=True)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} -{self.amount}"
    class Meta:
        db_table = 'restock'
