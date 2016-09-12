from django.db.models import Count, Sum, Max

from sakila.models import *


def assignment_1():
    """
    How many Films do we have in the DVD store?
    """
    return Film.objects.count()


def assignment_2():
    """
    How many Films are rented at the moment?
    """
    pass
    # Rental.objects.values('return_date').annotate(Count('rental_id'))
    # Rental.objects.filter(return_date=None).count()
    # test = Rental.objects.filter(
    # return Rental.objects.filter(return_date__lt = )
    # return Rental.objects.filter(return_date__gt=).count()


def assignment_3():
    """
    List the full name of all Staff members that live in Canada
    """
    #print(Country.objects.get(country="Canada").country_id)
    staff_country = Staff.objects.filter(address__city__country=Country.objects.get(country="Canada").country_id)
    names = []
    for i in staff_country:
        names.append(i.first_name + " " + i.last_name)
    return names

def assignment_4():
    """
    Who is the customer that has rented more Films?
    """
    q=Rental.objects.values('customer').annotate(Count('inventory'))
    customer_name = Customer.objects.get(customer_id=q.filter(inventory__count = q.aggregate(Max("inventory__count"))['inventory__count__max'])[0]['customer'])
    return customer_name.first_name + " " + customer_name.last_name


def assignment_5():
    """
    Which is the most popular FilmCategory?
    """
    # For each category, add how many movies there are
    list_of_cat_counts = FilmCategory.objects.values('category').annotate(Count('film'))
    current_max = 0
    category_number = 0
    for elem in list_of_cat_counts:
        if elem['film__count'] > current_max:
            current_max = elem['film__count']
            category_number = elem['category']
    # After this, we'll have the amount of films in the max cat and also the cat number, which we need to translate to an actual name
    cat_name_query = Category.objects.get(category_id=category_number)
    return cat_name_query.name
            


def assignment_6():
    """
    How much has earned each store renting movie films?
    Return a list of tuples, each containing (<store-id>, <earnings-in-decimal>)
    """
    
    earnings_per_staff = Payment.objects.values("staff").annotate(Sum("amount"))
    return [(element['staff'], element['amount__sum']) for element in earnings_per_staff]
        


def assignment_7():
    """
    List the first 4 cities where customers rent more Films
    """
    # Return a list with a dictionary containing city names and the amount of rentals per city, ordered by: highest rentals to lowest
    list_of_city_rentals = City.objects.values('city').annotate(Count('address__customer__rental')).order_by('-address__customer__rental__count')
    top_4_cities_filtered = list_of_city_rentals[0:4]
    return [cities['city'] for cities in top_4_cities_filtered]


def assignment_8():
    """
    List how many Films are there for each language.
    """
    # list_of_langs = []
    # for lang in Language.objects.all():
    #     list_of_langs.append((lang.name,len(Film.objects.filter(language=lang))))
    return [(lang.name, len(Film.objects.filter(language=lang))) for lang in Language.objects.all()]


def assignment_9():
    """
    Which is the most rented Film?
    """
    anon=Rental.objects.values("inventory__film__title").annotate(Count("rental_date"))
    # You receive:  {'rental_date__count__max': 34}
    max_rental_result = anon.aggregate(Max("rental_date__count"))
    # You receive: [{'inventory__film__title': u'BUCKET BROTHERHOOD', 'rental_date__count': 34}]
    return anon.filter(rental_date__count=max_rental_result['rental_date__count__max'])[0]['inventory__film__title']
