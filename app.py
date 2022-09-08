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

def getData_bind():
    today = date.today()
    data = NseDbDailyData(str('info["Time"]'),str('info["C_OI"]'),str('c_roi'),str('info["C_CH_OI"]'),str('c_rocoi'),str('info["C_T_Volume"]'),str('c_rov'),str('info["C_IV"]'),str('c_roiv'),str('info["C_LTP"]'),str('c_roltp'),str('c_nt'),str('c_ront'),str('c_ltp_vlm'),str('c_roltp_vlm'),str('info["C_CHG"]'),str('c_coi_nt'),str('c_rocoi_nt'),str('c_ltp_coi'),str('c_roc_ltp_coi'),str('info["C_B_QTY"]'),str('info["C_B_Price"]'),str('info["C_Ask_Price"]'),str('info["C_Ask_QTY"]'),str('info["SP"]'),str('info["P_B_QTY"]'),str('info["P_B_Price"]'),str('info["P_Ask_QTY"]'),str('info["P_Ask_Price"]'),str('info["P_CHG"]'),str('info["P_LTP"]'),str('p_roltp'),str('p_nt'),str('p_ront'),str('p_ltp_vlm'),str('p_roltp_vlm'),str('info["P_IV"]'),str('p_roiv'),str('info["P_T_Volume"]'),str('p_rov'),str('info["P_CH_OI"]'),str('p_rocoi'),str('info["P_OI"]'),str('p_roi'),str('p_coi_nt'),str('p_rocoi_nt'),str('p_ltp_coi'),str('p_roc_ltp_coi'),str(today.strftime("%d-%m-%Y")),str('c_roc_vol_roc_nt'),str('roc_c_roc_vol_roc_nt'),str('p_roc_vol_roc_nt'),str('roc_p_roc_vol_roc_nt'))
    db.session.add(data)
    db.session.commit()
    return str(data)

@app.route('/')
def home():
    animal = getData_bind()
    return render_template('sample.html', data=animal)

if __name__ == '__main__':
    app.run(debug=True)
