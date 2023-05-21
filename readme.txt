
Group members :
   Group member1 :Zixuan Mi   
   Group member2: Yixin Xie 


Folders:


1.notebook :This folder contains three Jupyter notebooks:

  (a).web-scraping&sql1.ipynb : Do not run this notebook since this notebook is designed to run only once. The website we scrape updated every day. This file extracts data only on date 5/24/2021 and 5/25/2021.We already scrape the data for these two days and store these two cleaned dataframes in covid.sqlite
  
  (b).web-scraping&sql2.ipynb : This file is designed to scrape two-days-ago data on the website. Since the website updated everyday and only keep three continuous days' data(today, yesterday, and 2 days ago). The reason we only extract two-days-ago data is because it has the most complete data table. Run this file only if you want to append the cleaned dataframe from two days ago to the local database. 
  
  (c).Analyzing Dataset.ipynb : This is the main notebook which includes the data cleaning, data processing ,visualization and interactive visualization.



2.code :This folder contains two scripts and each script is a function written in python file

  (a).dataframe_clean.py :This file contains one function. This function takes in a dataframe and it deletes all the space in every cell of the dataframe.Then, it deletes all the comma in every string.Finally, it converted those string to integers so that it can be processed later.The function will processed every column except column Continent and date.In the end, the function returns the cleaned dataframe.
	

  (b).dataframe_organizer.py :This file contains one function. This function takes in dataframe and match each column of the dataframe with corresponding column names.Then, it drops irrelevant columns and set the column 'Country Name' as the index column.Finally, return the processed dataframe.




3.data: This folder contains one relational database

  (a).covid.sqlite :This database contains around 10 dataframes, each dataframe represents one day's data table.



