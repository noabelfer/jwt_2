from django.contrib.auth.models import User
from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(db_column="flight_number", max_length=256, null=False)
    origin_country = models.CharField(db_column="origin_country", max_length=256, null=False)
    origin_city = models.CharField(db_column="origin_city", max_length=256, null=False)
    origin_airport_code = models.CharField(db_column="origin_airport_code", max_length=256, null=False)
    destination_country = models.CharField(db_column="destination_country", max_length=256, null=False)
    destination_city= models.CharField(db_column="destination_city", max_length=256, null=False)
    destination_airport_code = models.CharField(db_column="destination_airport_code", max_length=256, null=False)
    date_time_origin = models.DateTimeField(db_column="date_time_origin", max_length=256, null=False)
    date_time_destination = models.DateTimeField(db_column="date_time_destination", max_length=256, null=False)
    total_num_of_seats = models.IntegerField(db_column="total_num_of_seats", max_length=256, null=False)
    seats_left = models.IntegerField(db_column="seats_left", max_length=256, null=False)
    is_cancelled = models.BooleanField(db_column="is_cancelled", max_length=256, default=False)
    price = models.IntegerField(db_column="price", max_length=256, null=False)

    def __str__(self):
        return (
            f"Flight number: {self.flight_number} origin airport code:{self.origin_airport_code}, destination airport code:{self.destination_airport_code} "
        )

    class Meta:
        db_table = 'flights'

class Order(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.RESTRICT)
    User_id = models.ForeignKey(User, max_length=256, on_delete=models.RESTRICT)
    number_of_seats = models.IntegerField(db_column="number_of_seats", max_length=128, null=False)
    order_date = models.DateTimeField(db_column="date_time_destination", max_length=256, null=False)
    total_price = models.IntegerField(db_column="total_price", max_length=256, null=False)





