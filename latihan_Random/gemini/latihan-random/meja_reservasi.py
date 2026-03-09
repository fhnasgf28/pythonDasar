import json 
import os 
import datetime 

class Table:
    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
    
    def __str__(self):
        return f"Meja ID: {self.table_id}, kapasitas: {self.capacity} orang"
    def to_dict(self):
        return {"table_id": self.table_id, "capacity": self.capacity}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['table_id'], data['capacity'])

class Reservation:
    def __init__(self, reservation_id, table_id,customer_name, phone_number,date,time, num_guests):
        self.reservation_id = reservation_id
        self.table_id = table_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.date = date
        self.time = time
        self.num_guests = num_guests
    
    def __str__(self):
        return (f"Reservasi ID: {self.reservation_id}\n"
        f"meja ID: {self.table_id}\n"
        f"Pelanggan: {self.customer_name}{self.phone_number}\n"
        f" Tanggal & waktu : {self.date}{self.time}\n"
        f" Jumlah Tamu: {self.num_guests}\n"
        )
    
    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "table_id": self.table_id,
            "customer_name": self.customer_name,
            "phone_number": self.phone_number,
            "date": self.date,
            "time": self.time,
            "num_guests": self.num_guests
        }
