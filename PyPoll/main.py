import csv 

#define path to CSV file 
pypoll_csv = "Resources/election_data.csv"
#define path to print results in txt file 
output_file = "Analysis.txt"

#variable for vote count
vote_count = 0 

#variable/dictionary for candidate
candidate_dict = {}

with open(pypoll_csv, encoding = 'UTF-8') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip header 
    next(csv_reader)

    #Loop through CSV rows   
    for row in csv_reader: 
       
        #count total votes (should return 369711)
        vote_count += 1

        #add values to dictionary 
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else: 
            candidate_dict[row_candidate] = 1


    #output 
    output = f"""Election Results
    -------------------------
    Total Votes: {vote_count}
    -------------------------\n"""

    candidate_max = ""
    max_votes = 0 

    #loop and print each candidate name w/ percent of votes and total votes 
    for candidate in candidate_dict.keys():
        #get votes 
        votes = candidate_dict[candidate]
        percent = 100*(votes / vote_count)

        line = f"{candidate}: {round(percent, 3)}% ({votes})\n"
        output += line 

        #get max values 
        if votes > max_votes: 
                candidate_max = candidate
                max_votes = votes 

last_line = f"""-----------------------------
Winner: {candidate_max}
--------------------------------"""
output += last_line

print(output)

#printing and saving results to txt file
with open(output_file, "w") as txt_file:
        txt_file.write(output)
    
print("Results have been exported to", output_file)
    