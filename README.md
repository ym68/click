# station_count

## env preparation  

virtualenv venpd  

cd venpd  

source ./bin/activate #Linux or  

  cd scripts & activate #Windows  

pip install pandas



## run data cleaning and analysis

### data cleaning with clean_connected.py and clean_rejected.py

save csv files under /csv and mind the path in clean_connected.py and clean_rejected.py  

copy .csv and rename as ana.csv

run  
python clean_connected.py  or clean_rejected.py   

get the results in the screen print and  

connected_cleaned.csv  or rejected_cleaned.csv  

if data cleaning is "Y".
"Y" means the End time is before what you expected.   
Then you will get the file to be analyzed as connected_cleaned.csv, or rejected_cleaned.csv.  

### run data analysis


run  
python count_connected.py   or  
python count_rejected.py   

to get the results both in the screen print and sum_connected.csv / sum_rejected.csv for the combined *_cleaned.csv file.  

run  
python clean_date.py  
to get a date_cleaned.csv  
then run  
python count_date.py  
to get the results by date
