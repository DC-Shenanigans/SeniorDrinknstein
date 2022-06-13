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

|Drink |Alcohol Amount| Mixer Amount |
--- | --- | --- |
|Mango Daquiri|59mL Rum|118mL Mango Mixer|
|Pina Colada|59mL Rum| 118mL Pina Colada Mixer|
|Margarita|59mL Tequila|118mL Marg. Mixer|
|Mai Tai| 59mL Rum|118mL Mai Tai Mixer|
|White Wine| 177mL White Wine| N/A|
|Red Wine| 177mL Red Wine| N/A|


Pump List:

|Pump |Pump Contains|
--- | --- |
|Pump 0|Rum|
|Pump 1|Pina Colada Mixer|
|Pump 2|Mango Daquiri Mixer|
|Pump 3|Mai Tai Mixer|
|Pump 4|Tequila|
|Pump 5|Margarita Mixer|
|Pump 6|White Wine|
|Pump 7|Red Wine|
|Pump 8|Malort

GPIO Reference:

|GPIO Pin|Function|
--- | --- |
|GPIO 0|Screen - SDA|
|GPIO 1|Screen - SCL|
|GPIO 2|Pump 0 - Rum|
|GPIO 3|Pump 1 - Pina Colada Mixer|
|GPIO 4|Pump 2 - Mango Daquiri Mixer|
|GPIO 5|Pump 8 - Malort|
|GPIO 6|Pump 4 - Tequila|
|GPIO 7|Pump 5 - Margarita Mixer|

Button Layout Reference:

|Mai Tai|Pina Colada|Mango Daiquiri|Margarita|
|Red Wine|White Wine|Unused|Unusued|
