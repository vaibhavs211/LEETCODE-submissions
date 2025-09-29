# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM patients
WHERE conditions LIKE '% DIAB1%' or conditions LIKE 'DIAB1%';