import tkinter as tk
from file_io import get_department, get_instructors

class GUI:
    def __init__(self):
        # initialzie instructors and departments
        self.instructors = get_instructors()
        self.departments = get_department()

        # Initialize the main window and size
        self.main_window = tk.Tk()
        self.main_window.title("University System Information")
        self.main_window.geometry("400x150")


        # Main frame
        self.main_frame = tk.Frame(self.main_window)
        self.main_frame.pack(side='top')

        # Navigation bar
        self.create_navigation()


        self.main_window.mainloop()

    def create_navigation(self):
        # Navigation frame will be on every "page"
        self.navigation = tk.Frame(self.main_window)

        # Stores the radio choice
        self.nav_radio = tk.IntVar()

        # Creating the buttons
        self.radio1 = tk.Radiobutton(self.navigation, text='Get Instructor Info', variable=self.nav_radio, value=1, command=self.display_instructor_information)
        self.radio2 = tk.Radiobutton(self.navigation, text='Get Department Info', variable=self.nav_radio, value=2, command=self.display_department_information)
        self.radio3 = tk.Radiobutton(self.navigation, text='Clear', variable=self.nav_radio, value=3, command=self.clear)
        self.radio4 = tk.Radiobutton(self.navigation, text='Quit', variable=self.nav_radio, value=4, command = self.main_window.destroy)

        # Pack
        self.radio1.pack(side="left")
        self.radio2.pack(side="left")
        self.radio3.pack(side="left")
        self.radio4.pack(side="left")
        self.navigation.pack(side='top')

    def display_instructor_information(self):
        self.clear()

        self.top_frame = tk.Frame(self.main_frame)
        self.label_ins = tk.Label(self.top_frame, text="Enter Instructor ID: ")
        self.label_ins.pack(side="left")
        self.entry_ins = tk.Entry(self.top_frame)
        self.entry_ins.pack(side="left")
        self.button_ins = tk.Button(self.top_frame, text="Submit", command=self.get_instructor_info)
        self.button_ins.pack(side="left")
        self.top_frame.pack(side="top", anchor="w")

        # Align output under the entry box and left aligned
        self.bottom_frame = tk.Frame(self.main_frame)
        self.output_var = tk.StringVar()
        self.output = tk.Label(self.bottom_frame, textvariable=self.output_var, justify="left")
        self.output.pack(side="left")
        self.bottom_frame.pack(side="top", anchor="w")






    def display_department_information(self):
        self.clear()

        self.top_frame = tk.Frame(self.main_frame)
        self.label_dept = tk.Label(self.top_frame, text="Enter Department Name: ")
        self.label_dept.pack(side="left")
        self.entry_dept = tk.Entry(self.top_frame)
        self.entry_dept.pack(side="left")
        self.button_dept = tk.Button(self.top_frame, text="Submit", command=self.get_department_info)
        self.button_dept.pack(side="left")
        self.top_frame.pack(side="top", anchor="w")

        # Align output under the entry box and left aligned
        self.bottom_frame = tk.Frame(self.main_frame)
        self.output_var = tk.StringVar()
        self.output = tk.Label(self.bottom_frame, textvariable=self.output_var, justify="left")
        self.output.pack(side="left")
        self.bottom_frame.pack(side="top", anchor="w")


    def clear(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.main_window)
        self.main_frame.pack(side='top')

    def get_instructor_info(self):
        # Get the instructor ID from the entry box
        if id := self.entry_ins.get():
            # Get the instructor name
            name = self.instructors[id][0]

            # Get the department name
            dept_name = self.instructors[id][1]

            # Get the department location
            loc = self.departments[dept_name][0]

            self.output_var.set(f"Name: {name}\nDepartment: {dept_name}\nLocation: {loc}")
        else:
            self.output_var.set("Information not found.")

    def get_department_info(self):
        # Get the department name from the entry box
        if dept_name := self.entry_dept.get():
            # Get the department location
            loc = self.departments[dept_name][0]

            # Get the department budget
            budget = self.departments[dept_name][1]

            self.output_var.set(f"Location: {loc}\nBudget: {budget}")
        else:
            self.output_var.set("Information not found.")