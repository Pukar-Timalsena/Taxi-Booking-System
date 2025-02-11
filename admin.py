from tkinter import *
from tkinter.ttk import Treeview


class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("800x700")
        self.root.config(bg="white")
        self.bookings_listbox = Listbox(self.root)  # Assuming a listbox or similar widget
        self.bookings = []  # Store booking details
        # Example Data
        self.bookings = [
            "Ram, Pickup: Koteshwor, Drop-off: Ratnapark, Time: 12:00 PM, Date: 2022-01-01",
            "Krishna, Pickup: Lagankhel, Drop-off: Jawalakhel, Time: 1:00 PM, Date: 2022-01-02",
            "Hari, Pickup: Jawalakhel, Drop-off: Pulchowk, Time: 2:00 PM, Date: 2022-01-03",
        ]
        self.drivers = ["Driver 1: Ramu", "Driver 2: Raju", "Driver 3: Ravi"]
        self.assigned_tasks = {}  

        # Header Section
        self.header_frame = Frame(self.root, bg="green", height=70)
        self.header_frame.pack(fill="x")

        Label(self.header_frame,text="Admin Dashboard",font=("Times New Roman", 20, "bold"),bg="green",fg="white",).pack(side=LEFT, padx=20)

        Button(self.header_frame, text="Logout", font=("Times New Roman", 12), bg="white", fg="black", command=self.logout).pack(side=RIGHT, padx=20, pady=10)

        # Bookings Section
        self.bookings_frame = LabelFrame(self.root, text="All Bookings", font=("Times New Roman", 12, "bold"), bg="white")
        self.bookings_frame.pack(fill="x", padx=20, pady=10)

        self.bookings_listbox = Listbox(self.bookings_frame, font=("Times New Roman", 10), height=8)
        self.bookings_listbox.pack(fill="x", padx=10, pady=10)

        for booking in self.bookings:
            self.bookings_listbox.insert(END, booking)

        # Drivers Section
        self.drivers_frame = LabelFrame(self.root, text="Assign to Drivers", font=("Times New Roman", 12, "bold"), bg="white")
        self.drivers_frame.pack(fill="x", padx=20, pady=10)

        Label(self.drivers_frame, text="Select Driver:", font=("Times New Roman", 10)).pack(anchor=W, padx=10, pady=5)
        self.driver_var = StringVar(value=self.drivers[0])
        self.driver_menu = OptionMenu(self.drivers_frame, self.driver_var, *self.drivers)
        self.driver_menu.pack(fill="x", padx=10, pady=5)

        Button(self.drivers_frame, text="Assign Booking", font=("Times New Roman", 12), bg="green", fg="white", command=self.assign_booking).pack(fill="x", padx=10, pady=10)

        # Tasks Section
        self.tasks_frame = LabelFrame(self.root, text="Assigned Tasks", font=("Times New Roman", 12, "bold"), bg="white")
        self.tasks_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tasks_listbox = Listbox(self.tasks_frame, font=("Times New Roman", 10), height=10)
        self.tasks_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        Button(self.drivers_frame, text="Cancel", font=("Times New Roman", 12), bg="red", fg="white", command=self.cancel_ride).pack(side=RIGHT, padx=10, pady=10)
    def cancel_ride(self):
        selected_indices = self.tasks_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            assignment = self.tasks_listbox.get(selected_index)
            driver = assignment.split("->")[-1].strip()
            self.tasks_listbox.delete(selected_index)
            self.assigned_tasks.pop(driver, None)
            print("Ride cancelled successfully.")
        else:
            print("No ride selected to cancel.")        
    def assign_booking(self):
        """Assign selected booking to the selected driver."""
        try:
            selected_booking = self.bookings_listbox.get(ACTIVE)
            selected_driver = self.driver_var.get()

            if not selected_booking:
                print("No booking selected.")
                return

            if selected_driver in self.assigned_tasks:
                print(f"Driver Busy: {selected_driver} is already assigned a task.")
                return

            assignment = f"{selected_booking} -> {selected_driver}"
            self.assigned_tasks[selected_driver] = selected_booking  # Track assignment by driver
            self.tasks_listbox.insert(END, assignment)
            self.bookings_listbox.delete(ACTIVE)  # Remove from bookings
        except Exception as e:
            print(f"Error assigning booking: {e}")
    def update_booking_list(self, booking_details):
        # Add the new booking to the list of bookings
        self.bookings.append(booking_details)
        self.bookings_listbox.insert(END, booking_details)
        print(f"New booking added: {booking_details}")
    def logout(self):
        self.root.destroy()
        print("Logged out successfully!")

if __name__ == "__main__":
    root = Tk()
    app = AdminDashboard(root)
    root.mainloop()
