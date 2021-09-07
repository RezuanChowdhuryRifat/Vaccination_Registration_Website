INSERT INTO address(ID, Street_Address, Upazilla_City_Corporation, Ward_No, District, Unionn)
VALUES(1, 'House No.-92, Moneshwar Rd, Zigatola', 'Dhaka South City Corporation', 11, 'Dhaka', ''),
(2, ' House No.-33/B, Rd No.-4, Dhanmondi', 'Dhaka South City Corporation', 15, 'Dhaka', 'NULL'),
(3, 'House No.-31/A, Rd No. 6, Dhanmondi', 'Dhaka South City Corporation', 15, 'Dhaka', 'NULL'),
(4, 'House No.-5, Road No.-5, Block No.-E, Lalmatia', 'Dhaka South City Corporation', 32, 'Dhaka', 'NULL'),
(5, ' House-3G, Road No.-104, Gulshan-2', 'Dhaka North City Corporation', 18, 'Dhaka', 'NULL');

INSERT INTO center_address(ID, Street_Address, Upazilla_City_Corporation, Ward_No, District, Unionn)
VALUES(1, '1a Hazaribagh Rd', 'Dhaka South City Corporation', 11, 'Dhaka', 'NULL'),
(2, 'Shahbag Road', 'Dhaka South City Corporation', 21, 'Dhaka', 'NULL'),
(3, '319 Isakha Ave', 'Dhaka North City Corporation', 01, 'Dhaka', 'NULL'),
(4, 'Sher-E-Bangla Nagar', 'Dhaka North City Corporation', 27, 'Dhaka', 'NULL'),
(5, 'Pilkhana Road', 'Dhaka South City Corporation', 23, 'Dhaka', 'NULL');

INSERT INTO center(Center_ID, Center_Name, Center_Address_ID)
VALUES(264923041, 'Nagar Matri Sadan', 1),
(582216709, 'Bangabandhu Sheikh Mujib Medical University Hospital (BSMMU)', 2),
(525200792, 'Kuwait Bangladesh Friendship Hospital(Uttara)', 3),
(413526234, 'Shaheed Sarwardi Medical College and Hospital', 4),
(598595316, 'BGB Hospital', 5);

INSERT INTO NID(id, FName, LName, dob, Fathers_Name, Mothers_Name, Address_ID)
VALUES(3123222287, 'Yashfinul', 'Haque', '2000-02-12', 'Late Md. Wahidul Haque', 'Farhana Haque', 1),
(3380786777, 'Rezuan', 'Chowdhury', '1998-07-24', 'Md. Lutfor Chowdhury', 'Rehana Chowdhury', 2),
(7842237733, 'Asfaria', 'Chowdhury', '1999-08-11', 'Md. Maruf Chowdhury', 'Nazmur Nahar Begum', 3),
(8804627056, 'Faiza', 'Akhter', '2000-01-06', 'Late Md. Sefayatul Akhter', 'Adiba Akhter', 4),
(1889910484, 'Zaqa Zeeshan', 'Saif', '2000-06-29', 'Md. Ashraf Saif', 'Fatima Saif', 5);

INSERT INTO Registration(NID, Date, Center_ID, Mobile_No, Age)
VALUES();

INSERT INTO Student(NID_ID, University_Name)
VALUES(3123222287, 'North South University'),
(3380786777, 'North South University');

INSERT INTO Citizen(NID_ID, Occupation, Job_Title)
VALUES(7842237733, 'Engineer', 'Full-Stack Developer');

INSERT INTO government_employee(NID_ID, Department, Job_Title)
VALUES(8804627056, 'NBR', 'Manager');

INSERT INTO medical_personel(NID_ID, Medical_Institution_Name)
VALUES(1889910484, 'United Hospital Limited');

INSERT INTO volunteering(NID_ID, Organization, Job_Title)
VALUES();