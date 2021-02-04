# Challenge: 
# 1º Clean/merge database
# 2º Estimate total pop by 'Nome_do_subdistrito'
# 3º Estimate pop exposed 'DNL_xx by 'NM_SUBIST'
import pandas as pd
import numpy as np
#import file/ separated by ;/index first col/ name of columns = first row. 
file = pd.read_csv('Domicilio01_DF.csv',sep=';', index_col=0, header = 0)

##### 1º Clean/merge database
#choose the right columns to analyse.
file_pop = file.iloc[:,51:60]
file_nn = file_pop

#clean data: remove "X"/ set int.
file_nn["V051"] = file_nn["V051"].str.replace("X", "0")
file_nn["V052"] = file_nn["V052"].str.replace("X", "0")
file_nn["V053"] = file_nn["V053"].str.replace("X", "0")
file_nn["V054"] = file_nn["V054"].str.replace("X", "0")
file_nn["V055"] = file_nn["V055"].str.replace("X", "0")
file_nn["V056"] = file_nn["V056"].str.replace("X", "0")
file_nn["V057"] = file_nn["V057"].str.replace("X", "0")
file_nn["V058"] = file_nn["V058"].str.replace("X", "0")
file_nn["V059"] = file_nn["V059"].str.replace("X", "0")
assert file_nn["V055"].str.contains('X').any() == False
#print(file_nn.head())
file_nn = file_nn.astype('int')

#residences to pop
file_nn["V051"] = file_nn["V051"]*1
file_nn["V052"] = file_nn["V052"]*2
file_nn["V053"] = file_nn["V053"]*3
file_nn["V054"] = file_nn["V054"]*4
file_nn["V055"] = file_nn["V055"]*5
file_nn["V056"] = file_nn["V056"]*6
file_nn["V057"] = file_nn["V057"]*7
file_nn["V058"] = file_nn["V058"]*8
file_nn["V059"] = file_nn["V059"]*9

#create a new column = sum of others w/o index (axis=1).
file_nn['total_pop'] = file_nn.sum(axis=1)

#import file/ separated by ;/index first col/ name of columns = first row/if the file have "Ç", use encoding cp1252 to read. 
data = pd.read_csv('Basico_DF.csv',sep=';', index_col=0, header = 0,encoding="cp1252")

#unique values for 'Nome_do_subdistrito'
data1 = data.drop_duplicates(subset = 'Nome_do_subdistrito')
data_b = data['Nome_do_subdistrito']

#merge Nome_do_subdistrito
left_dom_bas = file_nn.merge(data_b, on = 'Cod_setor', how = 'left')

#calculate mean pop by 'Nome_do_subdistrito'
total_pop_sub = left_dom_bas.groupby('Nome_do_subdistrito').agg({'sum', 'mean','count'})
total_1 = total_pop_sub['total_pop']
total_1_2 = total_1['mean'].mean()

#calculate mean pop by 'Nome_do_subdistrito' w/o null values, and replace null by mean.
left_dom_bas.loc[left_dom_bas['total_pop']==0,'total_pop'] = total_1_2

# 2º Estimate total pop by 'Nome_do_subdistrito'

MEAN =left_dom_bas.groupby('Nome_do_subdistrito').agg('sum')
TOTAL_POP_ESTIMATE= MEAN
print(TOTAL_POP_ESTIMATE['total_pop'])

#import pop_exp/merge on left_dom_bas
pop_exp = pd.read_csv('pop_exp2020.csv',sep=',', index_col=None, header = 0)
pop_exp = pop_exp.rename(columns={'CD_GEOCODI': 'Cod_setor'})

#CREATE NEW COLUMN DNL / MERGE DNL ON LEFT_DOM_BAS
d50 = pop_exp[pop_exp['NAME'] == 'DNL_50']
pop_exp_merge_d50 = d50.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d55 = pop_exp[pop_exp['NAME'] == 'DNL_55']
pop_exp_merge_d55 = d55.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d60 = pop_exp[pop_exp['NAME'] == 'DNL_60']
pop_exp_merge_d60 = d60.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d65 = pop_exp[pop_exp['NAME'] == 'DNL_65']
pop_exp_merge_d65 = d65.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d70 = pop_exp[pop_exp['NAME'] == 'DNL_70']
pop_exp_merge_d70 = d70.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d75 = pop_exp[pop_exp['NAME'] == 'DNL_75']
pop_exp_merge_d75 = d75.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d80 = pop_exp[pop_exp['NAME'] == 'DNL_80']
pop_exp_merge_d80 = d80.merge(left_dom_bas, on = 'Cod_setor', how = 'left')
d85 = pop_exp[pop_exp['NAME'] == 'DNL_85']
pop_exp_merge_d85 = d85.merge(left_dom_bas, on = 'Cod_setor', how = 'left')

#FILL N/A TOTAL_POP = MEAN POP
pop_exp_merge_d50['total_pop'] = pop_exp_merge_d50['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d55['total_pop'] = pop_exp_merge_d55['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d60['total_pop'] = pop_exp_merge_d60['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d65['total_pop'] = pop_exp_merge_d65['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d70['total_pop'] = pop_exp_merge_d70['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d75['total_pop'] = pop_exp_merge_d75['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d80['total_pop'] = pop_exp_merge_d80['total_pop'].fillna(total_1['mean'].min())
pop_exp_merge_d85['total_pop'] = pop_exp_merge_d85['total_pop'].fillna(total_1['mean'].min())

pop_50 = pop_exp_merge_d50.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_50['total_pop'])
pop_55 = pop_exp_merge_d55.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_55['total_pop'])
pop_60 = pop_exp_merge_d60.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_60['total_pop'])
pop_65 = pop_exp_merge_d65.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_65['total_pop'])
pop_70 = pop_exp_merge_d70.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_70['total_pop'])
pop_75 = pop_exp_merge_d75.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_75['total_pop'])
pop_80 = pop_exp_merge_d80.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_80['total_pop'])
pop_85 = pop_exp_merge_d85.groupby('Nome_do_subdistrito').agg({'sum'})
print(pop_85['total_pop'])
#save data into a new file/dont forget the index.
#left_dom_bas.to_csv(r'C:\Users\Lucas\Desktop\Sonora Engenharia\Aeroporto\Base informaçoes setores2010 universo DF\CSV/Domicilio01_DF_POP_Nome_subdist.csv', index_label = 'Cod_setor')

