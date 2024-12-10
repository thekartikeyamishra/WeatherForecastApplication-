import csv

def export_to_csv(data, filename="weather_data.csv"):

    with open(filename, mode ="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)