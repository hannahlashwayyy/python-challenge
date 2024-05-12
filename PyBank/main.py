import csv 

#define path to CSV file 
pybank_csv = "Resources/budget_data.csv"
#define path to print results in txt file 
output_file = "Analysis.txt"

#variables for months, Profits/Losses
month_count = 0
pf_sum_total = 0

#variables for Avg. Change
last_month_prof = 0
pf_change = []

#variables for max/min
month_change = []

  #open csv
with open(pybank_csv, encoding = 'UTF-8') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip header 
    next(csv_reader)
    #Loop through CSV rows   
    for row in csv_reader: 
       
        #count total months (should return 86)
        month_count += 1
   
        #sum Profits/Losses (should return 22564198)
        pf_sum = int(row[1])
        pf_sum_total += pf_sum
    
        #counting the number of changes (should be 85)
        #IF first row, no change 
        if (month_count == 1):
            last_month_prof = int(row[1])
        else: 
            change = int(row[1]) - last_month_prof
            pf_change.append(change)
            month_change.append(row[0])

            #reset last month prof
            last_month_prof = int(row[1])
        
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", month_count)
    print("Total: $", pf_sum_total) 
    print(len(pf_change))

    #now find average change in Profits/Losses
    #to get value we want, sub last month from current month
    #find avg of these values (should return $-8311.11) 
    #because there is a decimal, use a float val 
    avg_change = float(sum(pf_change)/len(pf_change))
    print ("Average Change: $", avg_change)

    max_change = max(pf_change)
    max_indx = pf_change.index(max_change)
    max_month = month_change[max_indx]

    print("Greatest Increase in Profits: ", max_month, " $", max_change)
    

    min_change = min(pf_change)
    min_indx = pf_change.index(min_change)
    min_month = month_change[min_indx]

    print("Greatest Decrease in Profits: ", min_month, " $", min_change)

    #printing and saving results to txt file
    with open(output_file, "w") as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("----------------------------\n")
        txt_file.write(f"Total Months: {month_count}\n")
        txt_file.write(f"Total: ${pf_sum_total}\n")
        txt_file.write(f"Average Change: ${round(sum(pf_change) / len(pf_change), 2)}\n")
        txt_file.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
        txt_file.write(f"Greatest Decrease in Profits: {min_month} (${min_change})\n")

    print("Results have been exported to", output_file)