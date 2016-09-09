from django.contrib import admin

from sakila.models import *


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'first_name', 'last_name')
    search_fields = ('actor_id', 'first_name', 'last_name')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'address')
    search_fields = ('address_id', 'address')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name')
    search_fields = ('category_id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'city')
    search_fields = ('city_id', 'city')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country')
    search_fields = ('country_id', 'country')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'active')
    search_fields = ('customer_id', 'first_name', 'last_name')
    list_filter = ('active',)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_id', 'title')
    search_fields = ('film_id', 'title')


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'film_id')
    search_fields = ('actor_id', 'film_id')


@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ('film_id', 'category_id')
    search_fields = ('film_id', 'category_id')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'film_id', 'store_id')
    search_fields = ('inventory_id', 'film_id', 'store_id')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_id', 'name')
    search_fields = ('language_id', 'name')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'customer_id', 'amount')
    search_fields = ('payment_id', 'customer_id')


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('rental_id', 'rental_date')
    search_fields = ('rental_id',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'active')
    search_fields = ('staff_id', 'first_name', 'last_name')
    list_filter = ('active',)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'address_id')
    search_fields = ('store_id', 'address_id')


















