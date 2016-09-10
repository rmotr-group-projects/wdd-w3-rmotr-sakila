from django.db.models import Count, Sum

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


def assignment_3():
    """
    List the full name of all Staff members that live in Canada
    """
    return [str(staff) for staff in
            Staff.objects.filter(address__city__country__country='Canada')]


def assignment_4():
    """
    Who is the customer that has rented more Films?
    """
    return str(Customer.objects.annotate(num_rentals=Count('rental')).order_by('-num_rentals')[0])


def assignment_5():
    """
    Which is the most popular FilmCategory?
    """
    return Category.objects.annotate(num_rentals=Count('filmcategory__film__inventory__rental')) \
        .order_by('-num_rentals')[0].name


def assignment_6():
    """
    How much has earned each store renting movie films?
    Return a list of tuples, each containing (<store-id>, <earnings-in-decimal>)
    """
    return [(store.store_id, store.earnings) for store in
            Store.objects.all().annotate(earnings=Sum('staff__payment__amount'))]


def assignment_7():
    """
    List the first 4 cities where customers rent more Films
    """
    return [str(city) for city in
            City.objects.all().annotate(num_rentals=Count('address__customer__rental')).order_by('-num_rentals')[:4]]


def assignment_8():
    """
    List how many Films are there for each language.
    """
    return [(lang.name, lang.num_films) for lang in Language.objects.annotate(num_films=Count('film'))]


def assignment_9():
    """
    Which is the most rented Film?
    """
    return str(Film.objects.annotate(num_rentals=Count('inventory__rental')).order_by('-num_rentals')[0])
