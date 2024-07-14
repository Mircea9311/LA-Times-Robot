import customtkinter as tk
import Robot as robot



class App:

    def __init__(self, root):
        self.root = root
        #self.done = done
        self.root.geometry('500x300')
        self.root.title('Latest News Robot')
        tk.set_appearance_mode('Dark')
        tk.set_default_color_theme('dark-blue')
        self.btn_label = None
            
            
        self.frame = tk.CTkFrame(self.root)
        self.frame.pack(expand = 1)


        self.input_frame = tk.CTkFrame(self.frame)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        #input label
        self.input_1_label = tk.CTkLabel(self.input_frame, text='Insert search phrase:')
        self.input_1_label.grid(row=0, column=0, padx=10, pady=10)
        #input field
        self.input_1 = tk.CTkEntry(self.input_frame)
        self.input_1.grid(row=0, column=1, padx=10, pady=10)

        #label for number of months
        self.input_2_label = tk.CTkLabel(self.input_frame, text='Insert number of months:')
        self.input_2_label.grid(row = 1, column = 0, padx=10, pady=10)
        #input number of months
        self.input_2 = tk.CTkEntry(self.input_frame)
        self.input_2.grid(row=1, column=1, padx=10, pady=10)

        #start button
        self.start_btn = tk.CTkButton(self.frame, text='Start', command=self.click)
        self.start_btn.grid(row=1, column=0, padx=20, pady=20)

        self.create_menu()

        
    def click(self):
        self.erase_all()

        try:
            int_input = int(self.input_2.get())
        except ValueError:
            print("Not a valid number")
            self.btn_label = tk.CTkLabel(self.root, text='Insert a valid number of months, starting with 0', text_color='red',)
        else:
            #run robot
            output = robot.main(search_phrase=self.input_1.get(), number_of_months=int(self.input_2.get()))
            if(output == True):
                self.btn_label = tk.CTkLabel(self.root, text='Execution finished successfully, output saved inside the output directory of the project')
            else:
                self.btn_label = tk.CTkLabel(self.root, text='Execution finished successfully, no news found for the desired search phrase')

        self.btn_label.pack()


    def erase_all(self):
        if self.btn_label is not None:
            self.btn_label.destroy()
            self.btn_label = None

    def create_menu(self):
        self.menu = tk.CTkOptionMenu(self.root, values=['Dark theme', 'Light theme'], command=self.change_theme)
        self.menu.set('Dark theme')
        self.menu.pack(pady=10)


    def change_theme(self, choice):
        if choice == 'Dark theme':
            tk.set_appearance_mode('Dark')
        elif choice == 'Light theme':
            tk.set_appearance_mode('Light')


    
root = tk.CTk()

app = App(root)
root.mainloop()