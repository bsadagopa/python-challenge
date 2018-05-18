
# coding: utf-8

# In[1]:


# Option 1: PyBank
import os
import csv

input_data_1_csv = os.path.join("./", "budget_data_1.csv")
input_data_2_csv = os.path.join("./", "budget_data_2.csv")

files = [input_data_1_csv, input_data_2_csv]


# In[2]:


for file in files:
    print("--- Processing file: " + file + "---")
    
    #reset all data from the previous file processing
    # Lists to store data
    dates = []
    tot_num_months = []
    tot_revenue = 0
    prev_rev = 0
    chg_in_revenue = []
    inc_in_revenue_date = ""
    inc_in_revenue_amt = 0
    dec_in_revenue_date = ""
    dec_in_revenue_amt = 0
    
    with open(file, newline="") as data_csvfile:
        csvreader = csv.reader(data_csvfile, delimiter=",")
        for row in csvreader:
            #skip the first header row
            if row[0] == "Date":
                #print("Skipping header row")
                continue
            # Get the Date
            dates.append(row[0])
            #Add the revenue
            rev = int(row[1])
            tot_revenue = tot_revenue + rev
            
            #cal the av change in revenue
            chg_rev = rev - prev_rev
            chg_in_revenue.append(chg_rev)            
            #print("Rev = "+ str(rev) + "-- PrevRev = " + str(prev_rev) + "change =" + str(rev - prev_rev))
            if chg_rev > inc_in_revenue_amt:
                inc_in_revenue_amt = chg_rev
                inc_in_revenue_date = row[0]
            if chg_rev < dec_in_revenue_amt:
                dec_in_revenue_amt = chg_rev
                dec_in_revenue_date = row[0]
                
            prev_rev = rev

    output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(dates)}\n"
    f"Total Revenue: ${tot_revenue}\n"
    f"Average Revenue Change: ${sum(chg_in_revenue) / len(chg_in_revenue)}\n"
    f"Greatest Increase in Revenue: {inc_in_revenue_date} (${inc_in_revenue_amt})\n"
    f"Greatest Decrease in Revenue: {dec_in_revenue_date} (${dec_in_revenue_amt})\n")

    #printing to the console
    print(output)
    
    #write to output file - adding analysis to the file name
    outputfilename = "." + file.split(".")[1] + "_analysis.txt"
    print("Writing to " + outputfilename + "\n")
    
    with open(outputfilename, "w") as txt_file:
        txt_file.write(output)

