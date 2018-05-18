
# coding: utf-8

# In[138]:


# Option3: PyBoss
#import us_state_abbrev as state_codes
import importlib
import datetime as dt
import re
import os
import csv

# importing us_state_abbrev.py file containing all the US state code abbrevations
state_codes = importlib.import_module("us_state_abbrev")

input_data_1_csv = os.path.join("./", "employee_data1.csv")
input_data_2_csv = os.path.join("./", "employee_data2.csv")

files = [input_data_1_csv, input_data_2_csv]
#files = [input_data_1_csv]

output_file_header = (f"Emp ID,First Name,Last Name,DOB,SSN,State\n")

i = 0


# In[139]:


for file in files:
    print("--- Processing file: " + file + "---")
    with open(file, newline="") as data_csvfile:
        
#        if(i == 100):
#            break
#        else:
#            i += 1
        
        outputfilename = "." + file.split(".")[1] + "_analysis.txt"
        print("Writing to " + outputfilename + "\n")
        with open(outputfilename, "w") as txt_file:
                       
            #csvreader = csv.DictReader(data_csvfile)
            csvreader = csv.reader(data_csvfile, delimiter=",")
            for row in csvreader:

                #print(row)           

                # skip the first row , header
                #and print the first row of the output file
                if row[0] == "Emp ID":
                    #print("Skipping header row")
                    txt_file.write(output_file_header)
                    continue

                ssn_exp = re.compile(r'^\d{3}-\d{2}-')
                output = (
                    f"{row[0]}," 
                    f"{row[1].split()[0]},{row[1].split()[1]},"
                    f"{(dt.datetime.strptime(row[2], '%Y-%m-%d')).strftime('%m/%d/%Y')},"
                    f"{re.sub(ssn_exp, r'***-**-', row[3])},"
                    f"{state_codes.us_state_abbrev.get(row[4])}"
                    f"\n")

                txt_file.write(output)
                #print(output)
            

