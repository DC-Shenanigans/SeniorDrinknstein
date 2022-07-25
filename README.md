# Se-orDrinknstein

Barbot software reposotory for the Rent an Assassin Party

This robot will be 3 rules safe. 

Porqe es muay rapido. 

Required features: 
- 9 relays for liquor/mixer pumps
- 3 relays for tower light
- 8 functional drink selection buttons (1 or 2 for easter egg)
- One screen for text output (i2c lcd, 20 x 4)
  - Screen will display current status of drink machine
    - Statuses:
      - Ready
      - Pouring
      - Drink done
      - Error


Drink List:

|Drink |Alcohol Amount| Mixer Amount | Button | 
--- | --- | --- | --- |
|Mai Tai| 59mL Rum|118mL Mai Tai Mixer| 0
|Pina Colada|59mL Rum| 118mL Pina Colada Mixer| 1
|Mango Daquiri|59mL Rum|118mL Mango Mixer| 2
|Margarita|59mL Tequila|118mL Marg. Mixer | 3
|Red Wine| 177mL Red Wine| N/A|4
|White Wine| 177mL White Wine| N/A|5
|Water| 177mL Water| N/A | 6
|Water| 177mL Water| N/A| 7


Pump List:

|Pump |Pump Contains|
--- | --- |
|Pump 0 |Rum|
|Pump 1 |Pina Colada Mixer|
|Pump 2 |Mango Daquiri Mixer|
|Pump 3 |Water
|Pump 4 |Tequila|
|Pump 5 |Margarita Mixer|
|Pump 6 |Mai Tai Mixer|
|Pump 7 |White Wine|
|Pump 8 |Red Wine|

GPIO Reference:

|GPIO Pin|Function|drink_name
--- | --- | --- | 
|GPIO 0| Screen - SDA| NA
|GPIO 1| Screen - SCL| NA
|GPIO 2 | Pump | rum 
|GPIO 3 | Pump | pina_colada 
|GPIO 4 | Pump | daqmix 
|GPIO 5 | Pump | water 
|GPIO 6 | Pump | tequila 
|GPIO 7 | Pump | margmix 
|GPIO 16 | Pump | maitaimix 
|GPIO 17 | Pump | whitewine 
|GPIO 19 | Pump | redwine 
|GPIO 8| Selection Button | Mai Tai
|GPIO 9| Selection Button | Pina Colada
|GPIO 10| Selection Button | Mango Daquiri
|GPIO 11| Selection Button | Margarita
|GPIO 12| Selection Button | Red Wine
|GPIO 13| Selection Button | White Wine
|GPIO 14| Selection Button | Water
|GPIO 15| Selection Button | Rum

Button Layout Reference:

[Button Layout](buttons.md)



