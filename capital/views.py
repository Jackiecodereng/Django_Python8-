from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from capital.app_forms import StockForm, PurchaseForm, LoginForm
from capital.models import Stock, Purchase
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def test(request):
    # stock1 = Stock(product= 'cake',product_id='1700',quantity='40',price='300',date='2023-04-04')
    # stock1.save()
    # stock2 = Stock(product='bacon', product_id='1300', quantity='50', price='350', date='2023-03-04')
    # stock2.save()
    stock_count = Stock.objects.count()
    stock1 = Stock.objects.get(id=1)
    print(stock1)

    purchase1 = Purchase(amount=1000, stocks=stock1, status=True)
    purchase1.save()

    purchase_count = Purchase.objects.count()

    return HttpResponse(f"the no of stocks is{stock_count} and number of purchases is {purchase_count}")


def view_stock(request):
    data = Stock.objects.all()
    paginator = Paginator(data, 10)  # this one separets the data in pages
    page_number = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page_number)
    except PageNotAnInteger | EmptyPage:
        paginated_data = paginator.page(1)

    return render(request, "view_stock.html", context={"whiskey": paginated_data})


def delete_product(request, stocks_id):
    stocks = Stock.objects.get(id=stocks_id)
    stocks.delete()
    messages.warning(request, f'The product  {stocks.product} was deleted from the database')

    return redirect('view_stock')


def home(request):
    # No data needed for the home page (optional)
    context = {}
    return render(request, 'home.html', context)


def add_stock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)

            # Set initial_quantity to the value of quantity
            stock.initial_quantity = stock.quantity

            # Save the instance to the database
            stock.save()
            messages.success(request, f'You have successfully added   {form.cleaned_data['product']} to the database')

            return redirect('view_stock')

    else:
        form = StockForm()

    return render(request, 'add_stock.html', context={"form": form})


def issue(request, stocks_id):
    stocks = get_object_or_404(Stock, id=stocks_id)
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            quantity_bought = form.cleaned_data['quantity_bought']
            bought_by = form.cleaned_data['bought_by']
            sold_by = form.cleaned_data['sold_by']
            stocks.quantity = stocks.quantity - int(quantity_bought)
            stocks.save()
            amount = stocks.price * int(quantity_bought)
            lime = Purchase(quantity_bought=quantity_bought, stocks=stocks, amount=amount, bought_by=bought_by,
                            sold_by=sold_by)
            lime.save()
            messages.success(request,
                             f'You have successfully bought  {quantity_bought}  {stocks.product} and the total amount is {amount}.')

            return redirect('view_stock')
    else:
        form = PurchaseForm()
    return render(request, template_name='issue.html', context={"form": form, "stocks": stocks}, )


def history(request):
    stock_data = Stock.objects.all()  # Fetch all stock data
    purchase_data = Purchase.objects.select_related('stocks')  # Fetch all purchase data with related stocks
    # Pass the data to the template
    return render(request, 'issue_history.html', {
        'stock_data': stock_data,
        'purchase_data': purchase_data,
    })


def login_user(request):
    if request.method == "GET":
        form = LoginForm
        return render(request, 'login_form.html', {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  # sessions,cookies
                return redirect('home')
            messages.error(request, 'Invalid username or password.')
            return render(request, template_name="login_form.html", context={"form": form})


def signout_user(request):
    logout(request)
    return redirect('login')


def delete_purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    purchase.delete()

    messages.success(request, 'Purchase deleted successfully!')

    return redirect('history')


def search_product(request):
    query = request.GET.get('search', '')
    data = Stock.objects.all()

    if query:
        data = data.filter(product__icontains=query)  # Searching based on the 'product' field

    paginator = Paginator(data, 10)  # Paginate the data, 10 stocks per page
    page_number = request.GET.get('page', 1)

    try:
        paginated_data = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        paginated_data = paginator.page(1)
    return render(request, "search.html", context={"whiskey": paginated_data,"query": query})
