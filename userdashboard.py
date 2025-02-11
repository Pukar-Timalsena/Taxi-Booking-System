from tkinter import *
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
from datetime import datetime
import sqlite3
from admin import AdminDashboard

class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")  # Title 
        self.root.geometry("800x700")  # size
        self.root.configure(bg="white")  # background color
        self.adminDashboard = AdminDashboard
        self.header_frame = Frame(self.root, bg="green", height=70)  # 
        self.header_frame.pack(fill="x")
    def create_database(self):
        self.conn = sqlite3.connect('us.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_registration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL
            )
        """)
        self.conn.commit()
        # Add the Dashboard title to the header
        Label(self.header_frame, text="Customer Dashboard", font=("Times New Roman", 20, "bold"), bg="green", fg="white").pack(side=LEFT, padx=20)

        # Add a Logout button to the header
        Button(self.header_frame, text="Logout", font=("Times New Roman", 12), bg="white", fg="black", command=self.logout).pack(side=RIGHT, padx=20, pady=10)
        
        # Booking Section
        self.form_frame = Frame(self.root, bg="white")
        self.form_frame.pack(fill="x", padx=20, pady=10)

        Label(self.form_frame, text="Pickup Location:", font=("Times New Roman", 12), bg="white").pack(anchor="w", padx=10, pady=5)
        self.pickup_entry = Entry(self.form_frame, font=("Times New Roman", 12))
        self.pickup_entry.pack(fill="x", padx=10, pady=5)

        Label(self.form_frame, text="DropOff Location:", font=("Times New Roman", 12), bg="white").pack(anchor="w", padx=10, pady=5)
        self.dropoff_entry = Entry(self.form_frame, font=("Times New Roman", 12))
        self.dropoff_entry.pack(fill="x", padx=10, pady=5)

        Label(self.form_frame, text="Pickup Date:", font=("Times New Roman", 12), bg="white").pack(anchor="w", padx=10, pady=5)
        self.pickup_date = DateEntry(self.form_frame, font=("Times New Roman", 12), date_pattern="yyyy-mm-dd")
        self.pickup_date.pack(padx=10, pady=5, anchor="s", fill="x")

        Label(self.form_frame, text="Pickup Time:", font=("Times New Roman", 12), bg="white").pack(anchor="w", padx=10, pady=5)
        self.pickup_time = Entry(self.form_frame, font=("Times New Roman", 12))
        self.pickup_time.pack(fill="x", padx=10, pady=5)
        self.pickup_time.insert(0, datetime.now().strftime("%I:%M:%S %p"))  # it gives current time

        # Confirm and Cancel Buttons
        Button(self.form_frame, text="Confirm", font=("Times New Roman", 12), bg="green", fg="white", command=self.confirm_ride).pack(side=LEFT, padx=10, pady=10)
        Button(self.form_frame, text="Cancel", font=("Times New Roman", 12), bg="red", fg="white", command=self.cancel_ride).pack(side=RIGHT, padx=10, pady=10)

        # Booking History Section
        self.history_frame = Frame(self.root, bg="white")
        self.history_frame.pack(fill="both", expand=True, padx=20, pady=10)

        Label(self.history_frame, text="Booking History", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=5)

        # Table for history using Treeview
        self.history_table = Treeview(self.history_frame, columns=("pickup", "dropoff", "time", "date", "status"), show="headings", height=10)
        self.history_table.pack(fill="both", expand=True, padx=10, pady=5)

        # Define column headings
        self.history_table.heading("pickup", text="Pickup Location")
        self.history_table.heading("dropoff", text="DropOff Location")
        self.history_table.heading("time", text="Time")
        self.history_table.heading("date", text="Date")
        self.history_table.heading("status", text="Status")

        # Define column widths
        self.history_table.column("pickup", width=80)
        self.history_table.column("dropoff", width=80)
        self.history_table.column("time", width=50)
        self.history_table.column("date", width=70)
        self.history_table.column("status", width=70)

        # Add sample data to the table
        self.sample_data()

    def sample_data(self):
        bookings = [
            ("Koteshwor", "Ratnapark", "12:00", "1/12/23", "complete"),
            ("Baneshwor", "Jawalakhel", "12:30", "1/11/23", "Completed"),
            ("Gwarko", "Pulchowk", "12:15", "1/11/23", "complete"),
            ("Lagankhel", "Ratnapark", "10:00", "12/18/22", "Completed"),
            ("Lagankhel", "Jawalakhel", "10:30", "12/17/22", "Completed"),
        ]
        for booking in bookings:
            self.history_table.insert("", "end", values=booking)

    def cancel_ride(self):
        selected_item = self.history_table.selection()
        if selected_item:
            self.history_table.delete(selected_item)
        else:
            print("No ride selected to cancel.")

    def confirm_ride(self):
        # Get booking details from the customer input fields
        pickup_location = self.pickup_entry.get()
        dropoff_location = self.dropoff_entry.get()
        pickup_date = self.pickup_date.get()
        pickup_time = self.pickup_time.get()

        if pickup_location and dropoff_location and pickup_date and pickup_time:
            # Confirm the booking
            booking_details = f"Pickup: {pickup_location}, Dropoff: {dropoff_location}, Time: {pickup_time}, Date: {pickup_date}"
            self.history_table.insert("", "end", values=(pickup_location, dropoff_location, pickup_time, pickup_date, "Pending"))
            print("Booking confirmed!")

            # Notify the Admin Dashboard to update
            self.adminDashboard.update_booking_list(booking_details)  # Call method in Admin Dashboard

        else:
            print("Please fill in all the fields.")

    def logout(self):
        print("Logged out.")
        self.root.destroy()  # Close the main window when logging out

if __name__ == "__main__":
    root = Tk()
    app = CustomerDashboard(root)
    root.mainloop()
