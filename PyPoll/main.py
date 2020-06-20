import os   
import csv

#Function to Draw the lines in output.
def drawline():
    for _ in range(20):
        print("-",end="")
    print("")

#opening and reading the csv file
cvspath = os.path.join('Resources','polling.csv')
opened_file = open(cvspath,encoding='utf8')
read_file = csv.reader(opened_file)

# converting the data into list of list
polling_data = list(read_file)

#total number of votes, Skipping the first row.
total_votes = len(polling_data[1:])

#dict for canditates as key and sum of their votes as value.
voting_list_dict = {}

for row in polling_data[1:]:
    if(row[2] in voting_list_dict):
        voting_list_dict[row[2]] =voting_list_dict[row[2]] + 1
    else:
        voting_list_dict[row[2]] = 1

#opening the text file in write mode.
text_file_path = os.path.join('Analysis','Result.txt')
text_file = open(text_file_path,'w')

#printing the result on terminal and writing it into the file also.
print("Election Results")
text_file.write("Election Results\n")

drawline()
text_file.write("--------------------\n")

print(f"Total Votes: {total_votes}")
text_file.write(f"Total Votes: {total_votes}\n")

drawline()
text_file.write("--------------------\n")

def Percentage(value):
    return round((value/total_votes) * 100,3)

for (key,value) in voting_list_dict.items():
    print(f"{key} : {Percentage(value)}% ({value})")
    text_file.write(f"{key} : {Percentage(value)}% ({value})\n")

drawline()
text_file.write("--------------------\n")

print(f"Winner: {max(voting_list_dict, key=voting_list_dict.get)}")
text_file.write(f"Winner: {max(voting_list_dict, key=voting_list_dict.get)}\n")

drawline()
text_file.write("--------------------\n")

#closing the text file.
text_file.close()