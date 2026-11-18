import csv

with open('job.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    counts = {}
    for row in reader:
        print(row)
        counts[row["status"]] = counts.get(row["status"], 0) + 1

print(counts)

with open('summary.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["status", "count"])
    writer.writeheader()
    for k, v in counts.items():
        writer.writerow({"status": k, "count": v})



