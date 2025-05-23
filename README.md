## Lab 1.1

### Introduction
The purpose of this lab is to practice fundamental Python skills. You will be using pandas built-in functions to read data and send it to different outputs (csv files, console).

#### Notes: 
Documentation for reading and writing files in pandas can be found here: 
https://pandas.pydata.org/docs/user_guide/io.html

When writing a file in pandas, you can change how the na is represented like this: df.to_csv('file.csv', na_rep='NULL')

While Python doesn't have an explicit "null" keyword like some other languages, the concept of null is represented by None. In the context of databases and data analysis, "null" generally refers to a missing or unknown value. Pandas uses NaN to represent null values in numeric columns and None or NaN in object columns. You will see "null" in database, .csv files, and other places.  


### Part 1
Read the `people.csv` file, and save it as `people_<yourLastName>.csv`. Verify that the data is formatted the same and no data was changed.  

### Part 2
Read the `people_no_header.csv` file, and save it as `people_header_added_<yourLastName>.csv`. Verify that the data is formatted the same and only the header was changed.

This is the header row that will need to be added:
**name,age,sex,height,weight,bmi,sibling_count,birth_order,years_played_sports**

### Part 3
Read the `people_dirty_header.csv` file, and save it as `people_clean_header_<yourLastName>.csv`. 
Verify that the data is formatted  and only the header was changed.

### Part 4
Read the `people_nulls.csv` file, and save it as `people_nulls_<yourLastName>.csv`. 
Verify that the data is formatted and nothing has changed. In this exercise, you will verify that you read in the data as a NaN.  

### Part 5
Read the `people_none.csv` file, and save it as `people_none_<yourLastName>.csv`. 
Take all of the values that are 'NONE' or NaN and change them to NULL. 

### Part 6
Read in the `file people_broken.csv`
- Add the correct header.
- Change any instance of NONE to NULL, 
- Change any 'null' text values to NULL

### Part 7
Read in the `mtcars.parquet` file and print its contents to the command line. Take a screenshot of the results.

### Part 8
Read in the `quiz.json` file and print its contents to the command line. Take a screenshot of the results. 

### Part 9
Read in the `menu.xml` file and print its contents to the command line. Take a screenshot of the results. 

#### Submission
Take all of the files that you created above and create a zipped folder called: `lab-1.1_<yourLastName>.zip`


