from flask import Flask, render_template, json, request, jsonify
import threading
import pandas as pd
import sqlite3 as sql
from traceback import print_tb
from nsepython import *
from pytz import timezone 
from datetime import datetime
from openpyxl import load_workbook
from datetime import date
from time import sleep
import openpyxl
import numpy as np
from flask_sqlalchemy import SQLAlchemy

workbook_name1 = "9_10_data.xlsx"
workbook_name2 = "10_11_data.xlsx"
workbook_name3 = "11_12_data.xlsx"
workbook_name4 = "12_13_data.xlsx"
workbook_name5 = "13_14_data.xlsx"
workbook_name6 = "14_15_data.xlsx"
workbook_name7 = "15_16_data.xlsx"
current = ''
count= 0
no_strikes = 5
strike_values = []
strike_values1 = []
strike_values2 = []
strike_values3 = []
strike_values4 = []
strike_values5 = []
strike_values6 = []
strike_values7 = []
strike_values8 = []
strike_values9 = []
strike_values10 = []
strike_values11 = []
udelying_values = []

app = Flask(__name__)
POOL_TIME = 60

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dthbhqoalqpqzz:9e86f95f3e4c6e3affeaf01ce218c74b9383fc7ecb1fcedf9787233ebc2836b7@ec2-54-147-36-107.compute-1.amazonaws.com:5432/d3si1ses3p1blg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class monthone(db.Model):
    __tablename__ = 'monthone'
    id = db.Column(db.Integer, primary_key=True)
    txtcurrent_date = db.Column(db.Text())
    strtime = db.Column(db.Text())
    monthdate = db.Column(db.Text())
    coi = db.Column(db.Text())
    roc_coi = db.Column(db.Text())
    feature_val = db.Column(db.Text())
    roc_feature_val = db.Column(db.Text())
    feature_strikeval = db.Column(db.Text())
    roc_feature_strikeval = db.Column(db.Text())
    ltp = db.Column(db.Text())
    roc_ltp = db.Column(db.Text())
    volume = db.Column(db.Text())
    roc_volume = db.Column(db.Text())
    oi = db.Column(db.Text())
    roc_oi = db.Column(db.Text())
    nt = db.Column(db.Text())
    roc_nt = db.Column(db.Text())
    coi_nt = db.Column(db.Text())
    roc_coi_nt = db.Column(db.Text())
    ltp_rocvolume = db.Column(db.Text())
    roc_ltp_rocvolume = db.Column(db.Text())
    rocvol_nt = db.Column(db.Text())
    roc_rocvol_nt = db.Column(db.Text())

    def __init__(self, txtcurrent_date, strtime, monthdate, coi,roc_coi,feature_val,roc_feature_val,feature_strikeval,roc_feature_strikeval,ltp,roc_ltp,volume,roc_volume,oi,roc_oi,nt,roc_nt,coi_nt,roc_coi_nt,ltp_rocvolume,roc_ltp_rocvolume,rocvol_nt,roc_rocvol_nt):
        self.txtcurrent_date = txtcurrent_date
        self.strtime = strtime
        self.monthdate = monthdate
        self.coi = coi
        self.roc_coi = roc_coi
        self.feature_val = feature_val
        self.roc_feature_val = roc_feature_val
        self.feature_strikeval = feature_strikeval
        self.roc_feature_strikeval = roc_feature_strikeval
        self.ltp = ltp
        self.roc_ltp = roc_ltp
        self.volume = volume
        self.roc_volume = roc_volume
        self.oi = oi
        self.roc_oi = roc_oi
        self.nt = nt
        self.roc_nt = roc_nt
        self.coi_nt = coi_nt
        self.roc_coi_nt = roc_coi_nt
        self.ltp_rocvolume = ltp_rocvolume
        self.roc_ltp_rocvolume = roc_ltp_rocvolume
        self.rocvol_nt = rocvol_nt
        self.roc_rocvol_nt = roc_rocvol_nt

class Month2(db.Model):
    __tablename__ = 'month2'
    id = db.Column(db.Integer, primary_key=True)
    txtcurrent_date = db.Column(db.Text())
    strtime = db.Column(db.Text())
    monthdate = db.Column(db.Text())
    coi = db.Column(db.Text())
    roc_coi = db.Column(db.Text())
    feature_val = db.Column(db.Text())
    roc_feature_val = db.Column(db.Text())
    feature_strikeval = db.Column(db.Text())
    roc_feature_strikeval = db.Column(db.Text())
    ltp = db.Column(db.Text())
    roc_ltp = db.Column(db.Text())
    volume = db.Column(db.Text())
    roc_volume = db.Column(db.Text())
    oi = db.Column(db.Text())
    roc_oi = db.Column(db.Text())
    nt = db.Column(db.Text())
    roc_nt = db.Column(db.Text())
    coi_nt = db.Column(db.Text())
    roc_coi_nt = db.Column(db.Text())
    ltp_rocvolume = db.Column(db.Text())
    roc_ltp_rocvolume = db.Column(db.Text())
    rocvol_nt = db.Column(db.Text())
    roc_rocvol_nt = db.Column(db.Text())

    def __init__(self, txtcurrent_date, strtime, monthdate, coi,roc_coi,feature_val,roc_feature_val,feature_strikeval,roc_feature_strikeval,ltp,roc_ltp,volume,roc_volume,oi,roc_oi,nt,roc_nt,coi_nt,roc_coi_nt,ltp_rocvolume,roc_ltp_rocvolume,rocvol_nt,roc_rocvol_nt):
        self.txtcurrent_date = txtcurrent_date
        self.strtime = strtime
        self.monthdate = monthdate
        self.coi = coi
        self.roc_coi = roc_coi
        self.feature_val = feature_val
        self.roc_feature_val = roc_feature_val
        self.feature_strikeval = feature_strikeval
        self.roc_feature_strikeval = roc_feature_strikeval
        self.ltp = ltp
        self.roc_ltp = roc_ltp
        self.volume = volume
        self.roc_volume = roc_volume
        self.oi = oi
        self.roc_oi = roc_oi
        self.nt = nt
        self.roc_nt = roc_nt
        self.coi_nt = coi_nt
        self.roc_coi_nt = roc_coi_nt
        self.ltp_rocvolume = ltp_rocvolume
        self.roc_ltp_rocvolume = roc_ltp_rocvolume
        self.rocvol_nt = rocvol_nt
        self.roc_rocvol_nt = roc_rocvol_nt

class Month3(db.Model):
    __tablename__ = 'month3'
    id = db.Column(db.Integer, primary_key=True)
    txtcurrent_date = db.Column(db.Text())
    strtime = db.Column(db.Text())
    monthdate = db.Column(db.Text())
    coi = db.Column(db.Text())
    roc_coi = db.Column(db.Text())
    feature_val = db.Column(db.Text())
    roc_feature_val = db.Column(db.Text())
    feature_strikeval = db.Column(db.Text())
    roc_feature_strikeval = db.Column(db.Text())
    ltp = db.Column(db.Text())
    roc_ltp = db.Column(db.Text())
    volume = db.Column(db.Text())
    roc_volume = db.Column(db.Text())
    oi = db.Column(db.Text())
    roc_oi = db.Column(db.Text())
    nt = db.Column(db.Text())
    roc_nt = db.Column(db.Text())
    coi_nt = db.Column(db.Text())
    roc_coi_nt = db.Column(db.Text())
    ltp_rocvolume = db.Column(db.Text())
    roc_ltp_rocvolume = db.Column(db.Text())
    rocvol_nt = db.Column(db.Text())
    roc_rocvol_nt = db.Column(db.Text())

    def __init__(self, txtcurrent_date, strtime, monthdate, coi,roc_coi,feature_val,roc_feature_val,feature_strikeval,roc_feature_strikeval,ltp,roc_ltp,volume,roc_volume,oi,roc_oi,nt,roc_nt,coi_nt,roc_coi_nt,ltp_rocvolume,roc_ltp_rocvolume,rocvol_nt,roc_rocvol_nt):
        self.txtcurrent_date = txtcurrent_date
        self.strtime = strtime
        self.monthdate = monthdate
        self.coi = coi
        self.roc_coi = roc_coi
        self.feature_val = feature_val
        self.roc_feature_val = roc_feature_val
        self.feature_strikeval = feature_strikeval
        self.roc_feature_strikeval = roc_feature_strikeval
        self.ltp = ltp
        self.roc_ltp = roc_ltp
        self.volume = volume
        self.roc_volume = roc_volume
        self.oi = oi
        self.roc_oi = roc_oi
        self.nt = nt
        self.roc_nt = roc_nt
        self.coi_nt = coi_nt
        self.roc_coi_nt = roc_coi_nt
        self.ltp_rocvolume = ltp_rocvolume
        self.roc_ltp_rocvolume = roc_ltp_rocvolume
        self.rocvol_nt = rocvol_nt
        self.roc_rocvol_nt = roc_rocvol_nt

class NseDbDailyData(db.Model):
    __tablename__ = 'nsedbdailydata'
    id = db.Column(db.Integer, primary_key=True)
    str_time = db.Column(db.Text())
    c_oi = db.Column(db.Text())
    c_roc_oi = db.Column(db.Text())
    c_chng_in_oi = db.Column(db.Text())
    c_roc_chng_in_oi = db.Column(db.Text())
    c_volume = db.Column(db.Text())
    c_roc_volume = db.Column(db.Text())
    c_iv = db.Column(db.Text())
    c_roc_iv = db.Column(db.Text())
    c_ltp = db.Column(db.Text())
    c_roc_ltp = db.Column(db.Text())
    c_nt = db.Column(db.Text())
    c_roc_nt = db.Column(db.Text())
    c_ltp_vl = db.Column(db.Text())
    c_roc_ltp_vl = db.Column(db.Text())
    c_chng = db.Column(db.Text())
    c_oi_nt = db.Column(db.Text())
    c_roc_oi_nt = db.Column(db.Text())
    c_ltp_coi =db.Column(db.Text())
    c_roc_ltp_coi = db.Column(db.Text())
    c_bid_qty = db.Column(db.Text())
    c_bid_price = db.Column(db.Text())
    c_ask_price = db.Column(db.Text())
    c_ask_qty = db.Column(db.Text())
    strike_price = db.Column(db.Text())
    p_bid_qty = db.Column(db.Text())
    p_bid_price = db.Column(db.Text())
    p_ask_price = db.Column(db.Text())
    p_ask_qty = db.Column(db.Text())
    p_chng = db.Column(db.Text())
    p_ltp = db.Column(db.Text())
    p_roc_ltp = db.Column(db.Text())
    p_nt = db.Column(db.Text())
    p_roc_nt = db.Column(db.Text())
    p_ltp_vl = db.Column(db.Text())
    p_roc_ltp_vl = db.Column(db.Text())
    p_iv = db.Column(db.Text())
    p_roc_iv = db.Column(db.Text())
    p_volume = db.Column(db.Text())
    p_roc_volume = db.Column(db.Text())
    p_chng_in_oi = db.Column(db.Text())
    p_roc_chng_in_oi = db.Column(db.Text())
    p_oi = db.Column(db.Text())
    p_roc_oi = db.Column(db.Text())
    p_oi_nt = db.Column(db.Text())
    p_roc_oi_nt = db.Column(db.Text())
    p_ltp_coi = db.Column(db.Text())
    p_roc_ltp_coi = db.Column(db.Text())
    txtcurrent_date = db.Column(db.Text())
    c_roc_vol_roc_nt = db.Column(db.Text())
    roc_c_roc_vol_roc_nt = db.Column(db.Text())
    p_roc_vol_roc_nt = db.Column(db.Text())
    roc_p_roc_vol_roc_nt = db.Column(db.Text())

    def __init__(self, str_time, c_oi, c_roc_oi, c_chng_in_oi,c_roc_chng_in_oi,c_volume,c_roc_volume,c_iv,c_roc_iv,c_ltp,c_roc_ltp,c_nt,c_roc_nt,c_ltp_vl,c_roc_ltp_vl,c_chng,c_oi_nt,c_roc_oi_nt,c_ltp_coi,c_roc_ltp_coi,c_bid_qty,c_bid_price,c_ask_price,c_ask_qty,strike_price,p_bid_qty,p_bid_price,p_ask_price,p_ask_qty,p_chng,p_ltp,p_roc_ltp,p_nt,p_roc_nt,p_ltp_vl,p_roc_ltp_vl,p_iv,p_roc_iv,p_volume,p_roc_volume,p_chng_in_oi,p_roc_chng_in_oi,p_oi,p_roc_oi,p_oi_nt,p_roc_oi_nt,p_ltp_coi,p_roc_ltp_coi,txtcurrent_date,c_roc_vol_roc_nt,roc_c_roc_vol_roc_nt,p_roc_vol_roc_nt,roc_p_roc_vol_roc_nt):
        self.txtcurrent_date = txtcurrent_date
        self.str_time = str_time
        self.c_oi = c_oi
        self.c_roc_oi = c_roc_oi
        self.c_chng_in_oi = c_chng_in_oi
        self.c_roc_chng_in_oi = c_roc_chng_in_oi
        self.c_volume = c_volume
        self.c_roc_volume = c_roc_volume
        self.c_iv = c_iv
        self.c_roc_iv = c_roc_iv
        self.c_ltp = c_ltp
        self.c_roc_ltp = c_roc_ltp
        self.c_nt = c_nt
        self.c_roc_nt = c_roc_nt
        self.c_ltp_vl = c_ltp_vl
        self.c_roc_ltp_vl = c_roc_ltp_vl
        self.c_chng = c_chng
        self.c_oi_nt = c_oi_nt
        self.c_roc_oi_nt = c_roc_oi_nt
        self.txtcurrent_date = txtcurrent_date
        self.c_ltp_coi = c_ltp_coi
        self.c_roc_ltp_coi = c_roc_ltp_coi
        self.c_bid_qty = c_bid_qty
        self.c_bid_price = c_bid_price
        self.c_ask_price = c_ask_price
        self.c_ask_qty = c_ask_qty
        self.strike_price = strike_price
        self.p_bid_qty = p_bid_qty
        self.p_bid_price = p_bid_price
        self.p_ask_price = p_ask_price
        self.p_ask_qty = p_ask_qty
        self.p_chng = p_chng
        self.p_ltp = p_ltp
        self.p_roc_ltp = p_roc_ltp
        self.p_nt = p_nt
        self.p_roc_nt = p_roc_nt
        self.p_ltp_vl = p_ltp_vl
        self.p_roc_ltp_vl = p_roc_ltp_vl
        self.p_iv = p_iv
        self.p_roc_iv = p_roc_iv
        self.p_volume = p_volume
        self.p_roc_volume = p_roc_volume
        self.p_chng_in_oi = p_chng_in_oi
        self.p_roc_chng_in_oi = p_roc_chng_in_oi
        self.p_oi = p_oi
        self.p_roc_oi = p_roc_oi
        self.p_oi_nt = p_oi_nt
        self.p_roc_oi_nt = p_roc_oi_nt
        self.p_ltp_coi = p_ltp_coi
        self.p_roc_ltp_coi = p_roc_ltp_coi
        self.txtcurrent_date = txtcurrent_date
        self.c_roc_vol_roc_nt = c_roc_vol_roc_nt
        self.roc_c_roc_vol_roc_nt = roc_c_roc_vol_roc_nt
        self.p_roc_vol_roc_nt = p_roc_vol_roc_nt
        self.roc_p_roc_vol_roc_nt = roc_p_roc_vol_roc_nt

