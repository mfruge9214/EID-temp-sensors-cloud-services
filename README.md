# EID-temp-sensors-UI-realization
Mike Fruge &amp; Bryan Cisneros, Emb. Interface Design Spring 21, Assignment 2

## Description

This application features 2 different web servers responding to the same html client, both of which serve the same data through different means.

The tornado web server retrieves data from the python Monitor, and the node websocket server interfaces directly with the SQL database to retrieve it's data.

After running 'python master.py', the application will launch a node process which creates 6 temperature sensors and populate the database with the created data. This will also launch both web servers and a user interface to view the data.

Lastly, the user may open "Sensor_Table.html" to interact with the webservers and view the generated data.

## Execution Instructions

**Python Requirments:**
- Python 3.x
- pyodbc library (pip install pyodbc)
- matplotlib library (pip install matplotlib)
- tornado webserver library		(pip install tornado)

**Node.js Requirments:**
- Node.js v14.15.4
- mssql node package (npm install mssql)
- websocket			(npm install websocket)

**SQL Configuration:**
- Utilized MSSQL resources to create servers (localhost), databases, and tables for implementation
- Ensure that the proper database and table are given in Monitor.py and Database.js, otherwise errors will arise
- Make sure the SQL server protocols support TCP/IP coonnections, otherwise you will be unable to connect


** PyQT_5:**
- 'pip install PyQT_5' 
- Utilized Qt Designer to create both interfaces



**Program Execution:**
- 'python master.py'
- open 'Sensor_Table.html' from the project directory




## Assumptions

- The desired database, table, and login information are valid upon application start. The application will not create a nonexistant table or DB, and will not be able to connect. 

- We decided to implement alarm handling as a User side feature, rather than a sensor side feature. We did this to reduce the amount of moving parts in our application, as our table is still a 'one way path'


