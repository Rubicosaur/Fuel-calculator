
class fuel:

    def CalcFuelConsumption(self, RangePassed, Liters):
        AvgConsumption =round((Liters/RangePassed)*100,2)
        return AvgConsumption
    
    def CalcPricePer100km(self, LitersPer100km, PricePerLiter):
        Price = round(LitersPer100km*PricePerLiter,2)
        return Price



   