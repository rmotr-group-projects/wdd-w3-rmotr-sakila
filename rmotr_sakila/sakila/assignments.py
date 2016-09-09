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
    return Film.objects.filter(
        inventory__rental__return_date__isnull=True).distinct().count()


def assignment_3():
    """
    List the full name of all Staff members that live in Canada
    """
    return ['{} {}'.format(s.first_name, s.last_name)
            for s in Staff.objects.filter(address__city__country__country='Canada')]

def assignment_4():
    """
    Who is the customer that has rented more Films?
    """
    customer = Customer.objects.annotate(
        count_rent=Count('rental')).order_by('-count_rent').first()
    return '{} {}'.format(customer.first_name, customer.last_name)


def assignment_5():
    """
    Which is the most popular FilmCategory?
    """
    return str(Category.objects.annotate(count_films=Count('filmcategory')).order_by('count_films').last())


def assignment_6():
    """
    How much has earned each store renting movie films?
    Return a list of tuples, each containing (<store-id>, <earnings-in-decimal>)
    """
    return [(doc.store_id, doc.rental_earned)
            for doc in Store.objects.all().annotate(
                rental_earned=Sum('inventory__rental__payment__amount'))]


def assignment_7():
    """
    List the first 4 cities where customers rent more Films
    """
    return [c.city for c in City.objects.annotate(
        count_rental=Count('address__customer__rental')).order_by('-count_rental')[:4]]


def assignment_8():
    """
    List how many Films are there for each language.
    """
    return list(Language.objects.annotate(
        count_films=Count('film')).values_list("name", "count_films"))


def assignment_9():
    """
    Which is the most rented Film?
    """
    return Rental.objects.values('inventory__film__title').annotate(
        Count('inventory__film')).order_by('-inventory__film__count').first()['inventory__film__title']
