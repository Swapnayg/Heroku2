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

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://feneghthythdta:5c99a5dfc7ce5f95d0c559d8091b2d644eccd3d5e1b232f5575888903dc2ba63@ec2-107-23-76-12.compute-1.amazonaws.com:5432/dbofs1cco6n2nf'
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
                        data = NseDbDailyData(str(info["Time"]),str(info["C_OI"]),str(c_roi),str(info["C_CH_OI"]),str(c_rocoi),str(info["C_T_Volume"]),str(c_rov),str(info["C_IV"]),str(c_roiv),str(info["C_LTP"]),str(c_roltp),str(c_nt),str(c_ront),str(c_ltp_vlm),str(c_roltp_vlm),str(info["C_CHG"]),str(c_coi_nt),str(c_rocoi_nt),str(c_ltp_coi),str(c_roc_ltp_coi),str(info["C_B_QTY"]),str(info["C_B_Price"]),str(info["C_Ask_Price"]),str(info["C_Ask_QTY"]),str(info["SP"]),str(info["P_B_QTY"]),str(info["P_B_Price"]),str(info["P_Ask_QTY"]),str(info["P_Ask_Price"]),str(info["P_CHG"]),str(info["P_LTP"]),str(p_roltp),str(p_nt),str(p_ront),str(p_ltp_vlm),str(p_roltp_vlm),str(info["P_IV"]),str(p_roiv),str(info["P_T_Volume"]),str(p_rov),str(info["P_CH_OI"]),str(p_rocoi),str(info["P_OI"]),str(p_roi),str(p_coi_nt),str(p_rocoi_nt),str(p_ltp_coi),str(p_roc_ltp_coi),str(today.strftime("%d-%m-%Y")),str(c_roc_vol_roc_nt),str(roc_c_roc_vol_roc_nt),str(p_roc_vol_roc_nt),str(roc_p_roc_vol_roc_nt))
                        db.session.add(data)
                        db.session.commit()
                        
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
        sql_query_list.append({"str_time":sql.str_time,"c_oi":sql.c_oi,"c_roc_oi":sql.c_roc_oi,"c_chng_in_oi":sql.c_chng_in_oi,"c_roc_chng_in_oi":sql.c_roc_chng_in_oi,"c_volume":sql.c_volume,"c_roc_volume":sql.c_roc_volume,"c_iv":sql.c_iv,"c_roc_iv":sql.c_roc_iv,"c_ltp":sql.c_ltp,"c_roc_ltp":sql.c_roc_ltp,"c_nt":sql.c_nt,"c_roc_nt":sql.c_roc_nt,"c_ltp_vl":sql.c_ltp_vl,"c_roc_ltp_vl":sql.c_roc_ltp_vl,"c_chng":sql.c_chng,"c_oi_nt":sql.c_oi_nt,"c_roc_oi_nt":sql.c_roc_oi_nt,"c_ltp_coi":sql.c_ltp_coi,"c_roc_ltp_coi":sql.c_roc_ltp_coi,"c_bid_qty":sql.c_bid_qty,"c_bid_price":sql.c_bid_price,"c_ask_price":sql.c_ask_price,"c_ask_qty":sql.c_ask_qty,"strike_price":sql.strike_price,"p_bid_qty":sql.p_bid_qty,"p_bid_price":sql.p_bid_price,"p_ask_price":sql.p_ask_price,"p_ask_qty":sql.p_ask_qty,"p_chng":sql.p_chng,"p_ltp":sql.p_ltp,"p_roc_ltp":sql.p_roc_ltp,"p_nt":sql.p_nt,"p_roc_nt":sql.p_roc_nt,"p_ltp_vl":sql.p_ltp_vl,"p_roc_ltp_vl":sql.p_roc_ltp_vl,"p_iv":sql.p_iv,"p_roc_iv":sql.p_roc_iv,"p_volume":sql.p_volume,"p_roc_volume":sql.p_roc_volume,"p_chng_in_oi":sql.p_chng_in_oi,"p_roc_chng_in_oi":sql.p_roc_chng_in_oi,"p_oi":sql.p_oi,"p_roc_oi":sql.p_roc_oi,"p_oi_nt":sql.p_oi_nt,"p_roc_oi_nt":sql.p_roc_oi_nt,"p_ltp_coi":sql.p_ltp_coi,"p_roc_ltp_coi":sql.p_roc_ltp_coi,"txtcurrent_date":sql.txtcurrent_date,"c_roc_vol_roc_nt":sql.c_roc_vol_roc_nt,"roc_c_roc_vol_roc_nt":sql.roc_c_roc_vol_roc_nt,"p_roc_vol_roc_nt":sql.p_roc_vol_roc_nt,"roc_p_roc_vol_roc_nt":sql.roc_p_roc_vol_roc_nt})
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

