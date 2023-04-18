# About bytestock

![Bytestock logo](https://github.com/bytestock/.github/blob/main/profile/pics/bytestock-logo-red.png)

## What is bytestock?
 
***bytestock*** is a research website which publishes stock prices as well as an algorithmic tag which displays whether now is a good time to buy. 
 
You can find the GitHub code [here](https://github.com/bytestock). 
 
## Legal 
 
bytestock is solely a research project. We do not advise any financial decisions whatsoever. All information is publicly available and our website and core infrastructure is open source. We do not recommend taking any financial decisions based on any information provided by bytestock. 

## Objective

Run simulations to find out if there is a potential to predict where stock prices will be in the immediate future (5 to 30 days) based on recent price movements.

## Research Focused

Bytestock is a research project by [Slate](https://github.com/5late), [Ryan Alumkal](https://github.com/ryanalumkal), and [Nolawi Teklehaimanot](https://github.com/nolawiyonas1).

## Open Source

You can check out the code behind the [core program](https://github.com/bytestock/bytestock-core) or the [web interface](https://github.com/bytestock/bytestock-web).

## Write-Up

To read the documentation, click below.

 <details>

<summary>CLICK HERE TO READ DOCUMENTATION</summary>
<br>

## Table of Contents

### Website

- [Bytestock Website](#bytestock-website)
    - [Home](#home)
    - [About](#about)
    - [Live](#live)

#### Code

- [Bytestock](#bytestock)
  - [Objective](#objective)
  - [Research Focused](#research-focused)
  - [Open Source](#open-source)
  - [Write-Up](#write-up)
  - [Table of Contents](#table-of-contents)
    - [Website](#website)
      - [Code](#code)
- [Bytestock Website](#bytestock-website)
  - [Home](#home)
  - [About](#about)
  - [Live](#live)
- [Bytestock Core](#bytestock-core)
  - [``.gitignore``](#gitignore)
  - [``README.md``](#readmemd)
  - [``calc.go``](#calcgo)
    - [Functions:](#functions)
  - [``calculations.py``](#calculationspy)
  - [``data.py``](#datapy)
    - [Functions:](#functions-1)
  - [``go.mod``](#gomod)
  - [``main.py``](#mainpy)
  - [``market-closed-dates.txt``](#market-closed-datestxt)
  - [``misc.py``](#miscpy)
    - [Functions:](#functions-2)
- [Bytestock Web](#bytestock-web)
  - [pages](#pages)
    - [``About.py``](#aboutpy)
    - [``Live.py``](#livepy)
    - [``about.md``](#aboutmd)
    - [``stocks.txt``](#stockstxt)
  - [pics](#pics)
  - [streamlit](#streamlit)
    - [``config.toml``](#configtoml)
    - [``Home.py``](#homepy)
    - [``README.md``](#readmemd-1)

# Bytestock Website

## Home

Allows users to input a stock ticker of choice (Ex: AAPL) that they want to run simulations on to predict where stock prices will be in the immediate future (5 to 30 days) based on recent price movements. 

<!--- Image of page -->

## About

Provides information about bytestock and legal information regarding data provided by the site. 

<!--- Image of page -->

## Live

Provides live hourly updates on 18 popular tech-focused company stocks. 

![Live Stocks](https://github.com/bytestock/.github/blob/main/profile/pics/live-stocks.png)

If the stock has been falling, a red arrow along with red text showing the % the stock has been down for the day will be shown. If the stock has been rising, a green arrow along with green text showing the % the stock has been up for the day will be shown.

The data is cached hourly, meaning, the price information will be updated every hour and the user will not have to wait for the price to be fetched. 


# Bytestock Core

## ``.gitignore``

The gitignore file includes files that should not be pushed to the public github repository. These include but are not limited to files with sensitive information such as API keys and passwords, files that are unreadable such as binaries, and files that do not serve much purpose for others to see such as log files.

## ``README.md``

Provides information about 'Bytestock Core' including its objective.

## ``calc.go``

Calculations for stock simulations and predictions on stock price in the immediate future, written in Go.

### Functions:

```go
func readLines(path string) ([]string, error)
```

```go
func sum(arr []int) float64
```

```go
func average(array []float64) float64 
```

```go
func normalDist(weekly_ratio_average float64, weekly_ratio_standard_deviation float64) float64 
```

```go
func weekly_ratio_calculation(index int, close_data []float64) float64
```

```go
func weekly_ratio_average_calculations(weekly_ratio_values []float64, comparison int) float64
```

```go
func weekly_ratio_standard_deviation_calculation(weekly_ratio_values []float64, comparison int) float64
```

```go
func simulation_and_probability_calculations(index int, close_data []float64, weekly_ratio_average float64, weekly_ratio_standard_deviation float64, period int) (int, int)
```

```go
func main()
```

## ``data.py``

Uses [``yfinance``](https://pypi.org/project/yfinance/) library to get data from "Yahoo! Finance".

### Functions:

```python
def getOCHLData(ticker, days: int) ->list:
```
Parameters: 
- ticker: User requested stock ticker (Ex: AAPL)

- days: Number of days to be considered when fetching data, 1095 days (3 years) by default

Fetches data  including open days, daily open, daily close, daily adjusted close (used for the actual simulations), daily high, daily low values, and returns to ``main.py``.  

```python
def getRealTimeOCHL(ticker, days:int) ->list:
```
<!-- Is this the function for live stocks?-->
Parameters: 
- ticker: 

## ``go.mod``

This is the modules file. It is similar to a requirements.txt file for python and holds the names of all the modules/library needed for the program to run.

## ``main.py``

Main program of bytestock-core. 

Calls ``calculations.py`` and ``data.py`` files. 

Purpose of each function:
```python
def main()->None:
```

The main function of the program, asks user for preferred stock ticker. 

Holds values of various data fetched from ``data.py`` file including open days, daily open, daily close, daily adjusted close (used for the actual simulations), daily high, and daily low values.  

Calls calculation file ``calculations.py`` which runs simulations to find out if there is a potential to predict where stock prices will be in the immediate future (5 to 30 days) based on recent price movements.

## ``market-closed-dates.txt``

Lists all the dates the stock markets are closed to observe U.S. holidays

## ``misc.py``
<!--- Wait for function docstrings-->

### Functions:



```python
def getDateTimefromTicks(self):

This function gets the date from the ticks.
```

```python
def getFancyDateTimefromTicks(self):

This function gets the formatted date from the ticks.
```

```python
def getDayFromDate(self):

This function gets the day from the date.
```

```python
def getMarketCloseDates(self):

This function gets the market closed dates.
```

```python
def isMarketClosed(self):

This function checks if the market is closed.
```

```python
def wasMarketClosedFrom(self):

This function checks if the market was closed from a certain date.
```

```python
def telemetry(self):

This function logs everytime the user queries a stock.
```

# Bytestock Web

## pages

This folder holds files for every single page including about, live_crypto, live_stock, etc.

### ``About.py``

This file opens up the markdown file and writes each line to streamlit. Streamlit automatically creates the formatting for markdown.

### ``Live_Crypto.py``

This file is used to generate a live updating page of cryptocurrencies and their within-the-hour USD exchange rate.

### ``Live_Stock.py``

This file is used to generate a live updating page of select technology sector stocks and their within-the-hour USD price.

### ``about.md``

This file contains the actual about.md, and contains this documentation within it.

### ``stocks.txt``

This file contains a list of a stock tickers which are used by the [Live Stock](#Live_Stock.py) file.

## pics

This is a folder that contains pictures that are used in this documentation. They include the bytestock logo, and pictures of the website.

### ``Home.py``

This is the main file that runs the home page and links the other pages.

### ``README.md``

This is the README file used on github primarily.

</details>
