import csv

# Create CSV file
file = open("patients.csv", "w", newline="")

fields = ["ID", "age", "BMI", "blood_pressure", "glucose", "diabetes"]

writer = csv.DictWriter(file, fieldnames=fields)

writer.writeheader()

writer.writerow({
    "ID": 1,
    "age": 41,
    "BMI": 27,
    "blood_pressure": 60,
    "glucose": 120,
    "diabetes": "positive"
})

writer.writerow({
    "ID": 2,
    "age": 35,
    "BMI": 30,
    "blood_pressure": 50,
    "glucose": 180,
    "diabetes": "positive"
})

writer.writerow({
    "ID": 3,
    "age": 27,
    "BMI": 22,
    "blood_pressure": 45,
    "glucose": 110,
    "diabetes": "negative"
})

file.close()


# Read and display records

file = open("patients.csv", "r")

reader = csv.DictReader(file)

patients = []

for row in reader:
    patients.append(row)
    print(row)

file.close()


# Count positive and negative cases

positive = 0
negative = 0

for patient in patients:

    if patient["diabetes"] == "positive":
        positive += 1

    elif patient["diabetes"] == "negative":
        negative += 1

print("Positive cases:", positive)
print("Negative cases:", negative)


# Find patients with glucose above threshold

threshold = 150

print("Patients with glucose above", threshold)

for patient in patients:

    if int(patient["glucose"]) > threshold:
        print(patient)


# Calculate average BMI and glucose

total_bmi = 0
total_glucose = 0

for patient in patients:

    total_bmi += float(patient["BMI"])
    total_glucose += float(patient["glucose"])

average_bmi = total_bmi / len(patients)
average_glucose = total_glucose / len(patients)

print("Average BMI:", average_bmi)
print("Average glucose:", average_glucose)


# Add a new patient

file = open("patients.csv", "a", newline="")

writer = csv.DictWriter(file, fieldnames=fields)

writer.writerow({
    "ID": 4,
    "age": 50,
    "BMI": 29,
    "blood_pressure": 70,
    "glucose": 160,
    "diabetes": "positive"
})

file.close()

print("New patient added.")


# Update an existing patient

update_id = input("Enter ID to update: ")

file = open("patients.csv", "r")

reader = csv.DictReader(file)

patients = list(reader)

file.close()

found = False

for patient in patients:

    if patient["ID"] == update_id:

        patient["age"] = input("Enter new age: ")
        patient["BMI"] = input("Enter new BMI: ")
        patient["blood_pressure"] = input("Enter new blood pressure: ")
        patient["glucose"] = input("Enter new glucose: ")
        patient["diabetes"] = input("Enter new diabetes label: ")

        found = True
        break


if found == True:

    file = open("patients.csv", "w", newline="")

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerows(patients)

    file.close()

    print("Patient updated.")

else:
    print("Patient ID not found.")