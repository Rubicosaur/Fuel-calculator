
import urllib.request
import urllib.error
import tkinter as tk
import pandas as pd
from html_table_parser import HTMLTableParser
from tkinter import messagebox as mbx



class DataGatherer:

    def get_fuel_data_from_web(self,fuel_name):

        root = tk.Tk()
        root.withdraw()

        def url_get_contents(url):
        # Connection error handler
            while True:
                try:
                    req = urllib.request.Request(url=url)
                    f = urllib.request.urlopen(req)
                    return f.read()
                    
                except (ConnectionError,urllib.error.URLError):
                    mbx.showerror("Error","No internet connection.")
                    print('No internet connection')
                    
        xhtml = url_get_contents("https://www.e-petrol.pl/notowania/rynek-krajowy/ceny-stacje-paliw").decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        frame = pd.DataFrame(p.tables[0])
        
        if(fuel_name == "Petrol 95"):
            country_fuel_price = frame.iloc[1,3]
        elif(fuel_name == "Petrol 98"):
            country_fuel_price = frame.iloc[1,2]
        elif(fuel_name == "Diesel"):
            country_fuel_price = frame.iloc[1,4]
        elif(fuel_name == "LPG"):
            country_fuel_price = frame.iloc[1,5]
        
        
        return country_fuel_price
        
