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


        # Navigation bar
        self.create_navigation()

        # Create frames
        self.input_frame = tk.Frame(self.main_window) # Will hold the Entry and Submit buttons
        self.output_frame = tk.Frame(self.main_window) # Will hold the output 
        self.input_frame.pack()
        self.output_frame.pack()

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
        # Clear the frames
        self.clear()

        self.label_ins = tk.Label(self.input_frame, text="Enter Instructor ID: ")
        self.label_ins.pack(side="left")

        self.instructor_id_entry = tk.Entry(self.input_frame, width=10)
        self.instructor_id_entry.pack(side="left")

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.handle_instructor_submit)

        self.name = tk.StringVar()
        self.dept = tk.StringVar()
        self.loc = tk.StringVar()

        self.name_label = tk.Label(self.output_frame, textvariable=self.name)
        self.dept_label = tk.Label(self.output_frame, textvariable=self.dept)
        self.loc_label = tk.Label(self.output_frame, textvariable=self.loc)

        self.name_label.pack(side="top")
        self.dept_label.pack(side="top")
        self.loc_label.pack(side="top")

        self.submit_button.pack(side="left")

    def display_department_information(self):
        self.clear()

        self.label_dept = tk.Label(self.input_frame, text="Enter Department Name: ")
        self.label_dept.pack(side="left")

        self.department_name_entry = tk.Entry(self.input_frame, width=10)
        self.department_name_entry.pack(side="left")

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.handle_department_submit)
        self.submit_button.pack(side="left")
        
        self.loc = tk.StringVar()
        self.budget = tk.StringVar()

        self.loc_label = tk.Label(self.output_frame, textvariable=self.loc)
        self.budget_label = tk.Label(self.output_frame, textvariable=self.budget)

        self.loc_label.pack(side="top")
        self.budget_label.pack(side="top")


    def clear(self):
        # Clears the input and output frames
        self.input_frame.destroy()
        self.output_frame.destroy()

        # Recreate the frames as empty frames
        self.input_frame = tk.Frame(self.main_window)
        self.output_frame = tk.Frame(self.main_window)

        # Pack the frames
        self.input_frame.pack()
        self.output_frame.pack()

    def handle_instructor_submit(self):
        text = self.instructor_id_entry.get()

        if text in self.instructors:
            self.name.set(f"Name: {self.instructors[text][0]}")
            self.dept.set(f"Department: {self.instructors[text][1]}")
            self.loc.set(f"Building: {self.departments[self.instructors[text][1]][0]}")
        else:
            self.name.set("Instructor not found")
            self.dept.set("")
            self.loc.set("")


    def handle_department_submit(self):
        text = self.department_name_entry.get()

        if text in self.departments:
            self.loc.set(f"Building: {self.departments[text][0]}")
            self.budget.set(f"Budget: {self.departments[text][1]}")
        else:
            self.loc.set("Department not found")
            self.budget.set("")

        

    


