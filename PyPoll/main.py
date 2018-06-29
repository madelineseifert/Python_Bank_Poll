import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('election_data.csv')

with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    votecount = 0
    listcandidates = []

    for row in csvreader:
        votecount = votecount + 1
        candidate = row[2]
        listcandidates.append(candidate)
        #for candidate in listcandidates:
            #if candidate not in listcandidates:
                #listcandidates.append(candidate)        
                               
    print(votecount)
    candidates = []
    for cand in listcandidates:
            if cand not in candidates:
                candidates.append(cand)
    print(candidates)

    votecounts = [0, 0, 0, 0]

    for cand in listcandidates:
        if cand == candidates[0]:
            votecounts[0] += 1
        elif cand == candidates[1]:
            votecounts[1] += 1
        elif cand == candidates[2]:
            votecounts[2] += 1
        else:
            votecounts[3] += 1           
    print(votecounts)

    percents = []

    for vote in votecounts:
        percent = (vote / votecount)*100
        roundpercent = round(percent, 3)
        percents.append(roundpercent)
    
    print(percents)
    results = zip(votecounts, candidates, percents)
    print(results)
    

