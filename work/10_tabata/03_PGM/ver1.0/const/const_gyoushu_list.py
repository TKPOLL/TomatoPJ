#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:42:59 2019

@author: tabatatoshinori
"""

#配列の1要素目：No
#配列の2要素目：業種コード
#配列の3要素目：業種名

#配列の4要素目：上位%の指定（実験する時はここの値のみを変更する）

CONST_GYOUSHU_LIST = [ 
    [1,"0050","水産・農林業",80],
    [2,"1050","鉱業",80],
    [3,"2050","建設業",80],
    [4,"3050","食料品",80],
    [5,"3100","繊維製品",80],
    [6,"3150","パルプ・紙",80],
    [7,"3200","化学",80],
    [8,"3250","医薬品",80],
    [9,"3300","石油・石炭製品",80],
    [10,"3350","ゴム製品",80],
    [11,"3400","ガラス・土石製品",80],
    [12,"3450","鉄鋼",80],
    [13,"3500","非鉄金属",80],
    [14,"3550","金属製品",80],
    [15,"3600","機械",80],
    [16,"3650","電気機器",80],
    [17,"3700","輸送用機器",80],
    [18,"3750","精密機器",80],
    [19,"3800","その他製品",80],
    [20,"4050","電気・ガス業",80],
    [21,"5050","陸運業",80],
    [22,"5100","海運業",80],
    [23,"5150","空運業",80],
    [24,"5200","倉庫・運輸関連業",80],
    [25,"5250","情報・通信業",80],
    [26,"6050","卸売業",80],
    [27,"6100","小売業",80],
    [28,"7050","銀行業",80],
    [29,"7100","証券、商品先物取引業",80],
    [30,"7150","保険業",80],
    [31,"7200","その他金融業",80],
    [32,"8050","不動産業",80],
    [33,"9050","サービス業",90]
]
    
print (CONST_GYOUSHU_LIST)