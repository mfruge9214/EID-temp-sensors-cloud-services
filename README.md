# EID-temp-sensors-cloud-services
Mike Fruge &amp; Bryan Cisneros, Emb. Interface Design Spring 21, Assignment 5

## Description

This project integrates the existing temperature/humidity sensors with AWS. Data is generated from
simulated temperature/humidity sensors as before, but this time the data is passed through a
rabbitmq queue. To make this a bit more interesting, we decided to generate the data on one
machine and pass the data over the internet to a remote gateway. The gateway then collects
the data from the sensors and sends it to AWS.

Data is received in AWS through an IoT Thing. There are several rules set up to store the incoming data
in DynamoDB, log the data to an SQS queue, and (if an alarm is detected) to send an email using SNS.
Note that the SNS functionality here is slightly different than the project description. The description
suggested using a Lambda function between IoT Thing and SNS, but we discovered that we could use an IoT
Thing Rule to go directly to SNS without even needing Lambda at all, so that's what we did.

There is also an AWS API Gateway that provides a REST API to get the last 10 measurements from the database.
This API using a Lambda function to retrieve the data from DynamoDB, format it, and then return it to the
user. The User can directly call this API, or can use the provided Sensor_Data_Get_Req.html web page. The 
latter approach is recommended.

## Execution Instructions

**Python Requirments:**
- Python 3.x

**Node.js Requirments:**
- Node.js v14.15.4

**RabbitMQ Requirments:**
- RabbitMQ 3.8.14

**Program Execution:**
- Run `python gateway.py` on the Raspberry Pi Gateway
- Run `node TempSensorApplication.js 3` on a different machine to simulate 3 temperature sensors
- open `Sensor_Data_Get_Req.html` from the project directory


## Assumptions

- We assume RabbitMQ is installed and running on the Raspberry Pi gateway and the machine
where the sensor data is generated.


