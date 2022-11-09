<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## DETAILED PROJECT DESCRIPTION

In this project, a Bayesian nonparametric kernel prediction algorithm in machine learning is applied to predict CO2, Methane, CFC emissions. A literature review has been conducted so that the proper independent variables have been identified. Classical least squares, robust least squares, and algorithms of the GPR were introduced and their prediction performance, including the evaluation criteria that are effective in the measurements for model performance, were summarized. The reliability and efficiency of the proposed algorithms were then demonstrated through the comparison between the actual data and the predicted results. It is found that GPR can give the most accurate predictions on Green House Gas (CO2, Methane, CFC emissions).

We did collect the earth data from NASA which is collected by using their satellites (Atmospheric Infrared Sounder (AIRS), Orbiting Carbon Observatory-2 (OCO-2), HIRDLS CFCs data from Earthdata Search) and along with that we have set two sensors(MQ2,TGS832) to measure emission rate of greenhouse gases. We recorded data from our IOT device through microcontroller and Lora gateway, we created a server side which helped us to get the time series data.
Then we merged earth data and the data we got from IOT setup and made a prediction through deep learning. We used Gaussian regression algorithm to get more accurate results. Then we connected this information to our website app which can generate a report and warning. So, Custom users can generate API key from our website.

Our solution is that we created a tool where everyone can know about particular GHG gases emission rate and compare between two small areas. Our application will also notify them in various ways. We will also share our data with government or non-government climate organization so that they can monitor and take necessary steps to control the emission rate of the particular Greenhouse gases.

## ADVANTAGES:
1. Our IoT setup can collect Greenhouse Gases data from little areas which can be compared with other data. It will help everyone to know that which areas are more prone to risks and where we should take steps.

2. Data is easily accessible for all type of users. They can track the daily data through our app.

3. Government and Non-Government organization can use our website’s API key to get all data and take important steps.


## SPACE AGENCY DATA

For Carbon Dioxide 
https://search.earthdata.nasa.gov/search?fi=OCO-2&fl=2%20-%20Geophys.%20Variables%2C%20Sensor%20Coordinates
https://search.earthdata.nasa.gov/search?fi=OCO-3&as%5binstrument%5d%5b0%5d=OCO-3
https://search.earthdata.nasa.gov/search?q=carbon%20dioxide&fi=AIRS

For Methane 
https://search.earthdata.nasa.gov/search?q=methane&fi=AIRS

For CFC 
https://search.earthdata.nasa.gov/search?fi=HIRDLS&fs10=Halocarbons%20And%20Halogens&fsm0=Atmospheric%20Chemistry&fs20=Chlorofluorocarbons&fst0=Atmosphere


### REFERENCES TOOLS USED:
 1. Google Colab for Deep Learning
 2. Microcontroller (Arduino Nano 33BLE)
 3. Sensors(MQ-2, TGS832)
 4. Visual Studio Code 
 5. Php
 6. https://climate.nasa.gov/
 7. MySql


