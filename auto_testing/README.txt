This is a python script that automates the strategy testing on Trading-view.

This script is based on python and selenium.
Copy and paste this comand in the terminal to install selenium, if you don't have it:
python -m pip install selenium

How it works and how to use:

First it will ask for 3 values for the 10 setings, named v0 to v9.
v0min is the minimum seting
v0max is the maximum seting
i0 is the incrementation for the seting, how much the seting should add after each test. ex: v0min=1 v0max=10, i0=2, it will test the setings: v0 = 1, v0 = 3, v0 = 5, v0 = 7, v0 = 9 and v0 = 11
(I recomend using higher i because it reduces testing time. It takes forever anyway.)

it will ask for the minimum profit factor, Sharpe ratio and win percentage. If a specific set of setings achieves results higher than these results, the setings and the results will be writen in a .txt file named output.txt

after the webdriver is running, you need to log in and navigate to the chart you want to test.

After the script detects a chart is loaded, it will select the top indicator template.
    if you want to use a different one, paste the CSS_SELECTOR in line 114 of the main.py code.*

it will ask for the symbol and timeframe. This is just so it can organise the results in the output.txt file if you test multiple charts in the same session.

To start testing, you need to copy the XPATH to each input field in the strategy*, and paste it at XPATH0 = " " at line 25 and so on for each seting.
    if you don't have 10 setings, put the same XPATH in multiple inputs, but be sure to not add useless cycles to the testing(put v0min same as v0max and i = 1.)

After the testing is done, it will ask 'do you want to test another symbol or timeframe? ' if you type yes it will let you select a different timeframe or symbol and start testing.

* to copy a CSS_SELECTOR or XPATH, open the website on firefox, right click on the element > inpect > right click on the code that represents the element > copy > copy CSS_SELECTOR/XPATH


I know this code is far from perfect and it takes forever to go through all the setings but it is what it is.