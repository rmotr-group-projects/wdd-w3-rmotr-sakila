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
    return Rental.objects.filter(return_date=None).count()


def assignment_3():
    """
    List the full name of all Staff members that live in Canada
    """
    canadians = Staff.objects.filter(address__city__country__country_id=20)
    return ['{} {}'.format(canadian.first_name, canadian.last_name) for canadian in canadians]


def assignment_4():
    """
    Who is the customer that has rented the most Films?
    """
    # cust_with_rentals = Customer.objects.values(
    #     'first_name', 'last_name').annotate(Count('rental'))
    # max_rentals = cust_with_rentals.aggregate(Max('rental__count'))['rental__count__max']
    # biggest_renter = cust_with_rentals.get(rental__count=max_rentals)
    # return ' '.join([biggest_renter['first_name'], biggest_renter['last_name']])
    
    cust_with_rentals = Customer.objects.annotate(Count('rental')).order_by('-rental__count')
    biggest_renter = cust_with_rentals[0]
    return ' '.join([biggest_renter.first_name, biggest_renter.last_name])


def assignment_5():
    """
    Which is the most popular FilmCategory?
    """
    # rental_count_by_category = Category.objects.annotate(
    #     rental_count=Count('filmcategory__film__inventory__rental')
    # )
    # max_rentals = rental_count_by_category.aggregate(Max('rental_count'))['rental_count__max']
    # popular_category = rental_count_by_category.get(rental_count=max_rentals)
    # return popular_category.name
    
    rental_count_by_category = Category.objects.annotate(
        rental_count=Count('filmcategory__film__inventory__rental')
    ).order_by('-rental_count')
    return rental_count_by_category[0].name


def assignment_6():
    """
    How much has earned each store renting movie films?
    Return a list of tuples, each containing (<store-id>, <earnings-in-decimal>)
    """
    # First try:
    # earnings_by_store = Store.objects.annotate(
    #     earnings=Sum('staff__payment__amount')
    # )
    
    # Second try:
    earnings_by_store = Store.objects.annotate(
        earnings=Sum('staff__rental__payment__amount')
    )
    return [(store.store_id, store.earnings) for store in earnings_by_store]


def assignment_7():
    """
    List the first 4 cities where customers rent more Films
    """
    rental_count_by_city = City.objects.annotate(
        rental_count=Count('address__customer__rental')
    ).order_by('-rental_count')
    return [city.city for city in rental_count_by_city[:4]]


def assignment_8():
    """
    List how many Films are there for each language.
    """
    film_count_by_language = []
    
    # First try:
    # for language in Language.objects.values('name').annotate(Count('film')):
    #     film_count_by_language.append((language['name'], language['film__count']))
    
    # Second try.  Appends them in the order expected in the tests
    for language in Language.objects.annotate(Count('film')):
        film_count_by_language.append((language.name, language.film__count))
        
    return film_count_by_language


def assignment_9():
    """
    Which is the most rented Film?
    """
    rental_count_by_film = Film.objects.annotate(
        rental_count=Count('inventory__rental')
    ).order_by('-rental_count')
    return rental_count_by_film[0].title
