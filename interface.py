from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
from utils import BigMartProject

@app.route("/")
def home():
    return "welcome to the big mart project."

@app.route("/predict_sales")

def get_predict_sales():
    data = request.form
    Item_Weight = eval(data["Item_Weight"])
    Item_Fat_Content = data["Item_Fat_Content"]
    Item_Visibility = eval(data["Item_Visibility"])
    Item_MRP = eval(data["Item_MRP"])
    Outlet_Establishment_Year = eval(data["Outlet_Establishment_Year"])
    Outlet_Size =data["Outlet_Size"]
    Outlet_Location_Type = data["Outlet_Location_Type"]
    Outlet_Type = data["Outlet_Type"]
    Item_Identifier = data["Item_Identifier"]
    Item_Type = data["Item_Type"]
    Outlet_Identifier = data["Outlet_Identifier"]
    predictor = BigMartProject(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Identifier,Item_Type,Outlet_Identifier)
    final_result =predictor.get_outlet_sales()
    return f"{final_result}"
app.run()
