import os
import csv


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
        

    candidates = []
    for cand in listcandidates:
            if cand not in candidates:
                candidates.append(cand)


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


    percents = []

    for vote in votecounts:
        percent = (vote / votecount)*100
        roundpercent = round(percent, 3)
        percents.append(roundpercent)
    
    listlength = len(votecounts)
    winnerindex = 0
    winnervote = 0
    
    for i in range(listlength):
        if votecounts[i] > winnervote:
            winnervote = votecounts[i]
            maxIndex = i
   

    print("Election Results")
    print("-------------------------")
    print("Total Votes:" + str(votecount))
    print("-------------------------")
    print(candidates[0] + ": " + str(percents[0]) + "% (" + str(votecounts[0]) + ")")
    print(candidates[1] + ": " + str(percents[1]) + "% (" + str(votecounts[1]) + ")")
    print(candidates[2] + ": " + str(percents[2]) + "% (" + str(votecounts[2]) + ")")
    print(candidates[3] + ": " + str(percents[3]) + "% (" + str(votecounts[3]) + ")")
    print("-------------------------")
    print("Winner: %s" % (candidates[winnerindex]))
    print("-------------------------")

         
text_file = open("Output.txt", "w")
text_file.write("Election Results" +"\n" +
                "----------------------------" +"\n" +
                candidates[0] + ": " + str(percents[0]) + "% (" + str(votecounts[0]) + ")" + "\n" + 
                candidates[1] + ": " + str(percents[1]) + "% (" + str(votecounts[1]) + ")" + "\n" +
                candidates[2] + ": " + str(percents[2]) + "% (" + str(votecounts[2]) + ")" + "\n" +
                candidates[3] + ": " + str(percents[3]) + "% (" + str(votecounts[3]) + ")" + "\n" +
                "-------------------------" + "\n"
                "Winner: %s" % (candidates[winnerindex]) + "\n"
                "-------------------------")