class NseDbOpenCloseData(db.Model):
    __tablename__ = 'nsedbopenclosedata'
    id = db.Column(db.Integer, primary_key=True)
    open_val = db.Column(db.Text())
    close_val = db.Column(db.Text())
    current_val = db.Column(db.Text())
    txttoday_date = db.Column(db.Text())
    expiry_dates = db.Column(db.Text())

    def __init__(self, open_val, close_val, current_val, txttoday_date,expiry_dates):
        self.open_val = open_val
        self.close_val = close_val
        self.current_val = current_val
        self.txttoday_date = txttoday_date
        self.expiry_dates = expiry_dates

def closest_value(input_list, input_value):
    if(len(input_list) != 0):
        arr = np.asarray(input_list)
        i = (np.abs(arr - input_value)).argmin()
        return arr[i]
    else:
        return ""

def dataenter(sheet,actual_data,strike_value,value,other,expiry_dates):
    global strike_values
    global strike_values1 
    global strike_values2 
    global strike_values3 
    global strike_values4
    global strike_values5
    global strike_values6
    global strike_values7
    global strike_values8
    global strike_values9
    global strike_values10
    global strike_values11
    global udelying_values
    strike_values = []
    strike_values1 = []
    strike_values2 = []
    strike_values3 = []
    strike_values4 = []
    strike_values5 = []
    strike_values6 = []
    strike_values7 = []
    strike_values8 = []
    strike_values9 = []
    strike_values10 = []
    strike_values11 = []
    udelying_values = []
    lat_row_time = ''
    today = date.today() 
    rowdata1 = NseDbDailyData.query.filter_by(txtcurrent_date=str(today.strftime("%d-%m-%Y"))).first()
    if(rowdata1 != None):
        row_num = rowdata1.id
        lat_row_time =  rowdata1.str_time
    else:
        row_num = 0
    c_rocoi = 0
    c_rov = 0
    c_roi = 0
    c_roiv = 0
    c_roltp = 0
    c_nt = 0
    c_ront = 0
    c_ltp_coi = 0
    c_roc_ltp_coi = 0
    c_coi_nt = 0
    c_rocoi_nt = 0
    c_ltp_vlm = 0
    c_roltp_vlm = 0
    c_roc_vol_roc_nt = 0
    roc_c_roc_vol_roc_nt = 0
    c_roltp_vlm = 0
    p_rov = 0
    p_rocoi = 0
    p_nt = 0
    p_ront = 0
    p_ltp_vlm = 0
    p_roi = 0
    p_roiv = 0
    p_roltp = 0
    p_ltp_vlm = 0
    p_roltp_vlm = 0
    p_coi_nt = 0
    p_ltp_coi = 0
    p_roc_ltp_coi = 0
    p_rocoi_nt = 0
    p_roc_vol_roc_nt = 0
    roc_p_roc_vol_roc_nt = 0
    counter = 1
    if(row_num != 0):
        row_data =  rowdata1
        lat_row_time = rowdata1.str_time
    for info in actual_data:
        if(row_num == 0):
            data = NseDbDailyData(str(info["Time"]),str(info["C_OI"]),str(c_roi),str(info["C_CH_OI"]),str(c_rocoi),str(info["C_T_Volume"]),str(c_rov),str(info["C_IV"]),str(c_roiv),str(info["C_LTP"]),str(c_roltp),str(c_nt),str(c_ront),str(c_ltp_vlm),str(c_roltp_vlm),str(info["C_CHG"]),str(c_coi_nt),str(c_rocoi_nt),str(c_ltp_coi),str(c_roc_ltp_coi),str(info["C_B_QTY"]),str(info["C_B_Price"]),str(info["C_Ask_Price"]),str(info["C_Ask_QTY"]),str(info["SP"]),str(info["P_B_QTY"]),str(info["P_B_Price"]),str(info["P_Ask_QTY"]),str(info["P_Ask_Price"]),str(info["P_CHG"]),str(info["P_LTP"]),str(p_roltp),str(p_nt),str(p_ront),str(p_ltp_vlm),str(p_roltp_vlm),str(info["P_IV"]),str(p_roiv),str(info["P_T_Volume"]),str(p_rov),str(info["P_CH_OI"]),str(p_rocoi),str(info["P_OI"]),str(p_roi),str(p_coi_nt),str(p_rocoi_nt),str(p_ltp_coi),str(p_roc_ltp_coi),str(today.strftime("%d-%m-%Y")),str(c_roc_vol_roc_nt),str(roc_c_roc_vol_roc_nt),str(p_roc_vol_roc_nt),str(roc_p_roc_vol_roc_nt))
            db.session.add(data)
            db.session.commit()
        else:
            if(len(info) != 0):
                sql_query = NseDbDailyData.query.filter_by(txtcurrent_date=today.strftime("%d-%m-%Y")).all()
                sql_query_list = []
                for sql in sql_query:
                    sql_query_list.append({"str_time":sql.str_time,"c_oi":sql.c_oi,"c_roc_oi":sql.c_roc_oi,"c_chng_in_oi":sql.c_chng_in_oi,"c_roc_chng_in_oi":sql.c_roc_chng_in_oi,"c_volume":sql.c_volume,"c_roc_volume":sql.c_roc_volume,"c_iv":sql.c_iv,"c_roc_iv":sql.c_roc_iv,"c_ltp":sql.c_ltp,"c_roc_ltp":sql.c_roc_ltp,"c_nt":sql.c_nt,"c_roc_nt":sql.c_roc_nt,"c_ltp_vl":sql.c_ltp_vl,"c_roc_ltp_vl":sql.c_roc_ltp_vl,"c_chng":sql.c_chng,"c_oi_nt":sql.c_oi_nt,"c_roc_oi_nt":sql.c_roc_oi_nt,"c_ltp_coi":sql.c_ltp_coi,"c_roc_ltp_coi":sql.c_roc_ltp_coi,"c_bid_qty":sql.c_bid_qty,"c_bid_price":sql.c_bid_price,"c_ask_price":sql.c_ask_price,"c_ask_qty":sql.c_ask_qty,"strike_price":sql.strike_price,"p_bid_qty":sql.p_bid_qty,"p_bid_price":sql.p_bid_price,"p_ask_price":sql.p_ask_price,"p_ask_qty":sql.p_ask_qty,"p_chng":sql.p_chng,"p_ltp":sql.p_ltp,"p_roc_ltp":sql.p_roc_ltp,"p_nt":sql.p_nt,"p_roc_nt":sql.p_roc_nt,"p_ltp_vl":sql.p_ltp_vl,"p_roc_ltp_vl":sql.p_roc_ltp_vl,"p_iv":sql.p_iv,"p_roc_iv":sql.p_roc_iv,"p_volume":sql.p_volume,"p_roc_volume":sql.p_roc_volume,"p_chng_in_oi":sql.p_chng_in_oi,"p_roc_chng_in_oi":sql.p_roc_chng_in_oi,"p_oi":sql.p_oi,"p_roc_oi":sql.p_roc_oi,"p_oi_nt":sql.p_oi_nt,"p_roc_oi_nt":sql.p_roc_oi_nt,"p_ltp_coi":sql.p_ltp_coi,"p_roc_ltp_coi":sql.p_roc_ltp_coi,"txtcurrent_date":sql.txtcurrent_date,"c_roc_vol_roc_nt":sql.c_roc_vol_roc_nt,"roc_c_roc_vol_roc_nt":sql.roc_c_roc_vol_roc_nt,"p_roc_vol_roc_nt":sql.p_roc_vol_roc_nt,"roc_p_roc_vol_roc_nt":sql.roc_p_roc_vol_roc_nt})
                df = pd.DataFrame(sql_query_list)
                df.columns = ['str_Time', 'C_OI', 'C_ROC_OI', 'C_CHNG_IN_OI', 'C_ROC_CHNG_IN_OI', 'C_VOLUME', 'C_ROC_VOLUME','C_IV','C_ROC_IV', 'C_LTP', 'C_ROC_LTP','C_NT','C_ROC_NT','C_LTP_VL','C_ROC_LTP_VL', 'C_CHNG','C_OI_NT','C_ROC_OI_NT','C_LTP_COI','C_ROC_LTP_COI', 'C_BID_QTY','C_BID_PRICE', 'C_ASK_PRICE', 'C_ASK_QTY','STRIKE_PRICE','P_BID_QTY', 'P_BID_PRICE', 'P_ASK_PRICE', 'P_ASK_QTY', 'P_CHNG','P_LTP','P_ROC_LTP','P_NT','P_ROC_NT','P_LTP_VL','P_ROC_LTP_VL', 'P_IV', 'P_ROC_IV', 'P_VOLUME', 'P_ROC_VOLUME', 'P_CHNG_IN_OI', 'P_ROC_CHNG_IN_OI', 'P_OI','P_ROC_OI','P_OI_NT','P_ROC_OI_NT','P_LTP_COI','P_ROC_LTP_COI',"txtcurrent_date","C_ROC_VOL_ROC_NT","ROC_C_ROC_VOL_ROC_NT","P_ROC_VOL_ROC_NT","ROC_P_ROC_VOL_ROC_NT"]
                if(df.empty == False):
                    lists =df.loc[(df['STRIKE_PRICE'] == str(info["SP"])) & (df['str_Time'] == str(lat_row_time))]
                    print(lists)
                    if(lists.empty == False):
                        c_roi = int(float(lists["C_OI"].values[0])) - int(info["C_OI"])
                        c_rocoi = int(float(lists["C_CHNG_IN_OI"].values[0])) - int(info["C_CH_OI"])
                        c_rov = int(info["C_T_Volume"]) - (int(float(lists["C_VOLUME"].values[0])) if len(lists["C_VOLUME"].values[0]) != 0 else 0 )
                        c_roiv = int(info["C_IV"]) - (int(float(lists["C_IV"].values[0])) if len(lists["C_IV"].values[0]) != 0 else 0 )
                        c_roltp = int(info["C_LTP"]) - (int(float(lists["C_LTP"].values[0])) if len(lists["C_LTP"].values[0]) != 0 else 0 )
                        try:
                            c_nt = float(format((c_rov/float(info["C_LTP"])), ".2f"))
                            c_ront = int(c_nt) - (int(float(lists["C_ROC_NT"].values[0])) if len(lists["C_ROC_NT"].values[0]) != 0 else 0 )
                        except:
                            c_nt = 0
                            c_ront = int(c_nt) - (int(float(lists["C_ROC_NT"].values[0])) if len(lists["C_ROC_NT"].values[0]) != 0 else 0 )
                        try:    
                            c_coi_nt = float(format((float(c_rocoi/c_ront)), ".2f"))
                            c_rocoi_nt = int(c_coi_nt)  - (int(float(lists["C_OI_NT"].values[0])) if len(lists["C_OI_NT"].values[0]) != 0 else 0 )
                        except:
                            c_coi_nt = 0
                            c_rocoi_nt = int(c_coi_nt)  - (int(float(lists["C_OI_NT"].values[0])) if len(lists["C_OI_NT"].values[0]) != 0 else 0 )
                        try:    
                            c_roc_vol_roc_nt = float(format((float(c_rov/c_ront)), ".2f"))
                            roc_c_roc_vol_roc_nt = int(c_roc_vol_roc_nt)  - (int(float(lists["ROC_C_ROC_VOL_ROC_NT"].values[0])) if len(lists["ROC_C_ROC_VOL_ROC_NT"].values[0]) != 0 else 0 )
                        except:
                            c_roc_vol_roc_nt = 0
                            roc_c_roc_vol_roc_nt = int(c_roc_vol_roc_nt)  - (int(float(lists["ROC_C_ROC_VOL_ROC_NT"].values[0])) if len(lists["ROC_C_ROC_VOL_ROC_NT"].values[0]) != 0 else 0 )
                        c_ltp_vlm = float(float(c_roltp) * float(c_rov))
                        c_roltp_vlm = int(c_ltp_vlm) - (int(float(lists["C_LTP_VL"].values[0])) if len(lists["C_LTP_VL"].values[0]) != 0 else 0 )
                        c_ltp_coi = float(float(info["C_LTP"]) * int(info["C_OI"]))
                        c_roc_ltp_coi = int(c_ltp_coi) - (int(float(lists["C_ROC_LTP_COI"].values[0])) if len(lists["C_ROC_LTP_COI"].values[0]) != 0 else 0 )
                        p_roi = int(info["P_OI"]) - (int(float(lists["P_OI"].values[0])) if len(lists["P_OI"].values[0]) != 0 else 0 )
                        p_rocoi = int(info["P_CH_OI"]) - (int(float(lists["P_ROC_CHNG_IN_OI"].values[0])) if len(lists["P_ROC_CHNG_IN_OI"].values[0]) != 0 else 0 )
                        p_rov = int(info["P_T_Volume"]) - (int(float(lists["P_VOLUME"].values[0])) if len(lists["P_VOLUME"].values[0]) != 0 else 0 )
                        p_roiv = int(info["P_IV"]) - (int(float(lists["P_IV"].values[0])) if len(lists["P_IV"].values[0]) != 0 else 0) 
                        p_roltp = int(info["P_LTP"]) - (int(float(lists["P_LTP"].values[0]))) 
                        try:
                            p_nt = float(format((p_rov/float(info["P_LTP"])), ".2f"))
                            p_ront = int(p_nt) - (int(float(lists["P_ROC_NT"].values[0])) if lists["P_ROC_NT"].values[0] != 'nan' else 0)
                        except:
                            p_nt = 0
                            p_ront = int(p_nt) - (int(float(lists["P_ROC_NT"].values[0])) if lists["P_ROC_NT"].values[0] != 'nan' else 0) 
                        try:
                            p_coi_nt = float(format((float(p_rocoi/p_ront)), ".2f"))
                            p_rocoi_nt = int(p_coi_nt)  - (int(float(lists["P_ROC_NT"].values[0])) if lists["P_ROC_NT"].values[0] != 'nan' else 0 )
                        except:   
                            p_coi_nt = 0
                            p_rocoi_nt = int(p_coi_nt)  - (int(float(lists["P_ROC_NT"].values[0])) if lists["P_ROC_NT"].values[0] != 'nan' else 0 )
                        try:    
                            p_roc_vol_roc_nt = float(format((float(p_rov/p_ront)), ".2f"))
                            roc_p_roc_vol_roc_nt = int(p_roc_vol_roc_nt)  - (int(float(lists["ROC_P_ROC_VOL_ROC_NT"].values[0])) if len(lists["ROC_P_ROC_VOL_ROC_NT"].values[0]) != 0 else 0 )
                        except:
                            p_roc_vol_roc_nt = 0
                            roc_p_roc_vol_roc_nt = int(p_roc_vol_roc_nt)  - (int(float(lists["ROC_P_ROC_VOL_ROC_NT"].values[0])) if len(lists["ROC_P_ROC_VOL_ROC_NT"].values[0]) != 0 else 0 )
                        p_ltp_vlm = float(float(p_roltp) * float(p_rov))
                        p_ltp_coi = float(float(info["P_LTP"]) * int(info["P_OI"]))
                        p_roc_ltp_coi = int(p_ltp_coi) - (int(float(lists["P_ROC_LTP_COI"].values[0])) if lists["P_ROC_LTP_COI"].values[0] != 'nan' else 0 )
                        p_roltp_vlm = int(p_ltp_vlm) - (int(float(lists["P_LTP_VL"].values[0])) if lists["P_LTP_VL"].values[0] != 'nan' else 0) 
                        print("here to enter")
                        data = NseDbDailyData(str(info["Time"]),str(info["C_OI"]),str(c_roi),str(info["C_CH_OI"]),str(c_rocoi),str(info["C_T_Volume"]),str(c_rov),str(info["C_IV"]),str(c_roiv),str(info["C_LTP"]),str(c_roltp),str(c_nt),str(c_ront),str(c_ltp_vlm),str(c_roltp_vlm),str(info["C_CHG"]),str(c_coi_nt),str(c_rocoi_nt),str(c_ltp_coi),str(c_roc_ltp_coi),str(info["C_B_QTY"]),str(info["C_B_Price"]),str(info["C_Ask_Price"]),str(info["C_Ask_QTY"]),str(info["SP"]),str(info["P_B_QTY"]),str(info["P_B_Price"]),str(info["P_Ask_QTY"]),str(info["P_Ask_Price"]),str(info["P_CHG"]),str(info["P_LTP"]),str(p_roltp),str(p_nt),str(p_ront),str(p_ltp_vlm),str(p_roltp_vlm),str(info["P_IV"]),str(p_roiv),str(info["P_T_Volume"]),str(p_rov),str(info["P_CH_OI"]),str(p_rocoi),str(info["P_OI"]),str(p_roi),str(p_coi_nt),str(p_rocoi_nt),str(p_ltp_coi),str(p_roc_ltp_coi),str(today.strftime("%d-%m-%Y")),str(c_roc_vol_roc_nt),str(roc_c_roc_vol_roc_nt),str(p_roc_vol_roc_nt),str(roc_p_roc_vol_roc_nt))
                        db.session.add(data)
                        db.session.commit()
                        print("here to exit")
                        
    today = date.today() 
    prev_val = NseDbOpenCloseData.query.filter_by(txttoday_date=today.strftime("%d-%m-%Y")).first()
    if(prev_val!=None):
        if(len(prev_val.current_val) != 0):
            prev_strike_val = prev_val.current_val
    else:
        prev_strike_val = 0
    if(value ==0):
        value = prev_strike_val
    val=closest_value(strike_value,round(value, 0))
    if(len(str(val)) == 0):
        val = int(prev_strike_val)
    else:
        val = int(val)
    last_2_digits = int(str(val)[-2:])
    under_val = 0
    if(last_2_digits < 100):
        under_val = int(val - last_2_digits)
    valueobj = NseDbOpenCloseData.query.filter(NseDbOpenCloseData.txttoday_date == str(today.strftime("%d-%m-%Y"))).first()
    if(valueobj != None):
        valueobj.current_val = str(val)
        valueobj.expiry_dates = str(expiry_dates)
        db.session.flush()
        db.session.commit()
    else:
        data = NseDbOpenCloseData(str(value),'','',str(today.strftime("%d-%m-%Y")),expiry_dates)
        db.session.add(data)
        db.session.commit()  
    udelying_values = [under_val-500,under_val-400,under_val-300,under_val-200,under_val-100,val,under_val+100,under_val+200,under_val+300,under_val+400,under_val+500]
    today = date.today()
    sql_query = NseDbDailyData.query.filter_by(txtcurrent_date=today.strftime("%d-%m-%Y")).all()
    sql_query_list = []
    for sql in sql_query:
        sql_query_list.append({"str_time":sql.txtcurrent_date,"c_oi":sql.c_oi,"c_roc_oi":sql.c_roc_oi,"c_chng_in_oi":sql.c_chng_in_oi,"c_roc_chng_in_oi":sql.c_roc_chng_in_oi,"c_volume":sql.c_volume,"c_roc_volume":sql.c_roc_volume,"c_iv":sql.c_iv,"c_roc_iv":sql.c_roc_iv,"c_ltp":sql.c_ltp,"c_roc_ltp":sql.c_roc_ltp,"c_nt":sql.c_nt,"c_roc_nt":sql.c_roc_nt,"c_ltp_vl":sql.c_ltp_vl,"c_roc_ltp_vl":sql.c_roc_ltp_vl,"c_chng":sql.c_chng,"c_oi_nt":sql.c_oi_nt,"c_roc_oi_nt":sql.c_roc_oi_nt,"c_ltp_coi":sql.c_ltp_coi,"c_roc_ltp_coi":sql.c_roc_ltp_coi,"c_bid_qty":sql.c_bid_qty,"c_bid_price":sql.c_bid_price,"c_ask_price":sql.c_ask_price,"c_ask_qty":sql.c_ask_qty,"strike_price":sql.strike_price,"p_bid_qty":sql.p_bid_qty,"p_bid_price":sql.p_bid_price,"p_ask_price":sql.p_ask_price,"p_ask_qty":sql.p_ask_qty,"p_chng":sql.p_chng,"p_ltp":sql.p_ltp,"p_roc_ltp":sql.p_roc_ltp,"p_nt":sql.p_nt,"p_roc_nt":sql.p_roc_nt,"p_ltp_vl":sql.p_ltp_vl,"p_roc_ltp_vl":sql.p_roc_ltp_vl,"p_iv":sql.p_iv,"p_roc_iv":sql.p_roc_iv,"p_volume":sql.p_volume,"p_roc_volume":sql.p_roc_volume,"p_chng_in_oi":sql.p_chng_in_oi,"p_roc_chng_in_oi":sql.p_roc_chng_in_oi,"p_oi":sql.p_oi,"p_roc_oi":sql.p_roc_oi,"p_oi_nt":sql.p_oi_nt,"p_roc_oi_nt":sql.p_roc_oi_nt,"p_ltp_coi":sql.p_ltp_coi,"p_roc_ltp_coi":sql.p_roc_ltp_coi,"txtcurrent_date":sql.txtcurrent_date,"c_roc_vol_roc_nt":sql.c_roc_vol_roc_nt,"roc_c_roc_vol_roc_nt":sql.roc_c_roc_vol_roc_nt,"p_roc_vol_roc_nt":sql.p_roc_vol_roc_nt,"roc_p_roc_vol_roc_nt":sql.roc_p_roc_vol_roc_nt})
    df = pd.DataFrame(sql_query_list)
    df.columns = ['str_Time', 'C_OI', 'C_ROC_OI', 'C_CHNG_IN_OI', 'C_ROC_CHNG_IN_OI', 'C_VOLUME', 'C_ROC_VOLUME','C_IV','C_ROC_IV', 'C_LTP', 'C_ROC_LTP','C_NT','C_ROC_NT','C_LTP_VL','C_ROC_LTP_VL', 'C_CHNG','C_OI_NT','C_ROC_OI_NT','C_LTP_COI','C_ROC_LTP_COI', 'C_BID_QTY','C_BID_PRICE', 'C_ASK_PRICE', 'C_ASK_QTY','STRIKE_PRICE','P_BID_QTY', 'P_BID_PRICE', 'P_ASK_PRICE', 'P_ASK_QTY', 'P_CHNG','P_LTP','P_ROC_LTP','P_NT','P_ROC_NT','P_LTP_VL','P_ROC_LTP_VL', 'P_IV', 'P_ROC_IV', 'P_VOLUME', 'P_ROC_VOLUME', 'P_CHNG_IN_OI', 'P_ROC_CHNG_IN_OI', 'P_OI','P_ROC_OI','P_OI_NT','P_ROC_OI_NT','P_LTP_COI','P_ROC_LTP_COI',"txtcurrent_date","C_ROC_VOL_ROC_NT","ROC_C_ROC_VOL_ROC_NT","P_ROC_VOL_ROC_NT","ROC_P_ROC_VOL_ROC_NT"]
    if(df.empty == False):
        for t in df.str_Time.unique():
            for i,un in enumerate(udelying_values):
                lists = df.loc[(df['str_Time'] == str(t)) & (df['STRIKE_PRICE'] == str(un))]
                if(lists.empty == False):
                    if(i==0):
                        strike_values1.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==1):
                        strike_values2.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==2):
                        strike_values3.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==3):
                        strike_values4.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==4):
                        strike_values5.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==5):
                        strike_values6.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==6):
                        strike_values7.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==7):
                        strike_values8.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==8):
                        strike_values9.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==9):
                        strike_values10.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
                    elif(i==10):
                        strike_values11.append({"time":t.replace(",",":"),"C_OI":lists["C_OI"].values[0],"C_ROC_OI":lists["C_ROC_OI"].values[0],"C_CHNG_IN_OI":lists["C_CHNG_IN_OI"].values[0],"C_ROC_CHNG_IN_OI":lists["C_ROC_CHNG_IN_OI"].values[0],"C_VOLUME":lists["C_VOLUME"].values[0],"C_ROC_VOLUME":lists["C_ROC_VOLUME"].values[0],"C_IV":lists["C_IV"].values[0],"C_ROC_IV":lists["C_ROC_IV"].values[0],"C_LTP":lists["C_LTP"].values[0],"C_ROC_LTP":lists["C_ROC_LTP"].values[0],"C_NT":lists["C_NT"].values[0],"C_ROC_NT":lists["C_ROC_NT"].values[0],"C_LTP_VL":lists["C_LTP_VL"].values[0],"C_ROC_LTP_VL":lists["C_ROC_LTP_VL"].values[0],"C_CHNG":lists["C_CHNG"].values[0],"P_CHNG":lists["P_CHNG"].values[0],"P_LTP":lists["P_LTP"].values[0],"P_ROC_LTP":lists["P_ROC_LTP"].values[0],"P_NT":lists["P_NT"].values[0],"P_ROC_NT":lists["P_ROC_NT"].values[0],"P_LTP_VL":lists["P_LTP_VL"].values[0],"P_ROC_LTP_VL":lists["P_ROC_LTP_VL"].values[0],"P_IV":lists["P_IV"].values[0],"P_ROC_IV":lists["P_ROC_IV"].values[0],"P_VOLUME":lists["P_VOLUME"].values[0],"P_ROC_VOLUME":lists["P_ROC_VOLUME"].values[0],"P_CHNG_IN_OI":lists["P_CHNG_IN_OI"].values[0],"P_ROC_CHNG_IN_OI":lists["P_ROC_CHNG_IN_OI"].values[0],"P_OI":lists["P_OI"].values[0],"P_ROC_OI":lists["P_ROC_OI"].values[0],"C_OI_NT":lists["C_OI_NT"].values[0],"C_ROC_OI_NT":lists["C_ROC_OI_NT"].values[0],"P_OI_NT":lists["P_OI_NT"].values[0],"P_ROC_OI_NT":lists["P_ROC_OI_NT"].values[0],"C_LTP_COI":lists["C_LTP_COI"].values[0],"C_ROC_LTP_COI":lists["C_ROC_LTP_COI"].values[0],"P_LTP_COI":lists["P_LTP_COI"].values[0],"P_ROC_LTP_COI":lists["P_ROC_LTP_COI"].values[0],"C_ROC_VOL_ROC_NT":lists["C_ROC_VOL_ROC_NT"].values[0],"ROC_C_ROC_VOL_ROC_NT":lists["ROC_C_ROC_VOL_ROC_NT"].values[0],"P_ROC_VOL_ROC_NT":lists["P_ROC_VOL_ROC_NT"].values[0],"ROC_P_ROC_VOL_ROC_NT":lists["ROC_P_ROC_VOL_ROC_NT"].values[0]})
    return strike_values1

