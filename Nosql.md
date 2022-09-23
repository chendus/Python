Relational database have a hard time scaling. They have to maintain these process and requires a lot of memory and compute power.
Relational are scaled vertically and Nosql are scaled horizontally  whereas Nosql is scaled horizontally.
Horizontal scaling is like building a house and adding more floors to it thus proving it has limitations whereas vertical scaling is like add more new buildings in a vertical pattern and has no limits.
Duplicates are perfectly acceptable in Nosql 
Nosql  does not make use of a relational data model pattern. It commands flexible designs and its schemaless and output files are usually stored as jason files
Databse i used is couchbase
Unlike the sql,data is stored as collection of documents. 
I downloaded the couchebase installer app on my mac laptop and was able to connect to the server. The app was quite large and required a company email address to set up Whch i was able to get ,set up a new cluster and i was in my dashboard.
I made use of couchbase because it has built SQL features in it and it is free
I create a cluster then I created a unique document id  called  "rupert",the first monitor street with name Rupert monitor in the root collection to maintain the different keys and values. 
I named my key as 206 which is the corresponding value for the station id ,set type to integer and made set the value to station id.the value of the station id was my unique Id which functions as a foreign key keeping the relationship of the model.I ensured i used consistent naming in my documents so that my queries where easy to run. I created several monitors as a subcollections and their corresponding values. You cannot run a query across multiple user-as it is scoped for a particular user. So i denormalized my data and saved it as group collection
The query api is used to perform read and write operations.
i used the key/value query system by sending a value which was my unique ID and it returned all components in relation with my unique id showing their relationships.
I was able to insert and update my values using this query method.I also queried by searching for the full text which remember i stored consistently and result were displayed accordingly.
Majority of my queries where carried out in Nippl e whcich accomodates relational sql syntax
I went to the query tab and got a decent workbench,put on my query inthe query editor,clicked execute and got my results in jason format.
I also got the syntaxhighlighting and some autocompleted\s from the server .
I got a graphical view that confirmed my index to me.
I had extra features like the bump insights which showed me the shape of my data because i was using the Enteprise Edition.
it was a really helpful working environment
I went over to my terminal to run some few queries using the cbq command ,then the cbq history comand theni ran a query from rupert streent t limit1;
files where saved at my local host which i had set up a connection by runninga command.

I was able to run queries using the SELECT FROM ,INSERT and UPDATE my save files

