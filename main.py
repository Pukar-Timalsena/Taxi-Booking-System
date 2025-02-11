from tkinter import *
from login import Login
from userdashboard import CustomerDashboard
from driverdashboard import DriverDashboard
from admin import AdminDashboard
from regis import RegistrationPage

class TaxiBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600')  # Example window size
        self.root.title("Taxi Booking System")
        
        # Initialize the Login page
        Login(self.root, self.handle_login)  # Pass the handle_login function as callback

    def handle_login(self, username):
        """Handle the login based on username"""
        if username == "admin":
            self.show_admin_dashboard()
        elif username == "user1" or username == "user2":
            self.show_customer_dashboard()
        elif username == "driver":
            self.show_driver_dashboard()
        elif username == "regis":
            self.show_registration_page()  # Fixed method call
        else:
            print("Unknown role")

    def show_admin_dashboard(self):
        """Show the Admin Dashboard"""
        for widget in self.root.winfo_children():
            widget.destroy()
        AdminDashboard(self.root)  # Open Admin Dashboard

    def show_customer_dashboard(self):
        """Show the Customer Dashboard"""
        for widget in self.root.winfo_children():
            widget.destroy()
        CustomerDashboard(self.root)  # Open Customer Dashboard

    def show_driver_dashboard(self):
        """Show the Driver Dashboard"""
        for widget in self.root.winfo_children():
            widget.destroy()
        DriverDashboard(self.root)  # Open Driver Dashboard
    
    def show_registration_page(self):
        """Show the Registration Page"""
        for widget in self.root.winfo_children():
            widget.destroy()
        RegistrationPage(self.root)  # Pass the root window to RegistrationPage

if __name__ == "__main__":
    root = Tk()  # Create main window
    taxi_booking_system = TaxiBookingSystem(root) # Initialize the system with the main window
    root.mainloop()  # Run the main loop
