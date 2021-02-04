# EID-temp-sensor-nodejs
Mike Fruge &amp; Bryan Cisneros, Emb. Interface Design Spring 21, Assignment 2

## Description

This application is plit into 2 main programs, a python application that monitors sensor progress, and a nodejs application that lauches a desired number of sensor processes to create data.
The data is then stored into a locally hosted (for this implementation) Microsoft SQL database. Data is created and the database updated every 10 seconds, for a 5 minute period. Every 30 seconds, the python monitor reads the database and writes sata to the console and text file. 
Graph.py can be run at any point to display a graph of current temperature readings from each sensor on a single plot, regardless of whether the run has finished or not.

## Execution Instructions

**Python Requirments:**
- Python 3.x
- pyodbc library (pip install pyodbc)
- matplotlib library (pip install matplotlib)

**Node.js Requirments:**
- Node.js v14.15.4
- mssql node package (npm install mssql)

**SQL Configuration:**
- Utilized MSSQL resources to create servers (localhost), databases, and tables for implementation
- Ensure that the proper database and table are given in Monitor.py and Database.js, otherwise errors will arise
- Make sure the SQL server protocols support TCP/IP coonnections, otherwise you will be unable to connect

**Program Execution:**
- 'node TempSensorApplication.js 4'
- 'python MonitorRoutine.py'


## Assumptions

- The desired database, table, and login information are valid upon application start. The application will not create a nonexistant table or DB, and will not be able to connect. 

