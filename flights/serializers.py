from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Booking

class RegisterUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only = True)
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password' ]
		extra_kwargs = {'first_name': {'required': True},
						'last_name': {'required': True}}

	def create (self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(first_name=first_name, last_name=last_name, username = username)
		new_user.set_password(password)
		new_user.save()

		return validated_data

class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']
