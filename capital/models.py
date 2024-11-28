from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.CharField(max_length=50, null=True)
    product_id = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(default=0 ,null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} {self.price}"

    class Meta:
        db_table = 'ice'

class Purchase(models.Model):

    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE) # stocks is the id renamed as stocks and also incharge of deleting all data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stocks.product} -{self.amount}"

    class Meta:
        db_table = 'lemon'
