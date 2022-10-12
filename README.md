# Price Advisor AI Model

This AI model seeks to help users do quick search on the favorite products that they want to buy or compare the prices. The model mines the price data from multiple site in kenya like 
[Jumia Kenya](https://www.jumia.co.ke/), [Kilomall Kenya](https://www.kilimall.co.ke/),
and [Sky Garden](https://sky.garden/home). The model does a mining a cross different sites and returns relevant highly rated products based on the user search thereby saving a lot of time in browsing for your favorite products.

- Built in Python version 3.x
- Uses [Airflow](https://airflow.apache.org/) for automating the ETL pipelines and processes.
- Uses [Scrapy](https://scrapy.org/) for Mining the products prices based on user price.
- Uses [RabbitMQ](https://www.rabbitmq.com/) for running processing task on the background.
- Uses [HBase](https://hbase.apache.org/) as the first warehouse for the mined data.
- Uses [PostgreSQL](https://www.postgresql.org/) as the DBMS for cleaned structured data.
- Uses [Flask Microframework](https://flask.palletsprojects.com/en/2.2.x/) as the server for taking user input and giving back output.
