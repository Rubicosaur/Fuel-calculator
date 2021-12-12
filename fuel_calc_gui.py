import tkinter as tk
from tkinter import StringVar, Text, ttk
from tkinter import messagebox as mbx
import fuel_calculation as Fc
import sys
import web_data_gatherer as wg

class FuelCalcGUI:

    def __init__(self, master):

        # For root initialization

        self.master = master
        master.title("Fuel Calculator")
        canvas = tk.Canvas(master, height= 640, width=640, bg = "#D9D8D7")
        canvas.pack()

        # List of Fuels for listbox

        fuels = [
        "Select",
        "Petrol 95",
        "Petrol 98",
        "Diesel",
        "LPG"
        ]

        # Main frame configuration

        self.frame = tk.Frame(master, bg = "#D9D8D7")
        self.frame.place(relwidth=0.6,relheight=0.6, rely=0.1, relx=0.1)

        # Labels 

        self.label_title = tk.Label(master,text="Please insert values below",bg = "#D9D8D7",font=7)
        canvas.create_window(300,200,window=self.label_title)
        self.label_title.place(relx=0.3,rely=0.1,width= 300, height=30)

        self.label_distance = tk.Label(master,text="Distance passed in kilometers:",bg = "#D9D8D7")
        canvas.create_window(300,200,window=self.label_distance)
        self.label_distance.place(relx=0.1,rely=0.25,width= 200, height=30)

        self.label_fuel_consumed = tk.Label(master,text="Fuel consumed in liters:",bg = "#D9D8D7")
        canvas.create_window(300,200,window=self.label_fuel_consumed)
        self.label_fuel_consumed.place(relx=0.1,rely=0.35,width= 200, height=30)

        self.label_fuel_price = tk.Label(master,text="Fuel price per liter (optional):",bg = "#D9D8D7")
        canvas.create_window(300,200,window=self.label_fuel_price)
        self.label_fuel_price.place(relx=0.1,rely=0.45,width= 200, height=30)

        self.label_result_consumption = tk.Label(master,text="Average consumption",bg = "#D9D8D7")
        canvas.create_window(300,200,window=self.label_result_consumption)
        self.label_result_consumption.place(relx=0.15,rely=0.77,width= 150, height=30)
        
        self.label_result_price = tk.Label(master,text="Price per 100 km",bg = "#D9D8D7")
        canvas.create_window(300,200,window=self.label_result_price)
        self.label_result_price.place(relx=0.15,rely=0.82,width= 150, height=30)

        self.label_result = tk.Label(master,bg = "grey",text = "0 liters/100km",foreground="white")
        canvas.create_window(300,200,window=self.label_result)
        self.label_result.place(relx=0.53,rely=0.77,width= 150, height=30)

        self.label_final_price = tk.Label(master,bg = "grey",text = "-;-",foreground="white")
        canvas.create_window(300,200,window=self.label_final_price)
        self.label_final_price.place(relx=0.53,rely=0.82,width= 150, height=30)

        # Text boxes for entering information into userform

        self.entry_box_distance = tk.Entry(master)
        canvas.create_window(300,200,window=self.entry_box_distance)
        self.entry_box_distance.place( relx=0.53,rely=0.25,width= 150, height=30)

        self.entry_box__fuel_consumed = tk.Entry(master)
        canvas.create_window(300,200,window=self.entry_box__fuel_consumed )
        self.entry_box__fuel_consumed .place(relx=0.53,rely=0.35,width= 150, height=30)

        self.entry_box__fuel_price = tk.Entry(master)
        canvas.create_window(300,200,window=self.entry_box__fuel_price )
        self.entry_box__fuel_price .place(relx=0.53,rely=0.45,width= 150, height=30)



        # Drop down list

        
        self.combo_box_fuel = ttk.Combobox(master,values=fuels)
        canvas.create_window(300,200,window=self.combo_box_fuel)
        self.combo_box_fuel.place(relx=0.15,rely=0.55,width= 150, height=30)
        self.combo_box_fuel.current(0)



        # Command button



        self.calculate_command_button = tk.Button(master,text="Calculate",command=lambda: self.calculate_and_display() )
        canvas.create_window(300,200,window=self.calculate_command_button)
        self.calculate_command_button.place(relx=0.357,rely=0.7,width= 150, height=30)

        self.exit_command_button = tk.Button(master,text="Exit",command=sys.exit)
        canvas.create_window(300,200,window=self.exit_command_button)
        self.exit_command_button.place(relx=0.615,rely=0.92,width= 150, height=30)

        self.clear_command_button = tk.Button(master,text="Clear",command=lambda: self.clear_boxes())
        canvas.create_window(300,200,window=self.clear_command_button)
        self.clear_command_button.place(relx=0.53,rely=0.60,width= 150, height=30)

        self.get_price_command_button = tk.Button(master,text="Get price",command=lambda: self.get_fuel_price())
        canvas.create_window(300,200,window=self.get_price_command_button)
        self.get_price_command_button.place(relx=0.53,rely=0.55, width= 150, height=30)
        
        self.get_info_command_button = tk.Button(master,text="?",command=lambda: self.get_info())
        canvas.create_window(300,200,window=self.get_info_command_button)
        self.get_info_command_button.place(relx=0.77,rely=0.55, width= 30, height=30)


    

        # GUI specific functions

    def calculate_and_display(self):
        try:
            fuel_calculator = Fc.fuel()
            distance_value = float((self.entry_box_distance.get()).replace(",", "."))
            liters_value = float((self.entry_box__fuel_consumed.get()).replace(",","."))
            consumption_of_fuel = fuel_calculator.CalcFuelConsumption(distance_value, liters_value)
            self.label_result.config(text=str(consumption_of_fuel) + " liters/100 km")

            if(self.entry_box__fuel_price.get()!=""):
                try:
                    price_value = float((self.entry_box__fuel_price.get()).replace(",", "."))
                    avg_price = fuel_calculator.CalcPricePer100km(price_value,consumption_of_fuel)
                    self.label_final_price.config(text=str(avg_price) + " zł")
                    print(avg_price)
                except ValueError:
                    mbx.showerror("Error !", "Provided values are not numbers")

            print(consumption_of_fuel)
        except ValueError:
            mbx.showerror("Error !", "Provided values are not numbers")

        
    def get_fuel_price(self):
        self.entry_box__fuel_price.delete(0,"end")
        gatherer = wg.DataGatherer()
        price = gatherer.get_fuel_data_from_web(self.combo_box_fuel.get())
        self.entry_box__fuel_price.insert(0,price)


            
    def clear_boxes (self):
        self.entry_box_distance.delete(0,"end")
        self.entry_box__fuel_consumed.delete(0,"end")
        self.entry_box__fuel_price.delete(0,"end")
        self.label_result.config(text = "0 liters/100km")
        self.label_final_price.config(text = "-;-")

    def get_info (self):
        mbx.showinfo("Info", "Fuel price according to website: https://www.e-petrol.pl/notowania/rynek-krajowy/ceny-stacje-paliw")
   
       

# GUI starter
     
root = tk.Tk()
fuel_calc_gui = FuelCalcGUI(root)

        
root.mainloop()








