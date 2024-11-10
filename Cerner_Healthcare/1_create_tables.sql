CREATE TABLE vaccines (
    vaccine_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    dose_required INT CHECK (dose_required > 0),
    approval_date DATE
);


CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    address VARCHAR(255),
    phone_number VARCHAR(15)
);


CREATE TABLE practices (
    practice_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(15),
    email VARCHAR(100),
    opening_hours VARCHAR(50)
);


CREATE TABLE vaccinations (
    vaccination_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    vaccine_id INT NOT NULL,
    practice_id INT NOT NULL,
    vaccination_date DATE NOT NULL,
    dose_number INT CHECK (dose_number > 0),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (vaccine_id) REFERENCES vaccines(vaccine_id),
    FOREIGN KEY (practice_id) REFERENCES practices(practice_id)
);


CREATE TABLE practice_patients (
    practice_patient_id SERIAL PRIMARY KEY,
    practice_id INT NOT NULL,
    patient_id INT NOT NULL,
    registration_date DATE NOT NULL,
    FOREIGN KEY (practice_id) REFERENCES practices(practice_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    UNIQUE (practice_id, patient_id)
);



CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY,
    vaccination_id INT NOT NULL,
    claim_date DATE NOT NULL,
    amount NUMERIC(10, 2) CHECK (amount >= 0),
    status VARCHAR(50) CHECK (status IN ('Pending', 'Approved', 'Denied')),
    FOREIGN KEY (vaccination_id) REFERENCES vaccinations(vaccination_id)
);
