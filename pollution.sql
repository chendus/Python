#drop database POLLUTION;
CREATE DATABASE pollution;
USE pollution;
CREATE TABLE `schema` (measure varchar(32)  primary key, 
					   `description` varchar(64) DEFAULT NULL UNIQUE, 
					   unit varchar(24) NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;                     
CREATE TABLE  stations (
  Stationid int(11) primary key,
  Location varchar(48) DEFAULT  NULL,
  geo_point_2d varchar(32)  NOT NULL)
 ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;                     

CREATE TABLE `readings`  (
  readingid int(11)  NOT NULL PRIMARY KEY,
  `DateTime` datetime DEFAULT  NULL,
  NOx float DEFAULT NULL,
  NO2 float DEFAULT NULL,
  `NO` float DEFAULT NULL,
  SiteID int(11)  DEFAULT NULL,
  PM10 float DEFAULT NULL,
  NVPM10 float DEFAULT NULL,
  `NNPM2.5` float DEFAULT NULL,
  CO float DEFAULT NULL,
  O3 float DEFAULT NULL,
  SO2 float DEFAULT NULL,
  Temperature REAL DEFAULT NULL,
  RH float DEFAULT NULL,
  AirPressure float DEFAULT NULL,
  DateStart datetime DEFAULT NULL,
  DateEnd datetime DEFAULT NULL,
  `Current` text  DEFAULT NULL,
  InstrumentType varchar(32) DEFAULT NULL,
  Stationid int(11),
  FOREIGN KEY (stationid) REFERENCES stations(stationid))
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                       
    
