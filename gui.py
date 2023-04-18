import tkinter as tk

class GUI:
    def __init__(self):
        # Initialize the main window and size
        self.main_window = tk.Tk()
        self.main_window.title("University System Information")
        self.main_window.geometry("400x150")


        self.body_frame = tk.Frame(self.main_window)

        # Navigation bar
        self.create_navigation()

        self.main_window.mainloop()

    def create_navigation(self):
        # Navigation frame will be on every "page"
        self.navigation = tk.Frame(self.main_window)

        # Stores the radio choice
        self.nav_radio = tk.IntVar()

        # Creating the buttons
        self.radio1 = tk.Radiobutton(self.navigation, text='Get Instructor Info', variable=self.nav_radio, value=1, command=self.handle_radio_one)
        self.radio2 = tk.Radiobutton(self.navigation, text='Get Department Info', variable=self.nav_radio, value=2, command=self.handle_radio_two)
        self.radio3 = tk.Radiobutton(self.navigation, text='Clear', variable=self.nav_radio, value=3, command=self.handle_radio_three)
        self.radio4 = tk.Radiobutton(self.navigation, text='Quit', variable=self.nav_radio, value=4, command = self.main_window.destroy)

        # Pack
        self.radio1.pack(side="left")
        self.radio2.pack(side="left")
        self.radio3.pack(side="left")
        self.radio4.pack(side="left")
        self.navigation.pack(side='top')

    def handle_radio_one(self):
        # Destroy the body frame and create a new one
        self.body_frame.destroy()
        self.body_frame = tk.Frame(self.main_window)

        # Label
        self.label = tk.Label(self.body_frame, text="Enter the instructor's ID:")
        self.input_radio_one = tk.Entry(self.body_frame, width=10)
        self.submit_radio_one = tk.Button(self.body_frame, text="Submit", command=self.handle_submit_radio_one)


        self.body_frame.pack(side='top')
        self.label.pack(side='left')
        self.input_radio_one.pack(side='left')
        self.submit_radio_one.pack(side='left')
    
    def handle_radio_two(self):
        # Destroy the body frame and create a new one
        self.body_frame.destroy()
        self.body_frame = tk.Frame(self.main_window)


        self.label = tk.Label(self.body_frame, text="Enter the department's name:")
        self.input_radio_two = tk.Entry(self.body_frame, width=10)
        self.submit_radio_two = tk.Button(self.body_frame, text="Submit", command=self.handle_submit_radio_two)

        self.body_frame.pack(side='top')
        self.label.pack(side='left')
        self.input_radio_two.pack(side='left')
        self.submit_radio_two.pack(side='left')

    def handle_radio_three(self):
        self.body_frame.destroy()
        self.body_frame = tk.Frame(self.main_window)
        self.body_frame.pack(side='top')

    def handle_submit_radio_one(self):
        pass

    def handle_submit_radio_two(self):
        pass


