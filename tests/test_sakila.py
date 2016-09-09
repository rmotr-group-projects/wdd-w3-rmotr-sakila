from django.test import TestCase

from sakila.models import *


def query_one():
    return Actor.objects.count()


assert query_one() == 200
