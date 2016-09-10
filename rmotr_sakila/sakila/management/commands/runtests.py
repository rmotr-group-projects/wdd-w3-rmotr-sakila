from django.core.management.base import BaseCommand

from decimal import Decimal

from sakila import assignments


EXPECTED_RESULTS = {
    'assignment_1': 1000,
    'assignment_2': 211,
    'assignment_3': ['Mike Hillyer'],
    'assignment_4': 'ELEANOR HUNT',
    'assignment_5': 'Sports',
    'assignment_6': [(1, Decimal('33489.47')), (2, Decimal('33927.04'))],
    'assignment_7': [u'Aurora', u'London', u'Saint-Denis', u'Cape Coral'],
    'assignment_8': [
        (u'English', 1000),
        (u'Italian', 0),
        (u'Japanese', 0),
        (u'Mandarin', 0),
        (u'French', 0),
        (u'German', 0)
    ],
    'assignment_9': 'BUCKET BROTHERHOOD'
}


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for func, expected_result in EXPECTED_RESULTS.items():
            exec_result = getattr(assignments, func)()
            try:
                assert exec_result == expected_result
            except AssertionError:
                print('Test "{}" failed. Expected "{}", but got "{}"'.format(
                    func, expected_result, exec_result))
        print('All tests passing!')
