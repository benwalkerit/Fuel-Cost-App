#modules
from tkinter import *
from calc import Calc

        
BACKGROUND_COLOR = "#d3d3d3"

class AppInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Journey Fuel Cost Calculator")
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
        self.title_label = Label(text="Journey Fuel Cost", fg="black", bg=BACKGROUND_COLOR)
        self.title_label.grid(row=0, column=0, columnspan=2)
        self.number_miles = Label(text="How many miles to your destination? ", fg="black", bg=BACKGROUND_COLOR)
        self.number_miles.grid(row=1, column =0)
        self.number_mpg = Label(text="What is your average MPG? ", fg="black", bg=BACKGROUND_COLOR)
        self.number_mpg.grid(row=2, column =0)
        self.fuel_cost = Label(text="Whats the cost of fuel per litre? £", fg="black", bg=BACKGROUND_COLOR)
        self.fuel_cost.grid(row=3, column =0)
        self.number_miles_in = Entry(width=6)
        self.number_miles_in.insert(END, string="100")
        self.number_miles_in.grid(row=1, column=1, columnspan=2)
        self.number_mpg_in = Entry(width=6)
        self.number_mpg_in.insert(END, string="35")
        self.number_mpg_in.grid(row=2, column=1, columnspan=2)
        self.fuel_cost_in = Entry(width=6)
        self.fuel_cost_in.insert(END, string="1.60")
        self.fuel_cost_in.grid(row=3, column=1, columnspan=2)
        self.calc_button = Button(text="Calculate", command=self.calculate, pady=20, padx=20)
        self.calc_button.grid(row=4, column=0, columnspan=2)
        self.oneway_label = Label(text="One-Way will cost £..... in fuel.", bg=BACKGROUND_COLOR)
        self.twoway_label = Label(text="Return trip will cost £..... in fuel.", bg=BACKGROUND_COLOR)
        self.oneway_label.grid(row=5, column=0, columnspan=2)
        self.twoway_label.grid(row=6, column=0, columnspan=2)     
        
        
        self.window.mainloop()
        
        
    def calculate(self):
        no_miles = float(self.number_miles_in.get()) 
        mpg = float(self.number_mpg_in.get())
        fuel = float(self.fuel_cost_in.get())
        one_way_cost_calc = (fuel * no_miles) / mpg * 4.546
        return_cal = one_way_cost_calc + one_way_cost_calc
        return_cost = round(return_cal,2)
        one_way_cost = round(one_way_cost_calc,2)
        print(one_way_cost)
        print(return_cost)
        self.oneway_label.config(text=f"One-Way will cost £{one_way_cost} in fuel.") 
        self.twoway_label.config(text=f"Return will cost £{return_cost} in fuel.")
        