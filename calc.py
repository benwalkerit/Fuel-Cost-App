
class Calc:
    def calculate_oneway(no_of_miles, mile_per_gallon, cost_per_litre):
        one_way_cost_calc = (cost_per_litre * no_of_miles) / mile_per_gallon * 4.546
        return round(one_way_cost_calc,2)
    
    def calculate_return(no_of_miles, mile_per_gallon, cost_per_litre):
        one_way_cost_calc = (cost_per_litre * no_of_miles) / mile_per_gallon * 4.546
        return_cal = one_way_cost_calc = one_way_cost_calc
        return round(return_cal,2)