@app.route('/')
def home():
    actual_data = [{'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 0, 'C_B_Price': 0, 'C_Ask_Price': 8465, 'C_Ask_QTY': 50, 'SP': 11000, 'P_B_QTY': 750, 'P_B_Price': 20.05, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 3.5}, {'Time': '11,26', 'C_OI': 75, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 0, 'C_B_Price': 0, 'C_Ask_Price': 7205.25, 'C_Ask_QTY': 200, 'SP': 11500, 'P_B_QTY': 14750, 'P_B_Price': 6.75, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 136.5}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 0, 'C_B_Price': 0, 'C_Ask_Price': 7620, 'C_Ask_QTY': 50, 'SP': 12000, 'P_B_QTY': 50, 'P_B_Price': 156, 'P_Ask_QTY': 50, 'P_Ask_Price': 173.95, 'P_CHG': -15, 'P_LTP': 155, 'P_IV': 30.77, 'P_T_Volume': 1, 'P_CH_OI': 0, 'P_OI': 31}, {'Time': '11,26', 'C_OI': 5, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 3301.4, 'C_Ask_Price': 3877.7, 'C_Ask_QTY': 1750, 'SP': 13950, 'P_B_QTY': 5100, 'P_B_Price': 3.6, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0},
    {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 0, 'C_B_Price': 0, 'C_Ask_Price': 5130, 'C_Ask_QTY': 50, 'SP': 14000, 'P_B_QTY': 100, 'P_B_Price': 120.05, 'P_Ask_QTY': 50, 'P_Ask_Price': 128, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 179}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 3182.05, 'C_Ask_Price': 3869, 'C_Ask_QTY': 1750, 'SP': 14050, 'P_B_QTY': 900, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 3151.1, 'C_Ask_Price': 3869.2, 'C_Ask_QTY': 1750, 'SP': 14100, 'P_B_QTY': 5000, 'P_B_Price': 3.9, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500,
    'C_B_Price': 3185.55, 'C_Ask_Price': 3814.6, 'C_Ask_QTY': 1750, 'SP': 14150, 'P_B_QTY': 3100, 'P_B_Price': 4.3, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 3138.3, 'C_Ask_Price': 3796.9, 'C_Ask_QTY': 1750, 'SP': 14200, 'P_B_QTY': 3100, 'P_B_Price': 4.85, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY':
    3250, 'C_B_Price': 3017.1, 'C_Ask_Price': 3705.55, 'C_Ask_QTY': 1750, 'SP': 14250, 'P_B_QTY': 3100, 'P_B_Price': 5.6, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 3250, 'C_B_Price': 2964.9, 'C_Ask_Price': 3650.8, 'C_Ask_QTY': 1750, 'SP': 14300, 'P_B_QTY': 3100, 'P_B_Price': 6.3, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 6, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 3093.35, 'C_Ask_Price': 3338.85, 'C_Ask_QTY': 1000, 'SP': 14350, 'P_B_QTY': 1900, 'P_B_Price': 3.05, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI':
    0, 'P_OI': 27}, {'Time': '11,26', 'C_OI': 1, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0,
    'C_B_QTY': 1500, 'C_B_Price': 2951, 'C_Ask_Price': 3320.1, 'C_Ask_QTY': 1500, 'SP': 14400, 'P_B_QTY': 150, 'P_B_Price': 5.3, 'P_Ask_QTY': 100, 'P_Ask_Price': 5.95, 'P_CHG': 0.75, 'P_LTP': 5.8, 'P_IV': 36.57, 'P_T_Volume':
    53, 'P_CH_OI': -33, 'P_OI': 180}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 2901.05, 'C_Ask_Price': 3259, 'C_Ask_QTY': 1000, 'SP': 14450, 'P_B_QTY': 2500, 'P_B_Price': 3.05, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 17}, {'Time': '11,26', 'C_OI': 2816, 'C_CH_OI': 0, 'C_T_Volume': 20, 'C_IV': 0, 'C_LTP': 3085.15, 'C_CHG': -74.54999999999973, 'C_B_QTY': 50, 'C_B_Price': 3024.8, 'C_Ask_Price': 3044.95, 'C_Ask_QTY': 50, 'SP': 14500, 'P_B_QTY': 50, 'P_B_Price': 6, 'P_Ask_QTY': 150, 'P_Ask_Price': 6.3, 'P_CHG': 0.15000000000000036, 'P_LTP': 5.9, 'P_IV': 35.55, 'P_T_Volume': 175, 'P_CH_OI': -81, 'P_OI': 7773}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 2803.75, 'C_Ask_Price': 3156, 'C_Ask_QTY': 2750, 'SP': 14550, 'P_B_QTY': 3700, 'P_B_Price': 3.05, 'P_Ask_QTY': 0,
    'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 10}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price':
    2702.55, 'C_Ask_Price': 3267.95, 'C_Ask_QTY': 1750, 'SP': 14600, 'P_B_QTY': 600, 'P_B_Price': 0.25, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2659.4, 'C_Ask_Price': 3233.3, 'C_Ask_QTY': 1750, 'SP': 14650, 'P_B_QTY': 600, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time':
    '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 2345.4, 'C_Ask_Price': 2989.55, 'C_Ask_QTY': 1500, 'SP': 14700, 'P_B_QTY': 1800, 'P_B_Price': 0.7, 'P_Ask_QTY': 700, 'P_Ask_Price': 2.6, 'P_CHG': 0, 'P_LTP': 2, 'P_IV': 47.53, 'P_T_Volume': 1, 'P_CH_OI': 0, 'P_OI': 1}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2568.45, 'C_Ask_Price': 3124.7, 'C_Ask_QTY': 1750, 'SP': 14750, 'P_B_QTY': 600, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI':
    0}, {'Time': '11,26', 'C_OI': 30, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY':
    100, 'C_B_Price': 2700.7, 'C_Ask_Price': 2798.6, 'C_Ask_QTY': 100, 'SP': 14800, 'P_B_QTY': 200, 'P_B_Price': 5.8, 'P_Ask_QTY': 200, 'P_Ask_Price': 6.45, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 1789}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 2530.95, 'C_Ask_Price': 2920.7, 'C_Ask_QTY': 1500, 'SP': 14850, 'P_B_QTY': 1500, 'P_B_Price': 16.8, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 10408, 'C_CH_OI': 5, 'C_T_Volume': 56, 'C_IV': 0, 'C_LTP': 2550, 'C_CHG': -116.80000000000018, 'C_B_QTY': 50, 'C_B_Price': 2536, 'C_Ask_Price': 2544.85, 'C_Ask_QTY': 100, 'SP': 15000, 'P_B_QTY': 50, 'P_B_Price': 7.3, 'P_Ask_QTY': 1200, 'P_Ask_Price': 7.5, 'P_CHG': -0.25, 'P_LTP': 7.35, 'P_IV': 31.08, 'P_T_Volume': 708, 'P_CH_OI': -126, 'P_OI': 23189}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2286.95, 'C_Ask_Price': 2768.9, 'C_Ask_QTY': 1750, 'SP': 15050, 'P_B_QTY': 400, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2248.35, 'C_Ask_Price': 2711.9,
    'C_Ask_QTY': 1750, 'SP': 15100, 'P_B_QTY': 400, 'P_B_Price': 0.25, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0,
    'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2198.6, 'C_Ask_Price': 2652.15, 'C_Ask_QTY': 1750, 'SP': 15150, 'P_B_QTY': 500, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2148, 'C_Ask_Price': 2604.75, 'C_Ask_QTY': 1750, 'SP': 15200, 'P_B_QTY': 500, 'P_B_Price': 0.25, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI':
    0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 2101.15, 'C_Ask_Price': 2545.2, 'C_Ask_QTY': 1750, 'SP': 15250, 'P_B_QTY': 400, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 135, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1550, 'C_B_Price': 2114.75, 'C_Ask_Price': 2289.5, 'C_Ask_QTY': 50, 'SP': 15300, 'P_B_QTY': 300, 'P_B_Price': 8.15, 'P_Ask_QTY': 300, 'P_Ask_Price': 8.3, 'P_CHG': 0.29999999999999893, 'P_LTP': 8.2, 'P_IV': 28.31, 'P_T_Volume': 528, 'P_CH_OI': 12, 'P_OI': 3709}, {'Time': '11,26', 'C_OI': 5, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500,
    'C_B_Price': 2063.7, 'C_Ask_Price': 2267.85, 'C_Ask_QTY': 1550, 'SP': 15350, 'P_B_QTY': 300, 'P_B_Price': 6.3,
    'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 28}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 1959.3, 'C_Ask_Price': 2383.35, 'C_Ask_QTY': 1750, 'SP': 15400, 'P_B_QTY': 3600, 'P_B_Price': 0.3, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY':
    1750, 'C_B_Price': 1916.8, 'C_Ask_Price': 2328.95, 'C_Ask_QTY': 1750, 'SP': 15450, 'P_B_QTY': 400, 'P_B_Price': 0.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 150, 'C_B_Price': 2026.75, 'C_Ask_Price': 2158.9, 'C_Ask_QTY': 1500, 'SP': 15500, 'P_B_QTY': 1850, 'P_B_Price': 2, 'P_Ask_QTY': 50, 'P_Ask_Price': 2.15, 'P_CHG': 0.10000000000000009, 'P_LTP': 2.2, 'P_IV': 35.1, 'P_T_Volume': 426, 'P_CH_OI': 206, 'P_OI': 1335}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1921.85, 'C_Ask_Price': 2105.65, 'C_Ask_QTY': 1500, 'SP': 15550, 'P_B_QTY': 600, 'P_B_Price': 1.05, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 1, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1873.75, 'C_Ask_Price': 2053.75, 'C_Ask_QTY': 1500,
    'SP': 15600, 'P_B_QTY': 400, 'P_B_Price': 2.55, 'P_Ask_QTY': 50, 'P_Ask_Price': 2.65, 'P_CHG': -0.15000000000000036, 'P_LTP': 2.55, 'P_IV': 34.52, 'P_T_Volume': 293, 'P_CH_OI': 15, 'P_OI': 589}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1854.95, 'C_Ask_Price': 1947.3, 'C_Ask_QTY': 1500, 'SP': 15650, 'P_B_QTY': 550, 'P_B_Price': 0.7, 'P_Ask_QTY': 200, 'P_Ask_Price': 0.75, 'P_CHG': 0.09999999999999998, 'P_LTP': 0.75, 'P_IV': 80.85, 'P_T_Volume': 325, 'P_CH_OI': 26, 'P_OI': 196}, {'Time': '11,26', 'C_OI': 2, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 100, 'C_B_Price': 1798.75, 'C_Ask_Price': 1887.05, 'C_Ask_QTY': 1500, 'SP': 15700, 'P_B_QTY': 1850, 'P_B_Price': 0.75, 'P_Ask_QTY': 500, 'P_Ask_Price': 0.85, 'P_CHG': 0, 'P_LTP': 0.85, 'P_IV': 79.83, 'P_T_Volume': 1906, 'P_CH_OI': 137, 'P_OI': 17350}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1729.85, 'C_Ask_Price': 1898.4, 'C_Ask_QTY': 1500, 'SP': 15750, 'P_B_QTY': 600, 'P_B_Price': 1.6, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 1572.05, 'C_Ask_Price': 1952.1, 'C_Ask_QTY': 1750, 'SP': 15800, 'P_B_QTY': 50, 'P_B_Price': 7.15, 'P_Ask_QTY': 50, 'P_Ask_Price': 8.95, 'P_CHG': 0.34999999999999964, 'P_LTP': 8, 'P_IV': 26.94, 'P_T_Volume': 20, 'P_CH_OI': 4, 'P_OI': 171}, {'Time': '11,26', 'C_OI': 6, 'C_CH_OI': 0,
    'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1600.5, 'C_Ask_Price': 1780.1, 'C_Ask_QTY': 1550, 'SP': 15850, 'P_B_QTY': 300, 'P_B_Price': 13.7, 'P_Ask_QTY': 250, 'P_Ask_Price': 29.5, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 195}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1550.3, 'C_Ask_Price': 1631.15, 'C_Ask_QTY': 1500, 'SP': 15950, 'P_B_QTY': 400, 'P_B_Price': 0.85, 'P_Ask_QTY': 100, 'P_Ask_Price': 0.9, 'P_CHG': 0.04999999999999993, 'P_LTP': 0.95, 'P_IV': 70.37, 'P_T_Volume': 288, 'P_CH_OI': 44, 'P_OI': 329}, {'Time': '11,26', 'C_OI': 13052, 'C_CH_OI': -15, 'C_T_Volume': 192, 'C_IV': 0, 'C_LTP': 1564.1, 'C_CHG': -126.70000000000005, 'C_B_QTY': 100, 'C_B_Price': 1558.95, 'C_Ask_Price': 1566.2, 'C_Ask_QTY': 100, 'SP': 16000, 'P_B_QTY': 1450, 'P_B_Price': 23.85, 'P_Ask_QTY': 850, 'P_Ask_Price': 24, 'P_CHG': 2.75, 'P_LTP': 23.9, 'P_IV':
    25.01, 'P_T_Volume': 7847, 'P_CH_OI': -113, 'P_OI': 85551}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 1350.7, 'C_Ask_Price': 1693.45, 'C_Ask_QTY': 1750, 'SP': 16050, 'P_B_QTY': 300, 'P_B_Price': 7.1, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 6}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 1327.75, 'C_Ask_Price': 1638.8, 'C_Ask_QTY': 1750, 'SP': 16100, 'P_B_QTY': 50, 'P_B_Price': 9.45, 'P_Ask_QTY': 150, 'P_Ask_Price': 14.9, 'P_CHG':
    0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 78}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1500, 'C_B_Price': 1351.3, 'C_Ask_Price': 1444.15, 'C_Ask_QTY': 1500, 'SP': 16150, 'P_B_QTY': 50, 'P_B_Price': 3.85, 'P_Ask_QTY': 50, 'P_Ask_Price': 7.75, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 51}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1245.1, 'C_Ask_Price': 1513.35, 'C_Ask_QTY': 1750, 'SP': 16200, 'P_B_QTY': 1050, 'P_B_Price': 15.05, 'P_Ask_QTY': 1100, 'P_Ask_Price': 15.75, 'P_CHG': 1.5, 'P_LTP': 15, 'P_IV': 24.18, 'P_T_Volume': 92, 'P_CH_OI': 66, 'P_OI': 167}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1157.6, 'C_Ask_Price': 1463.85, 'C_Ask_QTY': 1750, 'SP': 16250, 'P_B_QTY': 300, 'P_B_Price': 10.8, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1113.4, 'C_Ask_Price': 1414.9, 'C_Ask_QTY': 1750, 'SP': 16300, 'P_B_QTY': 50, 'P_B_Price': 18.85, 'P_Ask_QTY': 50, 'P_Ask_Price': 19.5, 'P_CHG': 2.5500000000000007, 'P_LTP': 19.2, 'P_IV': 23.9, 'P_T_Volume': 372, 'P_CH_OI': 157, 'P_OI': 590}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1063.2, 'C_Ask_Price': 1365.45, 'C_Ask_QTY': 1750, 'SP': 16350, 'P_B_QTY': 300, 'P_B_Price': 11.5, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 1009.85, 'C_Ask_Price': 1311, 'C_Ask_QTY': 1750, 'SP': 16400, 'P_B_QTY': 50, 'P_B_Price': 23.5, 'P_Ask_QTY': 50, 'P_Ask_Price': 23.95, 'P_CHG': 3.6999999999999993, 'P_LTP': 24, 'P_IV': 23.53, 'P_T_Volume': 408, 'P_CH_OI': 235, 'P_OI': 612}, {'Time': '11,26', 'C_OI': 1, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 150, 'C_B_Price': 1075.7, 'C_Ask_Price': 1109.3, 'C_Ask_QTY': 150, 'SP': 16450, 'P_B_QTY': 1450, 'P_B_Price': 8.95, 'P_Ask_QTY': 2050, 'P_Ask_Price': 9.05, 'P_CHG': 0.10000000000000142, 'P_LTP': 9.05, 'P_IV': 24.92, 'P_T_Volume': 1493, 'P_CH_OI': 422, 'P_OI': 840}, {'Time':
    '11,26', 'C_OI': 212, 'C_CH_OI': 12, 'C_T_Volume': 54, 'C_IV': 0, 'C_LTP': 1047.25, 'C_CHG': -141.75, 'C_B_QTY': 150, 'C_B_Price': 1043.9, 'C_Ask_Price': 1052.4, 'C_Ask_QTY': 300, 'SP': 16500, 'P_B_QTY': 3250, 'P_B_Price': 10.25, 'P_Ask_QTY': 2750, 'P_Ask_Price': 10.4, 'P_CHG': 0.25, 'P_LTP': 10.25, 'P_IV': 24.62, 'P_T_Volume': 12317, 'P_CH_OI': 2289, 'P_OI': 17412}, {'Time': '11,26', 'C_OI': 52, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 50, 'C_B_Price': 976, 'C_Ask_Price': 993.5, 'C_Ask_QTY': 3650, 'SP': 16550, 'P_B_QTY': 1500, 'P_B_Price': 1.1, 'P_Ask_QTY': 3100, 'P_Ask_Price': 1.15, 'P_CHG': -0.09999999999999987, 'P_LTP': 1.1, 'P_IV': 46.48, 'P_T_Volume': 8060, 'P_CH_OI': 671, 'P_OI': 4316}, {'Time': '11,26', 'C_OI': 10, 'C_CH_OI': 0, 'C_T_Volume': 1, 'C_IV': 16.25, 'C_LTP': 975, 'C_CHG': -133.45000000000005, 'C_B_QTY': 200, 'C_B_Price':
    948.65, 'C_Ask_Price': 954.55, 'C_Ask_QTY': 50, 'SP': 16600, 'P_B_QTY': 1500, 'P_B_Price': 13.55, 'P_Ask_QTY':
    4300, 'P_Ask_Price': 13.7, 'P_CHG': 1.299999999999999, 'P_LTP': 13.7, 'P_IV': 24.03, 'P_T_Volume': 9675, 'P_CH_OI': 1773, 'P_OI': 13541}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 786.95, 'C_Ask_Price': 1054, 'C_Ask_QTY': 1750, 'SP': 16650, 'P_B_QTY': 100, 'P_B_Price': 41.2, 'P_Ask_QTY': 50, 'P_Ask_Price': 42.2, 'P_CHG': 0, 'P_LTP': 37.45, 'P_IV': 21.92, 'P_T_Volume': 19, 'P_CH_OI': 0, 'P_OI': 17}, {'Time': '11,26', 'C_OI': 3, 'C_CH_OI': 0, 'C_T_Volume': 3, 'C_IV': 22.06, 'C_LTP': 950, 'C_CHG': -51.049999999999955, 'C_B_QTY': 1800, 'C_B_Price': 650.95, 'C_Ask_Price': 1001.25,
    'C_Ask_QTY': 1750, 'SP': 16700, 'P_B_QTY': 100, 'P_B_Price': 46.3, 'P_Ask_QTY': 250, 'P_Ask_Price': 46.55, 'P_CHG': 7.549999999999997, 'P_LTP': 46, 'P_IV': 22.5, 'P_T_Volume': 682, 'P_CH_OI': 184, 'P_OI': 1765}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 686.1, 'C_Ask_Price': 956.1, 'C_Ask_QTY': 1750, 'SP': 16750, 'P_B_QTY': 100, 'P_B_Price': 43.55, 'P_Ask_QTY': 50, 'P_Ask_Price': 56.4, 'P_CHG': 0, 'P_LTP': 45.35, 'P_IV': 21.35, 'P_T_Volume': 1, 'P_CH_OI': 0, 'P_OI': 6}, {'Time': '11,26', 'C_OI': 19, 'C_CH_OI': 7, 'C_T_Volume': 25, 'C_IV': 12.19, 'C_LTP': 774.85, 'C_CHG': -106.85000000000002, 'C_B_QTY': 150, 'C_B_Price': 761.6, 'C_Ask_Price': 765.25, 'C_Ask_QTY': 150, 'SP': 16800, 'P_B_QTY': 1100, 'P_B_Price': 24.95, 'P_Ask_QTY': 50, 'P_Ask_Price': 25.1, 'P_CHG': 3.5, 'P_LTP': 25, 'P_IV': 23.07, 'P_T_Volume': 13357, 'P_CH_OI': 1498, 'P_OI': 10885}, {'Time': '11,26', 'C_OI': 1, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800, 'C_B_Price': 591.55, 'C_Ask_Price': 869.8, 'C_Ask_QTY': 1750, 'SP': 16850, 'P_B_QTY': 100, 'P_B_Price': 60.3, 'P_Ask_QTY': 50, 'P_Ask_Price': 69.75, 'P_CHG': 14.299999999999997, 'P_LTP': 64, 'P_IV': 21.87, 'P_T_Volume': 15, 'P_CH_OI': 8, 'P_OI': 53}, {'Time': '11,26', 'C_OI':
    4, 'C_CH_OI': 0, 'C_T_Volume': 2, 'C_IV': 0, 'C_LTP': 711, 'C_CHG': -141.45000000000005, 'C_B_QTY': 100, 'C_B_Price': 709.35, 'C_Ask_Price': 749.9, 'C_Ask_QTY': 50, 'SP': 16900, 'P_B_QTY': 50, 'P_B_Price': 73.15, 'P_Ask_QTY': 100, 'P_Ask_Price': 73.65, 'P_CHG': 12.650000000000006, 'P_LTP': 73.45, 'P_IV': 22.07, 'P_T_Volume': 355, 'P_CH_OI': 49, 'P_OI': 795}, {'Time': '11,26', 'C_OI': 24, 'C_CH_OI': 20, 'C_T_Volume': 22, 'C_IV': 10.64, 'C_LTP': 628, 'C_CHG': -114.39999999999998, 'C_B_QTY': 200, 'C_B_Price': 627.4, 'C_Ask_Price': 630.2, 'C_Ask_QTY': 200, 'SP': 16950, 'P_B_QTY': 2250, 'P_B_Price': 39.15, 'P_Ask_QTY': 350, 'P_Ask_Price': 39.4, 'P_CHG': 6.75, 'P_LTP': 39.3, 'P_IV': 22.5, 'P_T_Volume': 2468, 'P_CH_OI': 293, 'P_OI': 940}, {'Time': '11,26', 'C_OI': 665, 'C_CH_OI': 307, 'C_T_Volume': 797, 'C_IV': 12.34, 'C_LTP': 586.45, 'C_CHG': -117.69999999999993, 'C_B_QTY': 50, 'C_B_Price': 584.05, 'C_Ask_Price': 585.75, 'C_Ask_QTY': 50, 'SP': 17000, 'P_B_QTY': 150, 'P_B_Price': 45.4, 'P_Ask_QTY': 2100, 'P_Ask_Price': 45.6, 'P_CHG': 8.100000000000001, 'P_LTP': 45.5, 'P_IV': 22.19, 'P_T_Volume': 31770, 'P_CH_OI': 2538, 'P_OI': 21181}, {'Time': '11,26', 'C_OI': 28, 'C_CH_OI': 8, 'C_T_Volume': 41, 'C_IV': 17.27, 'C_LTP': 550.15, 'C_CHG': -105.20000000000005, 'C_B_QTY': 200, 'C_B_Price': 541.05, 'C_Ask_Price': 543.5, 'C_Ask_QTY': 200, 'SP': 17050, 'P_B_QTY': 50, 'P_B_Price': 52.6, 'P_Ask_QTY': 1500, 'P_Ask_Price': 52.95, 'P_CHG': 10.650000000000006, 'P_LTP': 52.95, 'P_IV': 22.13, 'P_T_Volume': 2130, 'P_CH_OI': 166, 'P_OI': 987}, {'Time':
    '11,26', 'C_OI': 25, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1750, 'C_B_Price': 263.85, 'C_Ask_Price': 0, 'C_Ask_QTY': 0, 'SP': 17100, 'P_B_QTY': 50, 'P_B_Price': 111.8, 'P_Ask_QTY': 50, 'P_Ask_Price': 112.75, 'P_CHG': 19.64999999999999, 'P_LTP': 110.85, 'P_IV': 21.56, 'P_T_Volume': 366, 'P_CH_OI': 79, 'P_OI': 727}, {'Time': '11,26', 'C_OI': 61, 'C_CH_OI': 3, 'C_T_Volume': 63, 'C_IV': 15.3, 'C_LTP': 459.95, 'C_CHG': -118.40000000000003, 'C_B_QTY': 100, 'C_B_Price': 459.15, 'C_Ask_Price': 461.1, 'C_Ask_QTY': 200,
    'SP': 17150, 'P_B_QTY': 250, 'P_B_Price': 70.1, 'P_Ask_QTY': 1400, 'P_Ask_Price': 70.4, 'P_CHG': 14.25, 'P_LTP': 69.95, 'P_IV': 21.71, 'P_T_Volume': 3292, 'P_CH_OI': 524, 'P_OI': 1457}, {'Time': '11,26', 'C_OI': 654, 'C_CH_OI': 105, 'C_T_Volume': 470, 'C_IV': 16.52, 'C_LTP': 419.6, 'C_CHG': -107, 'C_B_QTY': 350, 'C_B_Price': 420.1, 'C_Ask_Price': 421, 'C_Ask_QTY': 100, 'SP': 17200, 'P_B_QTY': 400, 'P_B_Price': 80.45, 'P_Ask_QTY': 2300, 'P_Ask_Price': 80.8, 'P_CHG': 16.9, 'P_LTP': 80.8, 'P_IV': 21.52, 'P_T_Volume': 20155, 'P_CH_OI': 3676, 'P_OI': 13330}, {'Time': '11,26', 'C_OI': 41, 'C_CH_OI': -5, 'C_T_Volume': 35, 'C_IV': 16.19, 'C_LTP': 381.5, 'C_CHG': -117.80000000000001, 'C_B_QTY': 350, 'C_B_Price': 382, 'C_Ask_Price': 384, 'C_Ask_QTY': 600, 'SP': 17250, 'P_B_QTY': 50, 'P_B_Price': 92.25, 'P_Ask_QTY': 400, 'P_Ask_Price': 92.55, 'P_CHG': 20, 'P_LTP': 92.55, 'P_IV': 21.37,
    'P_T_Volume': 14112, 'P_CH_OI': 5436, 'P_OI': 6740}, {'Time': '11,26', 'C_OI': 952, 'C_CH_OI': 233, 'C_T_Volume': 1527, 'C_IV': 16.43, 'C_LTP': 347, 'C_CHG': -97.85000000000002, 'C_B_QTY': 100, 'C_B_Price': 346.6, 'C_Ask_Price': 347.7, 'C_Ask_QTY': 50, 'SP': 17300, 'P_B_QTY': 50, 'P_B_Price': 106.8, 'P_Ask_QTY': 250, 'P_Ask_Price': 107.05, 'P_CHG': 24.39999999999999, 'P_LTP': 106.6, 'P_IV': 21.34, 'P_T_Volume': 25042, 'P_CH_OI': 1811, 'P_OI': 11764}, {'Time': '11,26', 'C_OI': 2232, 'C_CH_OI': 1512, 'C_T_Volume': 15766, 'C_IV': 21.85, 'C_LTP': 215.4, 'C_CHG': -115.49999999999997, 'C_B_QTY': 150, 'C_B_Price': 215.15, 'C_Ask_Price': 215.55, 'C_Ask_QTY': 50, 'SP': 17350, 'P_B_QTY': 7950, 'P_B_Price': 26.95, 'P_Ask_QTY': 1850, 'P_Ask_Price': 27.05, 'P_CHG': 6, 'P_LTP': 26.85, 'P_IV': 26.15, 'P_T_Volume': 363932, 'P_CH_OI': 3855, 'P_OI': 33287}, {'Time': '11,26', 'C_OI': 16508, 'C_CH_OI': 11166, 'C_T_Volume': 136795, 'C_IV': 22.33, 'C_LTP': 176.55, 'C_CHG': -113.14999999999998, 'C_B_QTY': 250, 'C_B_Price': 176.3, 'C_Ask_Price': 176.7, 'C_Ask_QTY': 150, 'SP': 17400, 'P_B_QTY': 1900, 'P_B_Price': 38.1, 'P_Ask_QTY': 600, 'P_Ask_Price': 38.2, 'P_CHG': 10.350000000000001, 'P_LTP': 38.2, 'P_IV': 25.98, 'P_T_Volume': 818849, 'P_CH_OI': 24140, 'P_OI': 116890}, {'Time': '11,26', 'C_OI': 8319, 'C_CH_OI': 6490, 'C_T_Volume': 120950, 'C_IV': 22.74, 'C_LTP': 141, 'C_CHG': -106.55000000000001, 'C_B_QTY': 50, 'C_B_Price': 140.65, 'C_Ask_Price': 140.95, 'C_Ask_QTY': 350, 'SP': 17450, 'P_B_QTY': 700, 'P_B_Price': 52.55, 'P_Ask_QTY': 1800, 'P_Ask_Price': 52.7, 'P_CHG': 16.4, 'P_LTP': 52.6, 'P_IV': 25.8, 'P_T_Volume': 476952, 'P_CH_OI': 13985, 'P_OI': 42284}, {'Time': '11,26', 'C_OI': 10172, 'C_CH_OI': 6330, 'C_T_Volume': 31971, 'C_IV': 17.01, 'C_LTP': 220.05, 'C_CHG': -82.09999999999997, 'C_B_QTY': 500, 'C_B_Price': 219.3, 'C_Ask_Price': 219.95, 'C_Ask_QTY': 50, 'SP': 17500, 'P_B_QTY': 400, 'P_B_Price': 179.5, 'P_Ask_QTY': 50, 'P_Ask_Price': 179.9, 'P_CHG': 42.849999999999994, 'P_LTP': 179.9, 'P_IV': 21.12, 'P_T_Volume': 51366, 'P_CH_OI': 6046, 'P_OI': 24612}, {'Time': '11,26', 'C_OI': 120, 'C_CH_OI': 68, 'C_T_Volume': 196, 'C_IV': 16.18, 'C_LTP': 263.2, 'C_CHG': -72.35000000000002, 'C_B_QTY': 50, 'C_B_Price': 264.05, 'C_Ask_Price': 266.6, 'C_Ask_QTY': 50, 'SP': 17550, 'P_B_QTY': 50, 'P_B_Price': 268.2, 'P_Ask_QTY': 50, 'P_Ask_Price': 269.9, 'P_CHG': 55.44999999999999, 'P_LTP': 270, 'P_IV': 21.21, 'P_T_Volume': 277, 'P_CH_OI': 64, 'P_OI': 107}, {'Time': '11,26', 'C_OI': 26559, 'C_CH_OI': 5026, 'C_T_Volume': 20663, 'C_IV': 15.36, 'C_LTP': 287.95, 'C_CHG': -70.75, 'C_B_QTY': 50, 'C_B_Price': 287.5, 'C_Ask_Price': 287.95, 'C_Ask_QTY': 50, 'SP': 17600, 'P_B_QTY': 1150, 'P_B_Price': 335, 'P_Ask_QTY': 50, 'P_Ask_Price': 335.5, 'P_CHG': 57.69999999999999,
    'P_LTP': 335, 'P_IV': 20.97, 'P_T_Volume': 20114, 'P_CH_OI': 2451, 'P_OI': 25573}, {'Time': '11,26', 'C_OI': 1548, 'C_CH_OI': 9, 'C_T_Volume': 1351, 'C_IV': 15.21, 'C_LTP': 262.9, 'C_CHG': -66.45000000000005, 'C_B_QTY': 100, 'C_B_Price': 261.85, 'C_Ask_Price': 263.3, 'C_Ask_QTY': 200, 'SP': 17650, 'P_B_QTY': 400, 'P_B_Price': 358.95, 'P_Ask_QTY': 50, 'P_Ask_Price': 360.5, 'P_CHG': 63.700000000000045, 'P_LTP': 361.85, 'P_IV': 21, 'P_T_Volume': 1407, 'P_CH_OI': -211, 'P_OI': 1163}, {'Time': '11,26', 'C_OI': 24772, 'C_CH_OI': 695, 'C_T_Volume': 16874,
    'C_IV': 15.26, 'C_LTP': 238.35, 'C_CHG': -62.349999999999994, 'C_B_QTY': 50, 'C_B_Price': 237.7, 'C_Ask_Price': 237.95, 'C_Ask_QTY': 50, 'SP': 17700, 'P_B_QTY': 50, 'P_B_Price': 384.1, 'P_Ask_QTY': 50, 'P_Ask_Price': 384.8, 'P_CHG': 64.35000000000002, 'P_LTP': 384.05, 'P_IV': 20.9, 'P_T_Volume': 9033, 'P_CH_OI': -247, 'P_OI': 16176}, {'Time': '11,26', 'C_OI': 1856, 'C_CH_OI': 99, 'C_T_Volume': 1042, 'C_IV': 15.23, 'C_LTP': 215.65, 'C_CHG':
    -59.54999999999998, 'C_B_QTY': 100, 'C_B_Price': 216.05, 'C_Ask_Price': 216.7, 'C_Ask_QTY': 100, 'SP': 17750, 'P_B_QTY': 600, 'P_B_Price': 412, 'P_Ask_QTY': 700, 'P_Ask_Price': 413.95, 'P_CHG': 72.89999999999998, 'P_LTP':
    416, 'P_IV': 21.06, 'P_T_Volume': 201, 'P_CH_OI': -45, 'P_OI': 931}, {'Time': '11,26', 'C_OI': 1203, 'C_CH_OI': 236, 'C_T_Volume': 796, 'C_IV': 16.25, 'C_LTP': 151.15, 'C_CHG': -52.25, 'C_B_QTY': 50, 'C_B_Price': 151.3, 'C_Ask_Price': 152.95, 'C_Ask_QTY': 200, 'SP': 17800, 'P_B_QTY': 150, 'P_B_Price': 404.35, 'P_Ask_QTY': 50, 'P_Ask_Price': 406.95, 'P_CHG': 76.55000000000001, 'P_LTP': 405.6, 'P_IV': 21.45, 'P_T_Volume': 102, 'P_CH_OI': -10, 'P_OI': 212}, {'Time': '11,26', 'C_OI': 2330, 'C_CH_OI': 793, 'C_T_Volume': 5608, 'C_IV': 16.91, 'C_LTP': 73.9, 'C_CHG': -44.099999999999994, 'C_B_QTY': 3200, 'C_B_Price': 73.8, 'C_Ask_Price': 74.1, 'C_Ask_QTY': 350, 'SP': 17850, 'P_B_QTY': 250, 'P_B_Price': 382.15, 'P_Ask_QTY': 50, 'P_Ask_Price': 383.85, 'P_CHG': 87.34999999999997, 'P_LTP': 384.9, 'P_IV': 21.78, 'P_T_Volume': 355, 'P_CH_OI': 115, 'P_OI': 627}, {'Time': '11,26', 'C_OI': 1111, 'C_CH_OI': 359, 'C_T_Volume': 925, 'C_IV': 16.19, 'C_LTP': 115.95, 'C_CHG': -44.499999999999986, 'C_B_QTY': 100, 'C_B_Price': 116.4, 'C_Ask_Price': 117.45, 'C_Ask_QTY': 100, 'SP': 17900, 'P_B_QTY': 100, 'P_B_Price': 464.9, 'P_Ask_QTY': 50, 'P_Ask_Price': 478.25, 'P_CHG': 83.90000000000003, 'P_LTP': 467.1, 'P_IV': 21.03, 'P_T_Volume': 28, 'P_CH_OI': -2, 'P_OI': 163}, {'Time': '11,26', 'C_OI': 1316, 'C_CH_OI': -133, 'C_T_Volume': 1599, 'C_IV': 15.19, 'C_LTP': 140.15, 'C_CHG': -43.54999999999998, 'C_B_QTY': 150, 'C_B_Price': 139.95, 'C_Ask_Price':
    140.35, 'C_Ask_QTY': 650, 'SP': 17950, 'P_B_QTY': 350, 'P_B_Price': 534, 'P_Ask_QTY': 350, 'P_Ask_Price': 538,
    'P_CHG': 67.5, 'P_LTP': 522.5, 'P_IV': 20.16, 'P_T_Volume': 39, 'P_CH_OI': -9, 'P_OI': 142}, {'Time': '11,26',
    'C_OI': 3040, 'C_CH_OI': 672, 'C_T_Volume': 2073, 'C_IV': 16.04, 'C_LTP': 88.85, 'C_CHG': -34.900000000000006,
    'C_B_QTY': 250, 'C_B_Price': 87.9, 'C_Ask_Price': 88.45, 'C_Ask_QTY': 100, 'SP': 18000, 'P_B_QTY': 250, 'P_B_Price': 540, 'P_Ask_QTY': 50, 'P_Ask_Price': 543.6, 'P_CHG': 91.89999999999998, 'P_LTP': 542, 'P_IV': 21.83, 'P_T_Volume': 80, 'P_CH_OI': -16, 'P_OI': 58}, {'Time': '11,26', 'C_OI': 2146, 'C_CH_OI': 884, 'C_T_Volume': 4949,
    'C_IV': 16.84, 'C_LTP': 32.85, 'C_CHG': -23.299999999999997, 'C_B_QTY': 250, 'C_B_Price': 32.85, 'C_Ask_Price': 33.05, 'C_Ask_QTY': 100, 'SP': 18050, 'P_B_QTY': 450, 'P_B_Price': 538.4, 'P_Ask_QTY': 50, 'P_Ask_Price': 542.95, 'P_CHG': 104.55000000000007, 'P_LTP': 547.95, 'P_IV': 22.97, 'P_T_Volume': 18, 'P_CH_OI': 3, 'P_OI': 21}, {'Time': '11,26', 'C_OI': 12726, 'C_CH_OI': 1494, 'C_T_Volume': 21842, 'C_IV': 16.89, 'C_LTP': 26.45, 'C_CHG': -19.55, 'C_B_QTY': 1150, 'C_B_Price': 26.55, 'C_Ask_Price': 26.7, 'C_Ask_QTY': 2400, 'SP': 18100, 'P_B_QTY': 200, 'P_B_Price': 582.8, 'P_Ask_QTY': 100, 'P_Ask_Price': 585.4, 'P_CHG': 110.14999999999998, 'P_LTP': 588.15, 'P_IV': 23.02, 'P_T_Volume': 596, 'P_CH_OI': 67, 'P_OI': 281}, {'Time': '11,26', 'C_OI': 4886, 'C_CH_OI': 3061, 'C_T_Volume': 15039, 'C_IV': 16.77, 'C_LTP': 20.9, 'C_CHG': -15.950000000000003, 'C_B_QTY': 50, 'C_B_Price': 20.9, 'C_Ask_Price': 20.95, 'C_Ask_QTY': 1250, 'SP': 18150, 'P_B_QTY': 2550, 'P_B_Price': 624.05, 'P_Ask_QTY': 600, 'P_Ask_Price': 634.8, 'P_CHG': 88.79999999999995, 'P_LTP': 601.75, 'P_IV': 18.51, 'P_T_Volume': 11, 'P_CH_OI': -4, 'P_OI': 26}, {'Time': '11,26', 'C_OI': 13496, 'C_CH_OI': 337, 'C_T_Volume': 25103, 'C_IV': 16.93, 'C_LTP': 16.9, 'C_CHG': -12.25, 'C_B_QTY': 1700, 'C_B_Price': 16.85, 'C_Ask_Price': 16.95, 'C_Ask_QTY': 5050, 'SP': 18200, 'P_B_QTY': 50, 'P_B_Price': 673.4, 'P_Ask_QTY': 200, 'P_Ask_Price': 677.1, 'P_CHG': 124, 'P_LTP': 686.9, 'P_IV': 25.43, 'P_T_Volume': 80, 'P_CH_OI': 29, 'P_OI': 230}, {'Time': '11,26', 'C_OI': 30, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 100, 'C_B_Price': 28.45, 'C_Ask_Price': 46.2, 'C_Ask_QTY': 50, 'SP': 18250, 'P_B_QTY': 1750, 'P_B_Price': 439.8, 'P_Ask_QTY': 50, 'P_Ask_Price': 772.95, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 1}, {'Time': '11,26', 'C_OI': 12666, 'C_CH_OI': 1114, 'C_T_Volume': 5759, 'C_IV': 14.98, 'C_LTP': 56.05, 'C_CHG': -19.75, 'C_B_QTY': 350, 'C_B_Price': 56, 'C_Ask_Price': 56.15, 'C_Ask_QTY': 850, 'SP': 18300, 'P_B_QTY': 200, 'P_B_Price': 793.6, 'P_Ask_QTY': 200, 'P_Ask_Price': 804.1, 'P_CHG': 82.35000000000002, 'P_LTP': 770, 'P_IV': 20.09, 'P_T_Volume': 41, 'P_CH_OI': -21, 'P_OI':
    764}, {'Time': '11,26', 'C_OI': 151, 'C_CH_OI': 92, 'C_T_Volume': 122, 'C_IV': 15.96, 'C_LTP': 27.9, 'C_CHG': -12.399999999999999, 'C_B_QTY': 50, 'C_B_Price': 26.4, 'C_Ask_Price': 27.5, 'C_Ask_QTY': 50, 'SP': 18350, 'P_B_QTY': 1800, 'P_B_Price': 678.15, 'P_Ask_QTY': 1750, 'P_Ask_Price': 903.9, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 1}, {'Time': '11,26', 'C_OI': 13170, 'C_CH_OI': 1055, 'C_T_Volume': 16466,
    'C_IV': 17.42, 'C_LTP': 6.9, 'C_CHG': -4.199999999999999, 'C_B_QTY': 1800, 'C_B_Price': 6.9, 'C_Ask_Price': 6.95, 'C_Ask_QTY': 1550, 'SP': 18400, 'P_B_QTY': 150, 'P_B_Price': 854.1, 'P_Ask_QTY': 50, 'P_Ask_Price': 866.75,
    'P_CHG': 106, 'P_LTP': 834.55, 'P_IV': 19.46, 'P_T_Volume': 5, 'P_CH_OI': -1, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 14, 'C_CH_OI': 0, 'C_T_Volume': 3, 'C_IV': 15.68, 'C_LTP': 18.4, 'C_CHG': -12.8, 'C_B_QTY': 100, 'C_B_Price': 14.5, 'C_Ask_Price': 19.9, 'C_Ask_QTY': 50, 'SP': 18450, 'P_B_QTY': 1800, 'P_B_Price': 605.2, 'P_Ask_QTY':
    1750, 'P_Ask_Price': 992.2, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 1}, {'Time': '11,26', 'C_OI': 13110, 'C_CH_OI': 1246, 'C_T_Volume': 16012, 'C_IV': 17.94, 'C_LTP': 4.9, 'C_CHG': -2.1999999999999993, 'C_B_QTY': 9100, 'C_B_Price': 4.9, 'C_Ask_Price': 5, 'C_Ask_QTY': 4550, 'SP': 18500, 'P_B_QTY': 150, 'P_B_Price': 959.95, 'P_Ask_QTY': 250, 'P_Ask_Price': 964.5, 'P_CHG': 144, 'P_LTP': 955, 'P_IV': 26.77, 'P_T_Volume': 56, 'P_CH_OI': 39, 'P_OI': 73}, {'Time': '11,26', 'C_OI': 7335, 'C_CH_OI': -2, 'C_T_Volume': 11446,
    'C_IV': 45.6, 'C_LTP': 1.4, 'C_CHG': 0.44999999999999996, 'C_B_QTY': 8850, 'C_B_Price': 1.35, 'C_Ask_Price': 1.4, 'C_Ask_QTY': 1900, 'SP': 18550, 'P_B_QTY': 250, 'P_B_Price': 1006.7, 'P_Ask_QTY': 250, 'P_Ask_Price': 1021.85, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 7766, 'C_CH_OI': 1978, 'C_T_Volume': 8419, 'C_IV': 18.7, 'C_LTP': 3.8, 'C_CHG': -0.9500000000000002, 'C_B_QTY': 4450, 'C_B_Price': 3.75, 'C_Ask_Price': 3.85, 'C_Ask_QTY': 1250, 'SP': 18600, 'P_B_QTY': 150, 'P_B_Price': 1057, 'P_Ask_QTY': 150, 'P_Ask_Price': 1075.65, 'P_CHG': 87.25, 'P_LTP': 1026.25, 'P_IV': 19.18, 'P_T_Volume': 4, 'P_CH_OI': 2, 'P_OI': 9}, {'Time': '11,26', 'C_OI': 28, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 50, 'C_B_Price': 9.05, 'C_Ask_Price': 13.05, 'C_Ask_QTY': 50, 'SP': 18650, 'P_B_QTY': 1750, 'P_B_Price': 978.2, 'P_Ask_QTY': 1750, 'P_Ask_Price': 1201.05, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume':
    0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 5457, 'C_CH_OI': 323, 'C_T_Volume': 5245, 'C_IV': 19.54, 'C_LTP': 3, 'C_CHG': -0.10000000000000009, 'C_B_QTY': 2700, 'C_B_Price': 2.95, 'C_Ask_Price': 3.05, 'C_Ask_QTY': 1000, 'SP': 18700, 'P_B_QTY': 450, 'P_B_Price': 1137.45, 'P_Ask_QTY': 450, 'P_Ask_Price': 1177.3, 'P_CHG': 86.15000000000009, 'P_LTP': 1143.45, 'P_IV': 27.9, 'P_T_Volume': 4, 'P_CH_OI': 0, 'P_OI': 7}, {'Time': '11,26',
    'C_OI': 1018, 'C_CH_OI': 65, 'C_T_Volume': 6117, 'C_IV': 52.43, 'C_LTP': 1.2, 'C_CHG': 0.44999999999999996, 'C_B_QTY': 10100, 'C_B_Price': 1.15, 'C_Ask_Price': 1.2, 'C_Ask_QTY': 550, 'SP': 18750, 'P_B_QTY': 1650, 'P_B_Price': 1205.7, 'P_Ask_QTY': 1650, 'P_Ask_Price': 1225.35, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 2039, 'C_CH_OI': -1043, 'C_T_Volume': 3654, 'C_IV': 20.61, 'C_LTP': 2.8, 'C_CHG': 0.34999999999999964, 'C_B_QTY': 1350, 'C_B_Price': 2.75, 'C_Ask_Price': 2.8, 'C_Ask_QTY': 50, 'SP': 18800, 'P_B_QTY': 150, 'P_B_Price': 1257, 'P_Ask_QTY': 50, 'P_Ask_Price': 1262.75, 'P_CHG': 75.84999999999991, 'P_LTP': 1272.6, 'P_IV': 36.75, 'P_T_Volume': 2, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 1522, 'C_CH_OI': 673, 'C_T_Volume': 6507, 'C_IV': 55.25, 'C_LTP': 1.15, 'C_CHG': 0.44999999999999996, 'C_B_QTY':
    2450, 'C_B_Price': 1.15, 'C_Ask_Price': 1.2, 'C_Ask_QTY': 4200, 'SP': 18850, 'P_B_QTY': 150, 'P_B_Price': 1304.2, 'P_Ask_QTY': 450, 'P_Ask_Price': 1324.9, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 2}, {'Time': '11,26', 'C_OI': 4686, 'C_CH_OI': 1238, 'C_T_Volume': 14020, 'C_IV': 56.74, 'C_LTP': 1.1, 'C_CHG': 0.45000000000000007, 'C_B_QTY': 1800, 'C_B_Price': 1.05, 'C_Ask_Price': 1.1, 'C_Ask_QTY': 6750, 'SP': 18900, 'P_B_QTY': 650, 'P_B_Price': 1354.95, 'P_Ask_QTY': 900, 'P_Ask_Price': 1375.8, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 3}, {'Time': '11,26', 'C_OI': 281, 'C_CH_OI': -6, 'C_T_Volume': 40, 'C_IV': 22.38, 'C_LTP': 2.4, 'C_CHG': 0, 'C_B_QTY': 1350, 'C_B_Price': 2.35, 'C_Ask_Price': 2.75, 'C_Ask_QTY': 100, 'SP': 18950, 'P_B_QTY': 150, 'P_B_Price': 1401.3, 'P_Ask_QTY': 150, 'P_Ask_Price': 1438, 'P_CHG': 0,
    'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 1619, 'C_CH_OI': 410, 'C_T_Volume': 647, 'C_IV': 18.25, 'C_LTP': 4.85, 'C_CHG': -1, 'C_B_QTY': 50, 'C_B_Price': 4.85, 'C_Ask_Price': 4.95, 'C_Ask_QTY': 2900, 'SP': 19000, 'P_B_QTY': 1750, 'P_B_Price': 1302.45, 'P_Ask_QTY': 1750, 'P_Ask_Price': 1581.6, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 34, 'C_CH_OI': 0, 'C_T_Volume': 1, 'C_IV': 18.04, 'C_LTP': 3.75, 'C_CHG': -1.4500000000000002, 'C_B_QTY': 50, 'C_B_Price': 3.8, 'C_Ask_Price': 5.95, 'C_Ask_QTY': 50, 'SP': 19050, 'P_B_QTY': 1750, 'P_B_Price': 1350.7, 'P_Ask_QTY': 1750, 'P_Ask_Price': 1631.55, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 94, 'C_CH_OI': 46, 'C_T_Volume': 72, 'C_IV': 18.95, 'C_LTP': 4.35, 'C_CHG':
    -0.40000000000000036, 'C_B_QTY': 50, 'C_B_Price': 4.3, 'C_Ask_Price': 4.45, 'C_Ask_QTY': 100, 'SP': 19100, 'P_B_QTY': 1750, 'P_B_Price': 1395.55, 'P_Ask_QTY': 1750, 'P_Ask_Price': 1691.45, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 62, 'C_CH_OI': 4, 'C_T_Volume': 11, 'C_IV': 24.71, 'C_LTP': 2.15, 'C_CHG': 0.1499999999999999, 'C_B_QTY': 50, 'C_B_Price': 1.75, 'C_Ask_Price': 2.3, 'C_Ask_QTY': 700, 'SP': 19150, 'P_B_QTY': 1500, 'P_B_Price': 1569.85, 'P_Ask_QTY': 1500, 'P_Ask_Price': 1653.4, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 9936, 'C_CH_OI': 767, 'C_T_Volume': 6282, 'C_IV': 64.38, 'C_LTP': 0.75, 'C_CHG': 0.19999999999999996, 'C_B_QTY': 4050,
    'C_B_Price': 0.7, 'C_Ask_Price': 0.8, 'C_Ask_QTY': 3900, 'SP': 19200, 'P_B_QTY': 250, 'P_B_Price': 1634.6, 'P_Ask_QTY': 250, 'P_Ask_Price': 1694.9, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI':
    2}, {'Time': '11,26', 'C_OI': 39, 'C_CH_OI': -3, 'C_T_Volume': 41, 'C_IV': 26.01, 'C_LTP': 1.95, 'C_CHG': -0.30000000000000004, 'C_B_QTY': 50, 'C_B_Price': 2, 'C_Ask_Price': 2.15, 'C_Ask_QTY': 250, 'SP': 19250, 'P_B_QTY':
    1500, 'P_B_Price': 1669.55, 'P_Ask_QTY': 1500, 'P_Ask_Price': 1753.15, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 482, 'C_CH_OI': -33, 'C_T_Volume': 90, 'C_IV':
    25.63, 'C_LTP': 1.55, 'C_CHG': -0.050000000000000044, 'C_B_QTY': 50, 'C_B_Price': 1.6, 'C_Ask_Price': 1.8, 'C_Ask_QTY': 100, 'SP': 19300, 'P_B_QTY': 1500, 'P_B_Price': 1719.4, 'P_Ask_QTY': 1500, 'P_Ask_Price': 1803.05, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 195, 'C_CH_OI': 14, 'C_T_Volume': 64, 'C_IV': 26.63, 'C_LTP': 1.75, 'C_CHG': 0.1499999999999999, 'C_B_QTY': 50, 'C_B_Price': 1.8, 'C_Ask_Price': 1.95, 'C_Ask_QTY': 600, 'SP': 19350, 'P_B_QTY': 1500, 'P_B_Price': 1769.3, 'P_Ask_QTY': 1500, 'P_Ask_Price': 1852.95, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 809, 'C_CH_OI': 85, 'C_T_Volume': 400, 'C_IV': 26.77, 'C_LTP': 1.9, 'C_CHG': 0.2999999999999998, 'C_B_QTY': 50, 'C_B_Price': 1.75, 'C_Ask_Price': 1.85, 'C_Ask_QTY': 50, 'SP': 19400, 'P_B_QTY': 1500, 'P_B_Price': 1819.25, 'P_Ask_QTY': 50, 'P_Ask_Price': 1882.5, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 613, 'C_CH_OI': 23, 'C_T_Volume': 60, 'C_IV': 26.7, 'C_LTP': 1.35, 'C_CHG': -0.1499999999999999, 'C_B_QTY': 50, 'C_B_Price': 1.4, 'C_Ask_Price': 1.55, 'C_Ask_QTY': 2950, 'SP': 19450, 'P_B_QTY': 1500, 'P_B_Price': 1869, 'P_Ask_QTY': 1500, 'P_Ask_Price': 1952.75, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 60, 'C_CH_OI': 1, 'C_T_Volume': 5, 'C_IV': 15.99, 'C_LTP': 16.6, 'C_CHG': -1.6999999999999993, 'C_B_QTY': 50, 'C_B_Price': 16.5, 'C_Ask_Price': 16.95, 'C_Ask_QTY': 50, 'SP': 19750, 'P_B_QTY': 1500, 'P_B_Price': 1982.85, 'P_Ask_QTY': 1500, 'P_Ask_Price': 2298.9, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 34, 'C_CH_OI': -1, 'C_T_Volume': 2, 'C_IV': 16.33, 'C_LTP': 15.1, 'C_CHG': -1.0000000000000018, 'C_B_QTY': 50, 'C_B_Price': 14.7, 'C_Ask_Price': 16.55, 'C_Ask_QTY': 100, 'SP': 19850, 'P_B_QTY': 1500, 'P_B_Price': 2076.5, 'P_Ask_QTY': 1500, 'P_Ask_Price': 2402.3, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 27132, 'C_CH_OI': 425, 'C_T_Volume': 1871, 'C_IV': 23.09, 'C_LTP': 4.95, 'C_CHG': -0.09999999999999964, 'C_B_QTY': 150, 'C_B_Price': 4.95, 'C_Ask_Price': 5, 'C_Ask_QTY': 50, 'SP': 20000, 'P_B_QTY': 50, 'P_B_Price': 2429.15, 'P_Ask_QTY': 250, 'P_Ask_Price': 2444.35, 'P_CHG': 127, 'P_LTP': 2432.6, 'P_IV': 38.25, 'P_T_Volume': 42, 'P_CH_OI': -17, 'P_OI': 17210}, {'Time': '11,26', 'C_OI': 2343, 'C_CH_OI': 11, 'C_T_Volume': 81, 'C_IV': 29.24, 'C_LTP': 3.45, 'C_CHG': -0.1499999999999999, 'C_B_QTY': 200, 'C_B_Price': 3.45, 'C_Ask_Price': 3.9, 'C_Ask_QTY': 100, 'SP': 21000, 'P_B_QTY': 50, 'P_B_Price': 3400.9, 'P_Ask_QTY': 150, 'P_Ask_Price': 3445.45, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 473}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 1800,
    'C_B_Price': 375.25, 'C_Ask_Price': 0, 'C_Ask_QTY': 0, 'SP': 22000, 'P_B_QTY': 50, 'P_B_Price': 1313.3, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}, {'Time': '11,26', 'C_OI': 0, 'C_CH_OI': 0, 'C_T_Volume': 0, 'C_IV': 0, 'C_LTP': 0, 'C_CHG': 0, 'C_B_QTY': 0, 'C_B_Price': 0, 'C_Ask_Price': 5779, 'C_Ask_QTY': 50, 'SP': 23000, 'P_B_QTY': 50, 'P_B_Price': 940.3, 'P_Ask_QTY': 0, 'P_Ask_Price': 0, 'P_CHG': 0, 'P_LTP': 0, 'P_IV': 0, 'P_T_Volume': 0, 'P_CH_OI': 0, 'P_OI': 0}]

    strike_value = [7500, 8500, 8700, 9000, 9500, 9700, 9900, 10000, 10500, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13500, 13950, 14000, 14050, 14100, 14150, 14200, 14250, 14300, 14350, 14400, 14450, 14500, 14550, 14600, 14650, 14700, 14750, 14800, 14850, 14900, 14950, 15000, 15050, 15100, 15150, 15200, 15250, 15300, 15350, 15400, 15450, 15500, 15550, 15600, 15650, 15700, 15750, 15800, 15850, 15900, 15950, 16000, 16050, 16100, 16150, 16200, 16250, 16300, 16350, 16400, 16450, 16500, 16550, 16600, 16650, 16700, 16750, 16800, 16850, 16900, 16950, 17000, 17050, 17100,
        17150, 17200, 17250, 17300, 17350, 17400, 17450, 17500, 17550, 17600, 17650, 17700, 17750, 17800, 17850, 17900, 17950, 18000, 18050, 18100, 18150, 18200, 18250, 18300, 18350, 18400, 18450, 18500, 18550, 18600, 18650, 18700, 18750, 18800, 18850, 18900, 18950, 19000, 19050, 19100, 19150, 19200, 19250, 19300, 19350, 19400, 19450, 19500, 19550, 19600, 19650, 19700, 19750, 19800, 19850, 19900, 19950, 20000, 20050, 20100, 20150, 20200, 20250, 20300, 20350, 20400, 20500, 21000, 22000, 23000]

    value = 17543.55

    e_dates = "2022-Sep-29, 2022-Oct-27, 2022-Nov-24"

    animal = dataenter(workbook_name1,actual_data,strike_value,value,"1",e_dates)
    return render_template('sample.html', data=animal)

if __name__ == '__main__':
    app.run(debug=True)
