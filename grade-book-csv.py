import csv
with open("grade-book.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Manpreet Kaur",80])
    writer.writerow(["shivani",100])
    writer.writerow(["sukhan",35])
    writer.writerow(["Tamanna",60])
    writer.writerow(["Raman",70])

    