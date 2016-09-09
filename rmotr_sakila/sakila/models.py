# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the True
# Feel free to rename the models, but don't rename db_table values or field names.
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



"""
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City')
    postal_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s, tel: %s' % (self.address, self.address2, self.phone)

    class Meta:
        db_table = 'address'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country')
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s, %s' % (self.city, self.country)

    class Meta:
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.country

    class Meta:
        db_table = 'country'


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film', through='FilmActor')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'actor'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film', through='FilmCategory')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        db_table = 'category'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language')
    original_language = models.ForeignKey(
        'Language', blank=True, null=True,
        related_name='filmAsOriginalLanguage')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, through='FilmCategory')
    actors = models.ManyToManyField(Actor, through='FilmActor')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        db_table = 'film'


class FilmActor(models.Model):
    film_actor_id = models.IntegerField(null=True)
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_actor'


class FilmCategory(models.Model):
    film = models.ForeignKey(Film)
    category = models.ForeignKey(Category)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_category'


class FilmText(models.Model):
    film = models.ForeignKey(Film)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'film_text'

    def __str__(self):
        return self.title


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        db_table = 'language'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address)
    active = models.BinaryField()
    create_date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    active = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'customer'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film)
    store = models.ForeignKey('Store')
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'No.%d' % self.inventory_id

    class Meta:
        db_table = 'inventory'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory)
    customer = models.ForeignKey(Customer)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff')
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'No.%d' % self.rental_id

    class Meta:
        db_table = 'rental'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer)
    staff = models.ForeignKey('Staff')
    rental = models.ForeignKey('Rental')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.payment_id

    class Meta:
        db_table = 'payment'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address)
    email = models.CharField(max_length=50, blank=True)
    store = models.ForeignKey('Store')
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    picture = models.BinaryField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.username)

    class Meta:
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(
        Staff, related_name='store_managed_by_me')
    address = models.ForeignKey(Address)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'No.%d' % self.store_id

    class Meta:
        db_table = 'store'
"""
