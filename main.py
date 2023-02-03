#Journey fuel cost app
#modules
from gui import AppInterface


print("Welcome to the Journey Fuel cost calculator.")
no_of_miles = float(input("No. of miles? :"))
cost_per_litre = float(input("Current cost of fuel per litre? "))
mile_per_gallon = float(input("What is your car's average MPG? "))


one_way_cost_calc = (cost_per_litre * no_of_miles) / mile_per_gallon * 4.546
one_way_cost = round(one_way_cost_calc,2)

print(f"Your fuel cost for one-way is: £{one_way_cost}")

app_ui=AppInterface()