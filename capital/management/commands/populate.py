from django.core.management import BaseCommand

from capital.models import Stock


class Command(BaseCommand):
    def handle(self, *args, **options):
        whiskey = [{"product":"Coriander - Ground","product_id":3161,"initial_quantity":60,"quantity":60,"price":938,"date":"2024-08-22"},
{"product":"Paste - Black Olive","product_id":3606,"initial_quantity":78,"quantity":78,"price":281,"date":"2024-01-07"},
{"product":"Pork - Bacon, Double Smoked","product_id":1968,"initial_quantity":37,"quantity":37,"price":994,"date":"2024-08-08"},
{"product":"Okra","product_id":3097,"initial_quantity":68,"quantity":68,"price":794,"date":"2024-04-05"},
{"product":"Shrimp - 150 - 250","product_id":1130,"initial_quantity":56,"quantity":56,"price":874,"date":"2024-02-07"},
{"product":"Pork Casing","product_id":1883,"initial_quantity":94,"quantity":94,"price":472,"date":"2024-06-14"},
{"product":"Chinese Foods - Cantonese","product_id":4876,"initial_quantity":99,"quantity":99,"price":325,"date":"2024-01-16"},
{"product":"Vol Au Vents","product_id":2340,"initial_quantity":74,"quantity":74,"price":543,"date":"2024-01-10"},
{"product":"Egg - Salad Premix","product_id":2907,"initial_quantity":90,"quantity":90,"price":284,"date":"2024-03-09"},
{"product":"Pasta - Fettuccine, Egg, Fresh","product_id":4232,"initial_quantity":63,"quantity":63,"price":236,"date":"2023-12-13"},
{"product":"Lettuce - Boston Bib - Organic","product_id":4474,"initial_quantity":21,"quantity":21,"price":769,"date":"2024-10-30"},
{"product":"Flour - Buckwheat, Dark","product_id":2777,"initial_quantity":30,"quantity":30,"price":717,"date":"2024-11-29"},
{"product":"Juice - Apple, 341 Ml","product_id":1205,"initial_quantity":37,"quantity":37,"price":157,"date":"2024-01-09"},
{"product":"Sambuca - Ramazzotti","product_id":1596,"initial_quantity":97,"quantity":97,"price":594,"date":"2024-01-19"},
{"product":"Cranberries - Frozen","product_id":1999,"initial_quantity":92,"quantity":92,"price":302,"date":"2024-05-26"},
{"product":"Lambcasing","product_id":3493,"initial_quantity":19,"quantity":19,"price":506,"date":"2024-01-07"},
{"product":"Coffee - Hazelnut Cream","product_id":1389,"initial_quantity":88,"quantity":88,"price":156,"date":"2024-09-18"},
{"product":"Glass - Juice Clear 5oz 55005","product_id":3517,"initial_quantity":78,"quantity":78,"price":922,"date":"2024-10-16"},
{"product":"Truffle Paste","product_id":2523,"initial_quantity":60,"quantity":60,"price":456,"date":"2024-09-13"},
{"product":"Trueblue - Blueberry 12x473ml","product_id":3402,"initial_quantity":83,"quantity":83,"price":885,"date":"2024-01-18"},
{"product":"Flower - Commercial Bronze","product_id":2871,"initial_quantity":56,"quantity":56,"price":184,"date":"2024-10-16"},
{"product":"Energy Drink","product_id":3997,"initial_quantity":79,"quantity":79,"price":390,"date":"2024-09-04"},
{"product":"Scotch - Queen Anne","product_id":3365,"initial_quantity":24,"quantity":24,"price":601,"date":"2023-12-29"},
{"product":"Dill - Primerba, Paste","product_id":2889,"initial_quantity":62,"quantity":62,"price":214,"date":"2024-08-17"},
{"product":"Bread - Onion Focaccia","product_id":2533,"initial_quantity":98,"quantity":98,"price":694,"date":"2024-10-02"},
{"product":"Sugar - White Packet","product_id":2892,"initial_quantity":39,"quantity":39,"price":536,"date":"2024-09-15"},
{"product":"Pasta - Canelloni","product_id":3425,"initial_quantity":94,"quantity":94,"price":103,"date":"2024-04-05"},
{"product":"Beef - Chuck, Boneless","product_id":2539,"initial_quantity":54,"quantity":54,"price":778,"date":"2024-09-08"},
{"product":"Huck White Towels","product_id":2436,"initial_quantity":52,"quantity":52,"price":458,"date":"2024-01-11"},
{"product":"Cup - Translucent 7 Oz Clear","product_id":1248,"initial_quantity":66,"quantity":66,"price":336,"date":"2024-11-12"},
{"product":"Rice - Sushi","product_id":3531,"initial_quantity":34,"quantity":34,"price":539,"date":"2024-07-11"},
{"product":"Sea Bass - Whole","product_id":4067,"initial_quantity":66,"quantity":66,"price":152,"date":"2024-11-05"},
{"product":"Sugar - White Packet","product_id":1936,"initial_quantity":34,"quantity":34,"price":846,"date":"2024-09-24"},
{"product":"Raisin - Golden","product_id":2230,"initial_quantity":52,"quantity":52,"price":264,"date":"2024-05-12"},
{"product":"Foil Wrap","product_id":4541,"initial_quantity":63,"quantity":63,"price":627,"date":"2024-01-21"},
{"product":"Spice - Greek 1 Step","product_id":3002,"initial_quantity":33,"quantity":33,"price":936,"date":"2024-06-26"},
{"product":"Hersey Shakes","product_id":1981,"initial_quantity":24,"quantity":67,"price":67,"date":"2024-08-05"},
{"product":"Lotus Root","product_id":3082,"initial_quantity":25,"quantity":25,"price":809,"date":"2024-07-03"},
{"product":"Stainless Steel Cleaner Vision","product_id":1399,"initial_quantity":74,"quantity":74,"price":505,"date":"2024-08-13"},
{"product":"Island Oasis - Banana Daiquiri","product_id":2717,"initial_quantity":68,"quantity":68,"price":681,"date":"2024-09-13"},
{"product":"Oil - Olive Bertolli","product_id":3237,"initial_quantity":15,"quantity":15,"price":563,"date":"2024-03-21"},
{"product":"Vodka - Smirnoff","product_id":1327,"initial_quantity":28,"quantity":28,"price":337,"date":"2024-09-09"},
{"product":"Wine - Champagne Brut Veuve","product_id":4946,"initial_quantity":25,"quantity":25,"price":186,"date":"2024-10-17"},
{"product":"Tuna - Loin","product_id":3042,"initial_quantity":44,"quantity":44,"price":456,"date":"2024-06-26"}]
        for led in whiskey:
            stocks = Stock(**led)
            stocks.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated stocks'))


