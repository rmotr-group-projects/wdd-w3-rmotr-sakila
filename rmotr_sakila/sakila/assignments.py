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
    pass

def assignment_4():
    """
    Who is the customer that has rented more Films?
    """
    pass


def assignment_5():
    """
    Which is the most popular FilmCategory?
    """
    pass


def assignment_6():
    """
    How much has earned each store renting movie films?
    Return a list of tuples, each containing (<store-id>, <earnings-in-decimal>)
    """
    pass


def assignment_7():
    """
    List the first 4 cities where customers rent more Films
    """
    pass


def assignment_8():
    """
    List how many Films are there for each language.
    """
    pass


def assignment_9():
    """
    Which is the most rented Film?
    """
    pass
