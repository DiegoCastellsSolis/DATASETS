-- Cargar datos en la tabla vaccines
COPY vaccines(vaccine_id, name, manufacturer, dose_required, approval_date)
FROM '/ruta/a/vaccines.csv' DELIMITER ',' CSV HEADER;

-- Cargar datos en la tabla patient
COPY patient(patient_id, first_name, last_name, date_of_birth, gender, address, phone_number)
FROM '/ruta/a/patient.csv' DELIMITER ',' CSV HEADER;

-- Cargar datos en la tabla practice
COPY practice(practice_id, name, address, contact_number, email, opening_hours)
FROM '/ruta/a/practice.csv' DELIMITER ',' CSV HEADER;

-- Cargar datos en la tabla practice_patient
COPY practice_patient(practice_patient_id, practice_id, patient_id, registration_date)
FROM '/ruta/a/practice_patient.csv' DELIMITER ',' CSV HEADER;

-- Cargar datos en la tabla vaccinations
COPY vaccinations(vaccination_id, patient_id, vaccine_id, practice_id, vaccination_date, dose_number)
FROM '/ruta/a/vaccinations.csv' DELIMITER ',' CSV HEADER;

-- Cargar datos en la tabla claims
COPY claims(claim_id, vaccination_id, claim_date, amount, status)
FROM '/ruta/a/claims.csv' DELIMITER ',' CSV HEADER;
