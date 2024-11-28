from django.http import HttpResponse
from django.shortcuts import render, redirect

from capital.models import Stock, Purchase


# Create your views here.
def test(request):
    # stock1 = Stock(product= 'cake',product_id='1700',quantity='40',price='300',date='2023-04-04')
    # stock1.save()
    # stock2 = Stock(product='bacon', product_id='1300', quantity='50', price='350', date='2023-03-04')
    # stock2.save()
    stock_count = Stock.objects.count()
    stock1 = Stock.objects.get(id=1)
    print(stock1)

    purchase1 = Purchase(amount=1000,stocks=stock1,status=True)
    purchase1.save()

    purchase_count= Purchase.objects.count()


    return HttpResponse(f"the no of stocks is{stock_count} and number of purchases is {purchase_count}")



def view_stock(request):
        data = Stock.objects.all()
        return render(request, "view_stock.html", context={"whiskey": data})


def delete_product(request, stocks_id):
    stocks = Stock.objects.get(id=stocks_id)
    stocks.delete()
    return redirect('view_stock')


def home(request):
        # No data needed for the home page (optional)
        context = {}
        return render(request, 'home.html', context)
