from tkinter import *
import sqlite3
import re

class RegistrationPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x600')
        self.root.title("Register Page")
        self.root.configure(bg="white")
        self.create_database()
        self.create_page()

    def create_database(self):
        self.conn = sqlite3.connect('regis.db')
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
        

    def create_page(self):
        Label(self.root, text='Sign up for Free', font=('Times New Roman', 20, "bold"), bg="#f9f9f9").pack(pady=30)
        
        Label(self.root, text='Full Name/ User Name', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.name_entry = Entry(self.root, width=35)
        self.name_entry.pack(pady=5)
        
        Label(self.root, text='Email', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.email_entry = Entry(self.root, width=35)
        self.email_entry.pack(pady=5)
        
        Label(self.root, text='Phone Number', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.phone_entry = Entry(self.root, width=35)
        self.phone_entry.pack(pady=5)
        
        Label(self.root, text='Address', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.address_entry = Entry(self.root, width=35)
        self.address_entry.pack(pady=5)

        Label(self.root, text='Password', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.password_entry = Entry(self.root, width=35, show='*')  # Masking password input
        self.password_entry.pack(pady=5)
        
        Label(self.root, text='User Type', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.user_type_var = StringVar(self.root)
        self.user_type_var.set("Select User Type")
        OptionMenu(self.root, self.user_type_var, "Driver", "User").pack(pady=5)

        Button(self.root, text='Submit', font=('Times New Roman', 12), bg='green', fg='white', width=25, command=self.register).pack(pady=10)
        Button(self.root, text='Back', font=("Times New Roman", 12), bg='blue', fg='white', width=25, command=self.root.withdraw).pack(pady=20)

        self.feedback_label = Label(self.root, text="", font=('Times New Roman', 12), bg="#f9f9f9")
        self.feedback_label.pack(pady=5)

    def register(self):
        full_name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        password = self.password_entry.get().strip()  
        user_type = self.user_type_var.get()

        if not full_name or len(full_name) < 5:
            self.feedback_label.config(text="Full Name must be at least 5 characters.", fg="red")
            return

        # Check if email is valid (simple email regex)
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.feedback_label.config(text="Valid Email is required.", fg="red")
            return

        # Check if phone number has exactly 10 digits
        if not phone.isdigit() or len(phone) != 10:
            self.feedback_label.config(text="Phone Number must be exactly 10 digits.", fg="red")
            return

        # Check if address has at least 8 characters
        if not address or len(address) < 5:
            self.feedback_label.config(text="Address must be at least 5 characters.", fg="red")
            return

        # Check if password has at least 8 characters
        if not password or len(password) < 5:
            self.feedback_label.config(text="Password must be at least 5 characters.", fg="red")
            return
        if user_type == "Select User Type":
            self.feedback_label.config(text="Please select a User Type.", fg="red")
            return

        try:
            self.cursor.execute("""
                INSERT INTO user_registration (full_name, email, phone, address, password, user_type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (full_name, email, phone, address, password, user_type))
            self.conn.commit()
            self.conn.close()
            self.feedback_label.config(text="Account Created Successfully!", fg="green")
        except sqlite3.IntegrityError:
            self.feedback_label.config(text="Email already exists.", fg="red")
        except Exception as e:
            self.feedback_label.config(text=f"Error: {e}", fg="red")

if __name__ == "__main__":
    root = Tk()
    app = RegistrationPage(root)
    root.mainloop()
