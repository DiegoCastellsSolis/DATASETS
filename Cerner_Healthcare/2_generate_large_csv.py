import csv
import random
from datetime import datetime, timedelta

# Funciones para generar datos aleatorios
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_vaccines_csv(file_path, num_records):
    vaccines = [
        ("Comirnaty (Pfizer-BioNTech)", "Pfizer", 2),
        ("Moderna COVID-19 Vaccine", "Moderna", 2),
        ("Janssen COVID-19 Vaccine", "Johnson & Johnson", 1),
        ("AstraZeneca", "AstraZeneca", 2)
    ]
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["vaccine_id", "name", "manufacturer", "dose_required", "approval_date"])
        for i in range(1, num_records + 1):
            vaccine = random.choice(vaccines)
            approval_date = random_date(start_date, end_date)
            writer.writerow([i, vaccine[0], vaccine[1], vaccine[2], approval_date.date()])

def generate_patient_csv(file_path, num_records):
    first_names = ["John", "Jane", "Alex", "Chris", "Pat", "Taylor", "Sam", "Jordan"]
    last_names = ["Smith", "Doe", "Johnson", "Lee", "Brown", "Davis", "Martinez", "Garcia"]
    start_date = datetime(1940, 1, 1)
    end_date = datetime(2022, 12, 31)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["patient_id", "first_name", "last_name", "date_of_birth", "gender", "address", "phone_number"])
        for i in range(1, num_records + 1):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            date_of_birth = random_date(start_date, end_date)
            gender = random.choice(['M', 'F', 'O'])
            address = f"{random.randint(1, 999)} Main St"
            phone_number = f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            writer.writerow([i, first_name, last_name, date_of_birth.date(), gender, address, phone_number])

def generate_practice_csv(file_path, num_records):
    practice_names = ["Health Clinic A", "Family Medical Center", "Wellness Center", "Primary Health Group"]
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["practice_id", "name", "address", "contact_number", "email", "opening_hours"])
        for i in range(1, num_records + 1):
            name = random.choice(practice_names)
            address = f"{random.randint(1, 999)} Clinic St"
            contact_number = f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            email = f"info{random.randint(1, 100)}@practice.com"
            opening_hours = "9:00-17:00"
            writer.writerow([i, name, address, contact_number, email, opening_hours])

def generate_practice_patient_csv(file_path, num_records, max_patient_id, max_practice_id):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["practice_patient_id", "practice_id", "patient_id", "registration_date"])
        for i in range(1, num_records + 1):
            practice_id = random.randint(1, max_practice_id)
            patient_id = random.randint(1, max_patient_id)
            registration_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
            writer.writerow([i, practice_id, patient_id, registration_date.date()])

def generate_vaccinations_csv(file_path, num_records, max_patient_id, max_practice_id, max_vaccine_id):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["vaccination_id", "patient_id", "vaccine_id", "practice_id", "vaccination_date", "dose_number"])
        for i in range(1, num_records + 1):
            patient_id = random.randint(1, max_patient_id)
            vaccine_id = random.randint(1, max_vaccine_id)
            practice_id = random.randint(1, max_practice_id)
            vaccination_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
            dose_number = random.randint(1, 3)
            writer.writerow([i, patient_id, vaccine_id, practice_id, vaccination_date.date(), dose_number])

def generate_claims_csv(file_path, num_records, max_vaccination_id):
    statuses = ["Pending", "Approved", "Denied"]
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["claim_id", "vaccination_id", "claim_date", "amount", "status"])
        for i in range(1, num_records + 1):
            vaccination_id = random.randint(1, max_vaccination_id)
            claim_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
            amount = round(random.uniform(50, 200), 2)
            status = random.choice(statuses)
            writer.writerow([i, vaccination_id, claim_date.date(), amount, status])

# Generar archivos CSV con un mayor volumen de datos
generate_vaccines_csv("vaccines.csv", 1000)
generate_patient_csv("patient.csv", 5000)
generate_practice_csv("practice.csv", 100)
generate_practice_patient_csv("practice_patient.csv", 5000, 5000, 100)
generate_vaccinations_csv("vaccinations.csv", 10000, 5000, 100, 1000)
generate_claims_csv("claims.csv", 10000, 10000)
