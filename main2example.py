import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    # Class variable
    watermark = "The Real Estate Company"

    # Instance method
    def __init__(self, hotel_id):
        # Instance variable - self.hotel_id,self.name,self.city
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    # Instance method
    def book(self):
        """Book a hotel by changing its availability to no"""
        availability = df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    # Instance method
    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # Class method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic Method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False



class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        Place: {self.hotel.city}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello, This is digital ticket"

    def Download(self):
        pass