# Airport-noise-python
Using python to calculate population exposed to noise of brasilian's airport (Juscelino Kubitcheck)
Files: 

1 - Basico_DF: on this file we have the ID's of each sub-distric of Federal District and the name of cities, provided by IBGE's 2010 sensus

2 - Domicilio1_DF: on this file we have the number of residences with 1-9 residents and the ID of each sub-district, provided by IBGE's 2010 sensus.

3 - pop_exp2020: on this file we have the noise impact by DB range (DNL50 - DNL 85), the id of each sub-district and the name of respective city, provided by Sonora Engenharia (consulting company)

FIRST challenge: upload files/clean database/fillna/indexes/etc.

SECONT challenge: Calculate the total pop of each city, merging Basico_DF on Domicilio1_DF.

THIRD challenge: Calculate pop exposed of each city and each range: 50DB, 55DB, until 85DB.
