class FlightReservation:
    def __init__(self):
        # Informasi penerbangan disimpan dalam dictionary
        self.flights = {
            "FL001": {"destination": "Bali", "price": 1500000, "capacity": 100, "booked": 0},
            "FL002": {"destination": "Jakarta", "price": 1000000, "capacity": 150, "booked": 0},
            "FL003": {"destination": "Surabaya", "price": 1200000, "capacity": 80, "booked": 0},
        }

    def display_flights(self):
        # Menampilkan daftar penerbangan yang tersedia
        print("Daftar Penerbangan:")
        for flight_number, info in self.flights.items():
            print(f"{flight_number}: Tujuan: {info['destination']}, Harga: {info['price']}, Kapasitas: {info['capacity']}, Terpesan: {info['booked']}")

    def book_ticket(self):
        # Memilih penerbangan dan memasukkan jumlah tiket
        flight_number = input("Masukkan nomor penerbangan: ")
        if flight_number not in self.flights:
            print("Nomor penerbangan tidak valid.")
            return
        
        num_tickets = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
        flight = self.flights[flight_number]

        # Memeriksa kapasitas pesawat
        if flight["booked"] + num_tickets > flight["capacity"]:
            print("Jumlah tiket yang dipesan melebihi kapasitas pesawat.")
            return

        # Menghitung total harga
        total_price = num_tickets * flight["price"]
        flight["booked"] += num_tickets

        # Menampilkan struk tiket
        print("\nStruk Tiket:")
        print(f"Nomor Penerbangan: {flight_number}")
        print(f"Tujuan: {flight['destination']}")
        print(f"Jumlah Tiket: {num_tickets}")
        print(f"Total Harga: {total_price}")

def main():
    reservation_system = FlightReservation()
    
    while True:
        reservation_system.display_flights()
        reservation_system.book_ticket()
        
        another_booking = input("Apakah Anda ingin melakukan pemesanan lain? (y/n): ")
        if another_booking.lower() != 'y':
            break

if __name__ == "__main__":
    main()