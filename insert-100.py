from operator import index
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
import MySQLdb


try:
        conn = MySQLdb.connect(
                host="localhost",
                user="root",
                password="manager123",
                database="pollution-db2"
                )
        cur = conn.cursor()
        #connection to databae
        #cur.execute("DROP DATABASE IF EXISTS `pollution-db3`")
        #cur.execute("CREATE DATABASE `pollution-db3`")
        #cur.execute("SHOW DATABASES")
        #cur.execute("USE `pollution-db3`")
        #cur.execute("DROP DATABASE IF EXISTS `pollution-db3`")
        #cur.execute("CREATE DATABASE `pollution-db3`")
        #cur.execute("SHOW DATABASES")
        #cur.execute("USE `pollution-db3`")
        #create an engine
        engine=create_engine("mysql://root:manager123@localhost/pollution-db2?charset=utf8mb4")
        #read clean,csv file
        dfw=pd.read_csv('clean.csv',sep=',',low_memory=False)
        #drop
        dfz=dfw[:100]
        #dfy.to_csv('insert100.csv',index=False)
        #Read insert100.csv file to readings with the required columns
        dfr= pd.read_csv('insert100.csv',sep=',',usecols=['Date Time','NOx','NO2','NO','SiteID','PM10','NVPM10','VPM10','NVPM2.5','PM2.5','VPM2.5','CO','O3','SO2','Temperature','RH','Air Pressure','DateStart','DateEnd','Current','Instrument Type'],low_memory=False)
        #Read insert100.csv to stations file
        dfs = pd.read_csv('insert100.csv',sep=',',usecols=['SiteID','Location','geo_point_2d'])
        #drop duplicates
        dfs=dfs.drop_duplicates(keep='first')
        #drop duplicates
        dfr= dfr.drop_duplicates(keep='first')
        #set index column for reading table
        dfr.index = dfr.index + 1
        #raed SCHEMA.csv for schema table
        dfsch=pd.read_csv('SCHEMA.csv',sep=';',usecols=['Measure','Description','Unit'])
        dfsch.index = dfsch.index + 1
        
        #create engine #alchemy
        engine=create_engine("mysql://root:manager123@localhost/pollution-db2?charset=utf8mb4")
        #convert to tables
        dfsch.to_sql(con=engine,name='schema', if_exists='append',index=True,index_label='schemaID')
        dfs.to_sql(con=engine,name='stations', if_exists='append',index=False)
        dfr.to_sql(con=engine,name='readings', if_exists='append',index=True,index_label='readingID',dtype={'Date Time': sqlalchemy.DateTime(), 'DateStart': sqlalchemy.DateTime(),'DateEnd': sqlalchemy.DateTime})
        
        
        #alter tables to set the primary and foreign key
        with engine.connect() as con:
                
                alter_sql='''ALTER TABLE `pollution-db2`.`readings`, 
                                    ADD PRIMARY KEY (`readingID`);'''
                alter2_sql='''ALTER TABLE `pollution-db2`.`stations`,
                                ADD PRIMARY KEY (`SiteID`);'''
                alter_3_sql='''ALTER TABLE `pollution-db2`.`schema`,
                                ADD PRIMARY KEY (`schemaID`);'''
                
                alter4_sql='''ALTER TABLE readings 
                                ADD FOREIGN KEY (`SiteID`) REFERENCES `pollution-db2`.stations(`SiteID`);'''
                con.execute(alter2_sql)             
                con.execute(alter_sql)
                
                con.execute(alter_3_sql)                       
                con.execute(alter4_sql)
                con.close() 

        #dispose engine        
        engine.dispose()

except BaseException as err:
    print(f"An error ocurred: {err}")