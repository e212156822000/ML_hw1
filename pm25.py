import numpy as np
import pandas as pd
import csv

######################################前處理######################################

df = pd.read_csv("train.csv", encoding = "big5")
titles = df["測項"].head(18)
feature_num = 18
#設定
# x 為前九個小時的氣象資料 18*9 的array list
x = []
#用於concate
x_prev = [] #前半段的data
x_post = [] #後半段的data
x_temp = []
# y 為每個第10個小時的pm2.5值
y = []
# 先不做最後一個set
for i in range(0,len(df)-feature_num,feature_num): #移動20天的dataset #len(df)-feature_num
	for j in range(0,24): #一次移動9個小時
		#切割長度固定為18 = i:i+feature_num-1
		slice_end_index = i+feature_num-1
		if(j+8 > 23): #要跳到下排去去值了
			slice_length = j+8-23
			df_prev = df.loc[i:i+feature_num-1, str(j):"23"]
			df_post = df.loc[i+feature_num:i+2*feature_num-1, "0":str(slice_length-1)]
			dfs = [df_prev, df_post]
			result = pd.concat([df.set_index(titles) for df in dfs], axis=1)
			x.append(result)
			y.append(df[str(slice_length)][9+i+feature_num])
		else:
			x.append(df.loc[i:i+feature_num-1, str(j):str(j+8)])
			#下一個小時的pm2.5值
			if(j+9 > 23):
				y.append(df["0"][9+i+feature_num]) 	
			else:
				y.append(df[str(j+9)][9+i])
		x_prev = []
		x_post = []
		x_temp = []
#處理最後一行
i += feature_num
for j in range(0,15):
	x.append(df.loc[i:i+feature_num-1, str(j):str(j+8)])
	y.append(df[str(j+9)][9+i])
# 印出資料確認是否正確
# print(x[-11:])
# print(y[-11:])

######################################開始Train######################################

# z = np.zeros(len(x),len(y))
# X,Y = np.
# a = np.array(x)
# print(a.shape)
# print(x[0:1].shape())