import pandas as pd
import numpy as np
dfa=pd.read_csv('crop.csv',delimiter=';',low_memory=False, parse_dates=True)

# initialize list of lists
data1 = [[188,'AURN Bristol Centre'],[203,'Brislington Depot'],[206,'Rupert Street'],[209,'IKEA M32'],[213,'Old Market'],
[215,'Parson Street School'],[228, 'Temple Meads Station'],[270,'Wells Road'],[271,'Trailer Portway P&R'],
[375,'Newfoundland Road Police Station'],[395,"Shiner's Garage"],[452,'AURN St Pauls'],[447,'Bath Road'],
[459,'Cheltenham Road \ Station Road'],[463,'Fishponds Road'],[481,'CREATE Centre Roof'],[500,'Temple Way'],[501,'Colston Avenue']
]
 # Create the pandas DataFrame
dfstat = pd.DataFrame(data1, columns = ['SiteID', 'Location'])
dfstat = dfstat.set_index('SiteID')

#convert nanValue to Float
nanValue=float("NaN")
dfa.replace("",nanValue, inplace=True)
     
merged_df = dfa.merge(dfstat, how = 'inner', on = ['SiteID', 'Location'])
merged_df.head
merged_df.to_csv('clean.csv')