def binddata_minute():
    global thread_start
    global count
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M')
    minute = ind_time.split(":")[0]
    second = ind_time.split(":")[1]
    if((int(minute) >= int("09") and int(second) >= int("15")) or (int(minute) <= int("15") and int(second) <= int("50"))): 
        if(int(minute) == int("09") and int(second) == int("50")):
            addstartval(ind_time,int(minute),int(second))
        elif(int(minute) == int("15") and int(second) == int("45")):
            addendval(ind_time,int(minute),int(second))
        else:
            actualFun(ind_time,int(minute),int(second))
    elif((int(minute) == int("18") and int(second) == int("05"))):
        addendval(ind_time,int(minute),int(second))
    else:
        actualFun(ind_time,int(minute),int(second))
    count = count + 1 
    thread_start = threading.Timer(POOL_TIME, binddata_minute, ())
    thread_start.start()  

def addstartval(ind_time,minute,second):
    try:
        today = date.today() 
        option_chain_data = nse_optionchain_scrapper('NIFTY')
        expiry_dates = list(option_chain_data["records"]["expiryDates"])
        s = pd.Series(pd.to_datetime(expiry_dates))
        new_list = s.groupby(s.dt.strftime('%Y-%m')).max().tolist()
        e_dates = new_list[0].strftime("%Y-%b-%d") + ", " + new_list[1].strftime("%Y-%b-%d")  + ", " + new_list[2].strftime("%Y-%b-%d")
        data = NseDbOpenCloseData(str(option_chain_data["records"]["underlyingValue"]),'','',str(today.strftime("%d-%m-%Y"),e_dates))
        db.session.add(data)
        db.session.commit()   
        actualFun(ind_time,minute,second)
    except:
        pass

def addendval(ind_time,minute,second):
    try:
        option_chain_data = nse_optionchain_scrapper('NIFTY')
        today = date.today() 
        value = NseDbOpenCloseData.query.filter(NseDbOpenCloseData.txttoday_date == str(today.strftime("%d-%m-%Y"))).first()
        value.close_val = str(option_chain_data["records"]["underlyingValue"])
        db.session.flush()
        db.session.commit()
        actualFun(ind_time,minute,second)
    except:
        pass

