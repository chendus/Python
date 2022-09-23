from sqlalchemy import text
from sqlalchemy import create_engine
from datetime import datetime
import sqlalchemy
import pandas as pd
import MySQLdb

try:

  #setting up my connection
        conn = MySQLdb.connect(
                host="localhost",
                user="root",
                password="manager123",
                database="pollution-db2"
                )
        cur = conn.cursor()
        #connection to databar
        #deop database duplicate
        cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
        #create databae
        cur.execute("CREATE DATABASE `pollution-db2`")
        #cur.execute("SHOW DATABASES")
        cur.execute("USE `pollution-db2`")
        #read clean.csv selecting speicific columns
        df_stations_sql = pd.read_csv('clean.csv',sep=',',usecols=['SiteID','Location','geo_point_2d'])
        #drop duplicates
        df_stations_sql=df_stations_sql.drop_duplicates(keep='first')
        #read csv file for readings 
        df_readings_sql= pd.read_csv('clean.csv',sep=',',usecols=['Date Time','NOx','NO2','NO','SiteID','PM10','NVPM10','VPM10','NVPM2.5','PM2.5','VPM2.5','CO','O3','SO2','Temperature','RH','Air Pressure','DateStart','DateEnd','Current','Instrument Type'],low_memory=False)
        #drop duplicates
        df_readings_sql= df_readings_sql.drop_duplicates(keep='first')
        #set index for column
        df_readings_sql.index = df_readings_sql.index + 1
        #read SCHEMS.csv file
        df_schema_sql=pd.read_csv('SCHEMA.csv',sep=';',usecols=['Measure','Description','Unit'])
        df_schema_sql.index = df_schema_sql.index + 1
        
        #create engine from sqlalchemy
        engine=create_engine("mysql://root:manager123@localhost/pollution-db2?charset=utf8mb4")
        #populate data into the datbase
        df_schema_sql.to_sql(con=engine,name='schema', if_exists='append',index=True,index_label='schemaID')
        df_stations_sql.to_sql(con=engine,name='stations', if_exists='append',index=False)
        df_readings_sql.to_sql(con=engine,name='readings', if_exists='append',index=True,index_label='readingID',dtype={'Date Time': sqlalchemy.DateTime(), 'DateStart': sqlalchemy.DateTime(),'DateEnd': sqlalchemy.DateTime})
        
        
        # set primary and foreign key relationship
        with engine.connect() as con:
                
                alter_sql='''ALTER TABLE `pollution-db2`.`readings` 
                                CHANGE COLUMN `readingID` `readingID` BIGINT NOT NULL ,
                                      ADD PRIMARY KEY (`readingID`);'''
                alter2_sql='''ALTER TABLE `pollution-db2`.`stations` 
                                CHANGE COLUMN `SiteID` `SiteID` DOUBLE NOT NULL ,
                                    ADD PRIMARY KEY (`SiteID`);'''
                alter_3_sql='''ALTER TABLE `pollution-db2`.`schema` 
                                    CHANGE COLUMN `schemaID` `schemaID` BIGINT NOT NULL ,
                                        ADD PRIMARY KEY (`schemaID`);'''
                
                alter4_sql='''ALTER TABLE readings 
                                ADD FOREIGN KEY (`SiteID`) REFERENCES `pollution-db2`.stations(`SiteID`);'''
                #con.execute(alter2_sql)             
                con.execute(alter_sql)
                
                con.execute(alter_3_sql)                       
                con.execute(alter4_sql)
                con.close() 

        #dispose engine        
        engine.dispose()

except BaseException as err:
    print(f"An error ocurred: {err}")
