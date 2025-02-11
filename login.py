from tkinter import *
from regis import RegistrationPage
import sqlite3

class Login:
    def __init__(self, root, on_login_callback):
        self.root = root
        self.root.geometry('400x600')  # Window size
        self.root.title("Login")
        self.root.configure(bg="white")
        self.on_login_callback = on_login_callback  # Store callback function

        # Sample user data (username: password)
        self.user_data = {
            "admin": "admin",
        }

        self.create_widgets()

    def create_widgets(self):
        """Create all widgets for the login form"""
        Label(self.root, text='Namaste', font=('Times New Roman', 20, "bold"), bg="#f9f9f9").pack(pady=10)
        
        # Username input field
        Label(self.root, text='Email/Username', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.username_entry = Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        # Password input field
        Label(self.root, text='Password', font=('Times New Roman', 12), bg="#f9f9f9").pack(pady=5)
        self.password_entry = Entry(self.root, width=30, show='*')
        self.password_entry.pack(pady=5)

        # Feedback label for error messages
        self.feedback_label = Label(self.root, text="", font=('Times New Roman', 12), bg="#f9f9f9")
        self.feedback_label.pack(pady=9)

        # Login button
        Button(self.root, text='Login', font=('Times New Roman', 12), background='blue', fg='white', width=20,
               command=self.login).pack(pady=6)

        # Create new account button
        Label(self.root, text="Click for new account", font=("Times New Roman", 10), bg="#f9f9f9").pack(pady=5)
        Button(self.root, text="Create New Account", font=("Times New Roman", 10), fg="white", bg="green", width=20,
               command=self.registration).pack(pady=5)

        self.username_entry.focus()

    def login(self):
        """Handle the login logic"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == 'admin' and password == 'admin':
            from admin import AdminDashboard
            AdminDashboard(self.root)
        else:
            self.conn = sqlite3.connect("regis.db")
            self.cursor = self.conn.cursor()
            
            try:
                # Parameterized query to avoid SQL injection
                self.cursor.execute("""
                    SELECT user_type 
                    FROM user_registration 
                    WHERE (full_name = ? OR email = ?) AND password = ?
                """, (username, username, password))
                
                result = self.cursor.fetchone()  # Fetch one row
                
                if result:
                    user_type = result[0].lower()
                    
                    if user_type == "driver":
                        for widget in self.root.winfo_children():
                            widget.destroy()
                        from driverdashboard import DriverDashboard
                        DriverDashboard(self.root)
                    elif user_type == "user":
                        for widget in self.root.winfo_children():
                            widget.destroy()
                        from userdashboard import CustomerDashboard
                        CustomerDashboard(self.root)
                    else:
                        self.feedback_label.config(text="Unknown user type.", fg="red")
                else:
                    self.feedback_label.config(text="Invalid username or password.", fg="red")
            except sqlite3.Error as e:
                self.feedback_label.config(text=f"Database error: {e}", fg="red")
            finally:
                self.conn.close()  # Always close the connection

    def registration(self):
        """Open the registration page when the user clicks 'Create New Account'"""
        try:
            self.new_window = Toplevel(self.root)
            self.app = RegistrationPage(self.new_window)
        except Exception as e:
            self.feedback_label.config(text="Registration feature not available.", fg="blue")
            print(f"Error loading RegistrationApp: {e}")

