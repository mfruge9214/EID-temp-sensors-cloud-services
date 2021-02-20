# EID-temp-sensors-UI-realization
Mike Fruge &amp; Bryan Cisneros, Emb. Interface Design Spring 21, Assignment 2

## Description


This application features 2 different UI designs that the user may select upon application start.

Both Complex_UI_Routine and Simple_UI_Routine utilize the python Monitor API to retrieve data from a MSSQL database

After running 'python master.py', the application will launch a node process which creates 6 temperature sensors and populate the database with the created data.

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


** PyQT_5:**
- 'pip install PyQT_5' 
- Utilized Qt Designer to create both interfaces



**Program Execution:**
- 'python master.py'




## Assumptions

- The desired database, table, and login information are valid upon application start. The application will not create a nonexistant table or DB, and will not be able to connect. 

- We decided to implement alarm handling as a User side feature, rather than a sensor side feature. We did this to reduce the amount of moving parts in our application, as our table is still a 'one way path'

- We had to be creative with our use of existing QObjects in both UI designs, and assume both managers will see the intent of each element

