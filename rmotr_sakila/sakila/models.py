from __future__ import unicode_literals

from django.db import models


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'actor'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'country'

    def __str__(self):
        return self.country


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'city'

    def __str__(self):
        return self.city


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'address'

    def __str__(self):
        return self.address


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return self.name


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    manager_staff = models.ForeignKey('sakila.Staff',
                                      related_name='store_managed_by_me')
    address_id = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'store'


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address)
    active = models.BinaryField()
    models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'customer'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'language'

    def __str__(self):
        return self.name


class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(Language)
    original_language_id = models.IntegerField(blank=True, null=True)
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.IntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film'

    def __str__(self):
        return self.title


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)


class FilmCategory(models.Model):
    film = models.ForeignKey(Film)
    category = models.ForeignKey(Category)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_category'
        unique_together = (('film', 'category'),)


class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    film = models.ForeignKey(Film)
    store = models.ForeignKey(Store)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'inventory'


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address)
    picture = models.BooleanField()
    email = models.EmailField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(Store)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'staff'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory)
    customer = models.ForeignKey(Customer)
    return_date = models.DateTimeField()
    staff = models.ForeignKey(Staff)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer)
    staff = models.ForeignKey(Staff)
    rental = models.ForeignKey(Rental, blank=True, null=True)
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'payment'
