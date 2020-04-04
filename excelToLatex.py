'''
Code: 	
	Reading an Excel file consisting of values.
	This code generates equivalent Latex command where 
		the minimum or maximum values in a row are bold.
Parameters: 
	inputExcel:	Excel file from where the data is to be read
	and Minimum or maximum value is find row-wise.
	operator: Minimum or Maximum
	outputCSV: File in which output will be saved 
Author: Himanshu Mittal		
'''

import pandas as pd


def myFunction(excelName,findIntentation,writeFilename):
	df = pd.read_excel(excelName, header=None)
		
	listofzeros = ["\\\\"] * df.shape[0]
	df[df.shape[1]] = listofzeros

	df1=df.iloc[:,:].copy()

	for i in range(df.shape[0]):

		if findIntentation == 'min':
			df2=df1.iloc[i,:-1]
			ValueIndexObj=df2[df2 == df2.min()].dropna()
			for j in range(len(ValueIndexObj)):
				indx=ValueIndexObj.index[j]
				s1='\\textbf{'+str(df1.iloc[i,indx])+'}'
				df1.iloc[i,indx]=s1
		else:
			df2=df1.iloc[i,:-1]
			ValueIndexObj=df2[df2 == df2.max()].dropna()
			for j in range(len(ValueIndexObj)):
				indx=ValueIndexObj.index[j]
				s1='\\textbf{$'+str(df1.iloc[i,indx])+'$}'
				df1.iloc[i,indx]=s1

	df1 = df1.astype(str)

	df1.to_csv(writeFilename,sep='&', header=False, index=False) 

if __name__ == '__main__':
	inputExcel = 'sd.xlsx'
	operator = 'min'
	outputCSV = 'file1.csv'
	myFunction(inputExcel,operator,outputCSV)