def actualFun(ind_time,minute,second):
    # try:
        counter = 0
        actual_data = []
        pe_data = []
        ce_data = []
        strike_value = []
        pe_data1 = []
        data1 = []
        value = 0
        e_dates = ''
        try:
            option_chain_data = nse_optionchain_scrapper('NIFTY')
            data1 = option_chain_data["records"]["data"]
            strike_value = option_chain_data["records"]["strikePrices"]
            value = float(option_chain_data["records"]["underlyingValue"])
            expiry_dates = list(option_chain_data["records"]["expiryDates"])
            s = pd.Series(pd.to_datetime(expiry_dates))
            new_list = s.groupby(s.dt.strftime('%Y-%m')).max().tolist()
            e_dates = new_list[0].strftime("%Y-%b-%d") + ", " + new_list[1].strftime("%Y-%b-%d")  + ", " + new_list[2].strftime("%Y-%b-%d")
            for sp in strike_value:
                sE_data =   [x for x in data1 if x["strikePrice"] == sp ]
                try:
                    PE_data = sE_data[0]["PE"]
                    pe_data.append({"SP":PE_data['strikePrice'],"OI":PE_data['openInterest'],"CH_OI":PE_data['changeinOpenInterest'],"T_Volume":PE_data['totalTradedVolume'],"IV":PE_data['impliedVolatility'],"LTP":PE_data['lastPrice'],"CHG":PE_data['change'],"B_QTY":PE_data['bidQty'],"B_Price":PE_data['bidprice'],"Ask_Price":PE_data['askPrice'],"Ask_QTY":PE_data['askQty']})
                except:
                    pass

            for sp in strike_value:
                sE_data =   [x for x in data1 if x["strikePrice"] == sp ]
                try:
                    CE_data = sE_data[0]["CE"]
                    pe_values = [x for x in pe_data if str(x['SP']) == str(sp)]
                    if(len(pe_values) != 0):
                        actual_data.append({"Time":str(str(minute) +","+str(second)),"C_OI":CE_data['openInterest'],"C_CH_OI":CE_data['changeinOpenInterest'],"C_T_Volume":CE_data['totalTradedVolume'],"C_IV":CE_data['impliedVolatility'],"C_LTP":CE_data['lastPrice'],"C_CHG":CE_data['change'],"C_B_QTY":CE_data['bidQty'],"C_B_Price":CE_data['bidprice'],"C_Ask_Price":CE_data['askPrice'],"C_Ask_QTY":CE_data['askQty'],"SP":CE_data['strikePrice'],"P_B_QTY":pe_values[0]['B_QTY'],"P_B_Price":pe_values[0]['B_Price'],"P_Ask_QTY":pe_values[0]['Ask_QTY'],"P_Ask_Price":pe_values[0]['Ask_Price'],"P_CHG":pe_values[0]['CHG'],"P_LTP":pe_values[0]['LTP'],"P_IV":pe_values[0]['IV'],"P_T_Volume":pe_values[0]['T_Volume'],"P_CH_OI":pe_values[0]['CH_OI'],"P_OI":pe_values[0]['OI']})
                except:
                    pass
        except:
            pass
        if(minute == int("09")):
            if(second >= int("15") and second <= int("59")):
                dataenter(workbook_name1,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("10")):
            if(second >= int("00") and second <= int("59")):
                dataenter(workbook_name2,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("11")):
            if(second >= int("00") and second <= int("59")):
                dataenter(workbook_name3,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("12")):
            if(second >= int("00") and second <= int("59")):
                dataenter(workbook_name4,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("13")):
            if(second >= int("00") and second <= int("59")):
                dataenter(workbook_name5,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("14")):
            if(second >= int("00") and second <= int("59")):
                dataenter(workbook_name6,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("15")):
            if(second >= int("00") and second <= int("31")):
                dataenter(workbook_name7,actual_data,strike_value,value,"1",e_dates)
        elif(minute == int("18")):
            dataenter(workbook_name7,actual_data,strike_value,value,"1",e_dates)
        else:
            dataenter(workbook_name7,actual_data,strike_value,value,"other",e_dates)
    # except:
    #     pass

@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/oi_chart')
def oi_chart():
    return render_template('oi_chart.html')

@app.route('/P_oi_chart')
def P_oi_chart():
    return render_template('P_oi_chart.html')

@app.route('/month1_chart1')
def month1_chart1():
    return render_template('month1_chart1.html')

@app.route('/month2_chart1')
def month2_chart1():
    return render_template('month2_chart1.html')

@app.route('/month3_chart1')
def month3_chart1():
    return render_template('month3_chart1.html')

