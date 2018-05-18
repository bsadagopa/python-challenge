
# coding: utf-8

# In[50]:


# Option 2: PyPoll
import os
import csv

input_data_1_csv = os.path.join("./", "election_data_1.csv")
input_data_2_csv = os.path.join("./", "election_data_2.csv")

files = [input_data_1_csv, input_data_2_csv]
#files = [input_data_1_csv]


# In[51]:


for file in files:
    print("--- Processing file: " + file + "---")
    
    #reset all data from the previous file processing
    # Lists to store data
    num_of_voters = 0
    candidate_dict = {}
    
    i = 0
    with open(file, newline="") as data_csvfile:
        
        #csvreader = csv.DictReader(data_csvfile)
        csvreader = csv.reader(data_csvfile, delimiter=",")
        for row in csvreader:
            
            #unit test code, need to be removed
            #if(i == 10):
            #    break
            #i = i+1
            #print("i = " + str(i))
            
            # skip the first row , header
            if row[0] == "Voter ID":
                #print("Skipping header row")
                continue
            num_of_voters = num_of_voters + 1
            
            #create dict with key = candidate : value to vote_count
            key = row[2]

            if(key in candidate_dict.keys()):
                #print("Adding Vote for:" + row[2])
                #increment the vote count for this candidate-county by one
                candidate_dict[key] += 1
            else: #new entry 
                #print("Adding new candidate :" + key)
                candidate_dict.update({key:1})
                #print("value = " + str(candidate_dict.get(key)))  
    
        print(candidate_dict)

    candidate_percentage_of_votes_dict = {}
    output_candidate_vote_record = ""
    for candidate in candidate_dict.keys():
        #print(candidate)
        vote_share_percentage = str('{0:.1%}'.format(candidate_dict.get(candidate) / num_of_voters))
        #candidate_percentage_of_votes_dict.update({candidate:'{0:.1%}'.format(candidate_dict.get(candidate) / num_of_voters)})
        output_candidate_vote_record += (f"{candidate}: {vote_share_percentage} ({candidate_dict.get(candidate)})\n")
    
    #print(output_candidate_vote_record)
    
    #
    # Last step to write output and print to files
    #
    output = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {num_of_voters}\n"
        f"----------------------------\n"
        f"{output_candidate_vote_record}"
        f"----------------------------\n"
        f"Winner: {max(candidate_dict, key=candidate_dict.get)}\n"
        f"----------------------------\n"
    )
    
    #printing to the console
    print(output)
    
    #write to output file - adding analysis to the file name
    outputfilename = "." + file.split(".")[1] + "_analysis.txt"
    print("Writing to " + outputfilename + "\n")
    
    with open(outputfilename, "w") as txt_file:
        txt_file.write(output)
            

