from tkinter import *
from tkinter.ttk import Treeview

class DriverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Dashboard")
        self.root.geometry("800x700")
        self.root.config(bg="white")  # Background color for the root window
        
        self.tasks = [  # Example of pre-assign task
            ("Ram", "Koteshwor", "Ratnapark", "12:00AM","12/11/2024"),
            ("Krishna", "Lagankhel", "Jawalakhel","12:00AM","12/11/2024"),
            ("Hari", "Jawalakhel", "Pulchowk","12:00AM","12/11/2024"),
        ]

        # Header Section
        self.header_frame = Frame(self.root, bg="green", height=70)  # Top green header bar
        self.header_frame.pack(fill="x")
        
        # Add the Dashboard title to the header
        Label(self.header_frame, text="Driver Dashboard", font=("Times New Roman", 20, "bold"), bg="green", fg="white").pack(side=LEFT, padx=20)
        
        # Add a Logout button to the header
        Button(self.header_frame, text="Logout", font=("Times New Roman", 12), bg="white", fg="black", command=self.logout).pack(side=RIGHT, padx=20, pady=10)
        
        # Assigned Tasks Section (Treeview Table)
        self.tasks_frame = LabelFrame(self.root, text="Assigned Tasks", font=("Times New Roman", 12, "bold"), bg="white", padx=20, pady=20)
        self.tasks_frame.pack(fill="x", padx=20, pady=10)

        self.tasks_table = Treeview(self.tasks_frame, columns=("customer", "pickup", "dropoff","time","date"), show="headings", height=8)
        self.tasks_table.pack(side=LEFT, fill="both", expand=True)

        # Setup columns for Assigned Tasks
        self.tasks_table.heading("customer", text="Customer")
        self.tasks_table.heading("pickup", text="Pickup Location")
        self.tasks_table.heading("dropoff", text="DropOff Location")
        self.tasks_table.heading("time", text="time")
        self.tasks_table.heading("date", text="date")
        
        self.tasks_table.column("customer", width=100)
        self.tasks_table.column("pickup", width=150)
        self.tasks_table.column("dropoff", width=150)
        self.tasks_table.column("time", width=150)
        self.tasks_table.column("date", width=150)
        
        # Setup the scroll bar for tasks table
        self.tasks_scrollbar = Scrollbar(self.tasks_frame, orient=VERTICAL, command=self.tasks_table.yview)
        self.tasks_scrollbar.pack(side=RIGHT, fill=Y)
        self.tasks_table.config(yscrollcommand=self.tasks_scrollbar.set)

        # Load the assigned tasks into the table
        self.update_task_history()

        
        # Task History Section (Treeview Table)
        self.history_frame = LabelFrame(self.root, text="Task History", font=("Times New Roman", 12, "bold"), bg="white", padx=20, pady=20)
        self.history_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.history_table = Treeview(self.history_frame, columns=("pickup", "dropoff", "time", "date", "status"), show="headings", height=10)
        self.history_table.pack(side=LEFT, fill="both", expand=True)

        # Setup columns for Task History
        self.history_table.heading("pickup", text="Pickup Location")
        self.history_table.heading("dropoff", text="DropOff Location")
        self.history_table.heading("time", text="Time")
        self.history_table.heading("date", text="Date")
        self.history_table.heading("status", text="Status")

        self.history_table.column("pickup", width=150)
        self.history_table.column("dropoff", width=150)
        self.history_table.column("time", width=100)
        self.history_table.column("date", width=100)
        self.history_table.column("status", width=100)

        # Setup the scroll bar for history table
        history_scrollbar = Scrollbar(self.history_frame, orient=VERTICAL, command=self.history_table.yview)
        history_scrollbar.pack(side=RIGHT, fill=Y)
        self.history_table.config(yscrollcommand=history_scrollbar.set)

        # Add sample data to history
        self.sample_data()

    def sample_data(self):
        """Adding some dummy data to the history Table."""
        bookings = [
            ("Koteshwor", "Ratnapark", "12:00", "1/12/23", "Pending"),
            ("Baneshwor", "Jawalakhel", "12:30", "1/11/23", "Completed"),
            ("Gwarko", "Pulchowk", "12:15", "1/11/23", "Pending"),
            ("Lagankhel", "Ratnapark", "10:00", "12/18/22", "Completed"),
            ("Lagankhel", "Jawalakhel", "10:30", "12/17/22", "Completed"),
        ]
        for booking in bookings:
            self.history_table.insert("", "end", values=booking)

    def update_task_history(self):
        """Load assigned tasks into the table."""
        self.tasks_table.delete(*self.tasks_table.get_children())  # Clear the table
        for task in self.tasks:
            self.tasks_table.insert("", "end", values=task)

    def logout(self):
        self.root.destroy()
        print("You have successfully logged out.") 

if __name__ == "__main__":
    root = Tk()
    app = DriverDashboard(root)
    root.mainloop()