def get_data(strike_num, param):
    data = []
    today_date = date.today()
    for i,un in enumerate(udelying_values):
        if(i ==0):
            times1 =[]
            values1 = []
            for t1 in strike_values1:
                tt1 = t1["time"].split(":")
                time_val = datetime(int(today_date.year),int(today_date.month),int(today_date.day),int(tt1[0]),int(tt1[1]))
                if(param == "C_ROC_OI"):
                    values1.append(float(format(float(t1["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values1.append(float(format(float(t1["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values1.append(float(format(float(t1["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values1.append(float(format(float(t1["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values1.append(float(format(float(t1["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values1.append(float(format(float(t1["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values1.append(float(format(float(t1["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values1.append(float(format(float(t1["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values1.append(float(format(float(t1["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values1.append(float(format(float(t1["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values1.append(float(format(float(t1["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values1.append(float(format(float(t1["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values1.append(float(format(float(t1["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values1.append(float(format(float(t1["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values1.append(float(format(float(t1["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values1.append(float(format(float(t1["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values1.append(float(format(float(t1["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values1.append(float(format(float(t1["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values1.append(float(format(float(t1["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values1.append(float(format(float(t1["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times1.append(int(format(time.mktime(time_val.timetuple()) * 1000, ".0f")))
            data.append({"strike_point":un,"times":times1,"value":values1})
        elif(i ==1):
            times2 =[]
            values2 = []
            for t2 in strike_values2:
                tt2 = t2["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt2[0]),int(tt2[1]))
                if(param == "C_ROC_OI"):
                    values2.append(float(format(float(t2["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values2.append(float(format(float(t2["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values2.append(float(format(float(t2["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values2.append(float(format(float(t2["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values2.append(float(format(float(t2["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values2.append(float(format(float(t2["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values2.append(float(format(float(t2["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values2.append(float(format(float(t2["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values2.append(float(format(float(t2["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values2.append(float(format(float(t2["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values2.append(float(format(float(t2["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values2.append(float(format(float(t2["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values2.append(float(format(float(t2["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values2.append(float(format(float(t2["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values2.append(float(format(float(t2["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values2.append(float(format(float(t2["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values2.append(float(format(float(t2["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values2.append(float(format(float(t2["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values2.append(float(format(float(t2["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values2.append(float(format(float(t2["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times2.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times2,"value":values2})
        elif(i ==2):
            times3 =[]
            values3 = []
            for t3 in strike_values3:
                tt3 = t3["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt3[0]),int(tt3[1]))
                if(param == "C_ROC_OI"):
                    values3.append(float(format(float(t3["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values3.append(float(format(float(t3["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values3.append(float(format(float(t3["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values3.append(float(format(float(t3["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values3.append(float(format(float(t3["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values3.append(float(format(float(t3["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values3.append(float(format(float(t3["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values3.append(float(format(float(t3["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values3.append(float(format(float(t3["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values3.append(float(format(float(t3["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values3.append(float(format(float(t3["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values3.append(float(format(float(t3["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values3.append(float(format(float(t3["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values3.append(float(format(float(t3["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values3.append(float(format(float(t3["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values3.append(float(format(float(t3["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values3.append(float(format(float(t3["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values3.append(float(format(float(t3["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values3.append(float(format(float(t3["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values3.append(float(format(float(t3["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times3.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times3,"value":values3})
        elif(i ==3):
            times4 =[]
            values4 = []
            for t4 in strike_values4:
                tt4 = t4["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt4[0]),int(tt4[1]))
                if(param == "C_ROC_OI"):
                    values4.append(float(format(float(t4["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values4.append(float(format(float(t4["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values4.append(float(format(float(t4["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values4.append(float(format(float(t4["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values4.append(float(format(float(t4["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values4.append(float(format(float(t4["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values4.append(float(format(float(t4["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values4.append(float(format(float(t4["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values4.append(float(format(float(t4["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values4.append(float(format(float(t4["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values4.append(float(format(float(t4["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values4.append(float(format(float(t4["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values4.append(float(format(float(t4["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values4.append(float(format(float(t4["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values4.append(float(format(float(t4["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values4.append(float(format(float(t4["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values4.append(float(format(float(t4["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values4.append(float(format(float(t4["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values4.append(float(format(float(t4["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values4.append(float(format(float(t4["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times4.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times4,"value":values4})
        elif(i ==4):
            times5 =[]
            values5 = []
            for t5 in strike_values5:
                tt5 = t5["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt5[0]),int(tt5[1]))
                if(param == "C_ROC_OI"):
                    values5.append(float(format(float(t5["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values5.append(float(format(float(t5["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values5.append(float(format(float(t5["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values5.append(float(format(float(t5["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values5.append(float(format(float(t5["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values5.append(float(format(float(t5["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values5.append(float(format(float(t5["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values5.append(float(format(float(t5["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values5.append(float(format(float(t5["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values5.append(float(format(float(t5["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values5.append(float(format(float(t5["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values5.append(float(format(float(t5["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values5.append(float(format(float(t5["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values5.append(float(format(float(t5["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values5.append(float(format(float(t5["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values5.append(float(format(float(t5["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values5.append(float(format(float(t5["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values5.append(float(format(float(t5["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values5.append(float(format(float(t5["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values5.append(float(format(float(t5["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times5.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times5,"value":values5})
        elif(i ==5):
            times6 =[]
            values6 = []
            for t6 in strike_values6:
                tt6 = t6["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt6[0]),int(tt6[1]))
                if(param == "C_ROC_OI"):
                    values6.append(float(format(float(t6["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values6.append(float(format(float(t6["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values6.append(float(format(float(t6["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values6.append(float(format(float(t6["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values6.append(float(format(float(t6["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values6.append(float(format(float(t6["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values6.append(float(format(float(t6["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values6.append(float(format(float(t6["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values6.append(float(format(float(t6["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values6.append(float(format(float(t6["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values6.append(float(format(float(t6["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values6.append(float(format(float(t6["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values6.append(float(format(float(t6["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values6.append(float(format(float(t6["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values6.append(float(format(float(t6["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values6.append(float(format(float(t6["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values6.append(float(format(float(t6["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values6.append(float(format(float(t6["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values6.append(float(format(float(t6["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values6.append(float(format(float(t6["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times6.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            
            data.append({"strike_point":un,"times":times6,"value":values6})
        elif(i ==6):
            times7 =[]
            values7 = []
            for t7 in strike_values7:
                tt7 = t7["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt7[0]),int(tt7[1]))
                if(param == "C_ROC_OI"):
                    values7.append(float(format(float(t7["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values7.append(float(format(float(t7["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values7.append(float(format(float(t7["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values7.append(float(format(float(t6["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values7.append(float(format(float(t7["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values7.append(float(format(float(t7["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values7.append(float(format(float(t7["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values7.append(float(format(float(t7["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values7.append(float(format(float(t7["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values7.append(float(format(float(t7["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values7.append(float(format(float(t7["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values7.append(float(format(float(t7["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values7.append(float(format(float(t7["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values7.append(float(format(float(t7["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values7.append(float(format(float(t7["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values7.append(float(format(float(t7["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values7.append(float(format(float(t7["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values7.append(float(format(float(t7["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values7.append(float(format(float(t7["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values7.append(float(format(float(t7["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times7.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times7,"value":values7})
        elif(i ==7):
            times8 =[]
            values8 = []
            for t8 in strike_values8:
                tt8 = t8["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt8[0]),int(tt8[1]))
                if(param == "C_ROC_OI"):
                    values8.append(float(format(float(t8["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values8.append(float(format(float(t8["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values8.append(float(format(float(t8["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values8.append(float(format(float(t8["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values8.append(float(format(float(t8["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values8.append(float(format(float(t8["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values8.append(float(format(float(t8["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values8.append(float(format(float(t8["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values8.append(float(format(float(t8["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values8.append(float(format(float(t8["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values8.append(float(format(float(t8["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values8.append(float(format(float(t8["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values8.append(float(format(float(t8["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values8.append(float(format(float(t8["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values8.append(float(format(float(t8["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values8.append(float(format(float(t8["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values8.append(float(format(float(t8["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values8.append(float(format(float(t8["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values8.append(float(format(float(t8["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values8.append(float(format(float(t8["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times8.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times8,"value":values8})
        elif(i ==8):
            times9 =[]
            values9 = []
            for t9 in strike_values9:
                tt9 = t9["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt9[0]),int(tt9[1]))
                if(param == "C_ROC_OI"):
                    values9.append(float(format(float(t9["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values9.append(float(format(float(t9["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values9.append(float(format(float(t9["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values9.append(float(format(float(t9["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values9.append(float(format(float(t9["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values9.append(float(format(float(t9["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values9.append(float(format(float(t9["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values9.append(float(format(float(t9["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values9.append(float(format(float(t9["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values9.append(float(format(float(t9["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values9.append(float(format(float(t9["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values9.append(float(format(float(t9["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values9.append(float(format(float(t9["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values9.append(float(format(float(t9["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values9.append(float(format(float(t9["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values9.append(float(format(float(t9["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values9.append(float(format(float(t9["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values9.append(float(format(t9["P_ROC_LTP_COI"], ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values9.append(float(format(float(t9["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values9.append(float(format(float(t9["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times9.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times9,"value":values9})
        elif(i ==9):
            times10 =[]
            values10 = []
            for t10 in strike_values10:
                tt10 = t10["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt10[0]),int(tt10[1]))
                if(param == "C_ROC_OI"):
                    values10.append(float(format(float(t10["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values10.append(float(format(float(t10["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values10.append(float(format(float(t10["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values10.append(float(format(float(t10["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values10.append(float(format(float(t10["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values10.append(float(format(float(t10["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values10.append(float(format(float(t10["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values10.append(float(format(float(t10["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values10.append(float(format(float(t10["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values10.append(float(format(float(t10["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values10.append(float(format(float(t10["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values10.append(float(format(float(t10["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values10.append(float(format(float(t10["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values10.append(float(format(float(t10["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values10.append(float(format(float(t10["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values10.append(float(format(float(t10["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values10.append(float(format(float(t10["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values10.append(float(format(float(t10["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values10.append(float(format(float(t10["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values10.append(float(format(float(t10["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times10.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times10,"value":values10})
        elif(i ==10):
            times11 =[]
            values11 = []
            for t11 in strike_values11:
                tt11 = t11["time"].split(":")
                time_val = datetime(today_date.year,today_date.month,today_date.day,int(tt11[0]),int(tt11[1]))
                if(param == "C_ROC_OI"):
                    values11.append(float(format(float(t11["C_ROC_OI"]), ".2f")))
                elif(param == "C_ROC_CHNG_IN_OI"):
                    values11.append(float(format(float(t11["C_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "C_ROC_VOLUME"):
                    values11.append(float(format(float(t11["C_ROC_VOLUME"]), ".2f")))
                elif(param == "C_ROC_IV"):
                    values11.append(float(format(float(t11["C_ROC_IV"]), ".2f")))
                elif(param == "C_ROC_LTP"):
                    values11.append(float(format(float(t11["C_ROC_LTP"]), ".2f")))
                elif(param == "P_ROC_OI"):
                    values11.append(float(format(float(t11["P_ROC_OI"]), ".2f")))
                elif(param == "P_ROC_CHNG_IN_OI"):
                    values11.append(float(format(float(t11["P_ROC_CHNG_IN_OI"]), ".2f")))
                elif(param == "P_ROC_VOLUME"):
                    values11.append(float(format(float(t11["P_ROC_VOLUME"]), ".2f")))
                elif(param == "P_ROC_IV"):
                    values11.append(float(format(float(t11["P_ROC_IV"]), ".2f")))
                elif(param == "P_ROC_LTP"):
                    values11.append(float(format(float(t11["P_ROC_LTP"]), ".2f")))
                elif(param == "C_ROC_NT"):
                    values11.append(float(format(float(t11["C_ROC_NT"]), ".2f")))
                elif(param == "C_ROC_OI_NT"):
                    values11.append(float(format(float(t11["C_ROC_OI_NT"]), ".2f")))
                elif(param == "C_ROC_LTP_VL"):
                    values11.append(float(format(float(t11["C_ROC_LTP_VL"]), ".2f")))
                elif(param == "P_ROC_NT"):
                    values11.append(float(format(float(t11["P_ROC_NT"]), ".2f")))
                elif(param == "P_ROC_OI_NT"):
                    values11.append(float(format(float(t11["P_ROC_OI_NT"]), ".2f")))
                elif(param == "P_ROC_LTP_VL"):
                    values11.append(float(format(float(t11["P_ROC_LTP_VL"]), ".2f")))
                elif(param == "C_ROC_LTP_COI"):
                    values11.append(float(format(float(t11["C_ROC_LTP_COI"]), ".2f")))
                elif(param == "P_ROC_LTP_COI"):
                    values11.append(float(format(float(t11["P_ROC_LTP_COI"]), ".2f")))
                elif(param == "ROC_C_ROC_VOL_ROC_NT"):
                    values11.append(float(format(float(t11["ROC_C_ROC_VOL_ROC_NT"]), ".2f")))
                elif(param == "ROC_P_ROC_VOL_ROC_NT"):
                    values11.append(float(format(float(t11["ROC_P_ROC_VOL_ROC_NT"]), ".2f")))
                times11.append(format(time.mktime(time_val.timetuple()) * 1000, ".0f"))
            data.append({"strike_point":un,"times":times11,"value":values11})
    return data

@app.route('/post_oi_chart', methods=['GET'])
def post_oi_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_OI")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_chg_in_chart', methods=['GET'])
def post_chg_in_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_CHNG_IN_OI")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_volume', methods=['GET'])
def post_volume(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_VOLUME")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_iv', methods=['GET'])
def post_iv(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_IV")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_ltp', methods=['GET'])
def post_ltp(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_LTP")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_oi_chart', methods=['GET'])
def post_p_oi_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_OI")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_chg_in_chart', methods=['GET'])
def post_p_chg_in_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_CHNG_IN_OI")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_volume', methods=['GET'])
def post_p_volume(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_VOLUME")
    resp = jsonify(data)
    resp.status_code = 201
    return resp
    
@app.route('/post_p_iv', methods=['GET'])
def post_p_iv(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_IV")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_ltp', methods=['GET'])
def post_p_ltp(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_LTP")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_notrade', methods=['GET'])
def post_notrade(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_co_notrade', methods=['GET'])
def post_co_notrade(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_OI_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_ltp_volum', methods=['GET'])
def post_ltp_volum(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_LTP_VL")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_volume_nt_chart', methods=['GET'])
def post_volume_nt_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"ROC_C_ROC_VOL_ROC_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_notrade', methods=['GET'])
def post_p_notrade(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_co_notrade', methods=['GET'])
def post_p_co_notrade(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_OI_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_ltp_volum', methods=['GET'])
def post_p_ltp_volum(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"P_ROC_LTP_VL")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/get_months', methods=['GET'])
def get_months(): 
    expiry_dates = []
    today = date.today() 
    prev_val = NseDbOpenCloseData.query.filter_by(txttoday_date=today.strftime("%d-%m-%Y")).first()
    if(prev_val!=None):
        if(len(prev_val.expiry_dates) != 0):
            expiry_dates = prev_val.expiry_dates.split(",")
    resp = jsonify(expiry_dates)
    resp.status_code = 201
    return resp

@app.route('/post_feat_month', methods=['GET'])
def post_feat_month(): 
    args = request.args
    strike_num = args.get('umonth')
    data = get_data(strike_num,"P_ROC_LTP_VL")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_ltp_coi', methods=['GET'])
def post_ltp_coi(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"C_ROC_OI_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

@app.route('/post_p_volume_nt_chart', methods=['GET'])
def post_p_volume_nt_chart(): 
    args = request.args
    strike_num = args.get('ustrike_num')
    data = get_data(strike_num,"ROC_P_ROC_VOL_ROC_NT")
    resp = jsonify(data)
    resp.status_code = 201
    return resp

def deleterecords(bar):
    print("bar")

if __name__ == '__main__':
    binddata_minute()
    app.run(debug=True, use_reloader=False)
