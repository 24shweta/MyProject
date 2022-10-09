import pickle
import json
import re
import config
import numpy as np

class BigMartProject():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Identifier,Item_Type,Outlet_Identifier):
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = Outlet_Type
        self.Item_Identifier = Item_Identifier
        self.Item_Type = Item_Type
        self.Outlet_Identifier = Outlet_Identifier

    def load_data(self):
        with open(config.model_path,"rb")as f:
            self.model = pickle.load(f)
        with open(config.re_dta,"r")as f:
            self.replace = json.load(f)

    def get_outlet_sales(self):
        self.load_data()
        result = np.zeros(len(self.replace["column"]))
        result[0] = self.Item_Weight
        result[1] = self.replace["Item_Fat_Content"][self.Item_Fat_Content]
        result[2] = self.Item_Visibility
        result[3] = self.Item_MRP
        result[4] = self.Outlet_Establishment_Year
        result[5] = self.replace["Outlet_Size"][self.Outlet_Size]
        result[6] = self.replace["Outlet_Location_Type"][self.Outlet_Location_Type]
        result[7] = self.replace["Outlet_Type"][self.Outlet_Type]
        Item_Identifier_index = self.replace["column"].index(self.Item_Identifier)
        result[Item_Identifier_index] = 1
        Item_Type_index = self.replace["column"].index(self.Item_Type)
        result[Item_Type_index] = 1
        Outlet_Identifier_index = self.replace["column"].index(self.Outlet_Identifier)
        result[Outlet_Identifier_index] = 1
        outlet_sales_predict = self.model.predict([result])
        return outlet_sales_predict

