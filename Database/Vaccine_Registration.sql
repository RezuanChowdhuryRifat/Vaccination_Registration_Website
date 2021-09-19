create table Address(
    ID int primary key,
    Street_Address varchar(300) not null,
    Upazilla_City_Corporation varchar(50) not null,
    Ward_No int not null,
    District varchar(50) not null,
    Unionn varchar(50),
    index(ID, Ward_No, District)
);

create table NID(
    id bigint(10) primary key,
    FName varchar(100),
    LName varchar(100),
    dob DATE not null,
    Fathers_Name varchar(150),
    Mothers_Name varchar(150),
    Address_ID int,
    CONSTRAINT NID_fk foreign key(Address_ID) references Address(ID)
    on update CASCADE
    on delete CASCADE,
    index(ID, LName, DOB, Address_ID)
);

create table Student(
    NID_ID bigint(10) primary key,
    University_Name varchar(200) not null,
    CONSTRAINT Student_fk foreign key(NID_ID) references NID(ID)
    on update CASCADE
    on delete CASCADE,
    Index(NID_ID, University_Name)
);

create table Medical_Personel(
    NID_ID bigint(10) primary key,
    Medical_Institution_Name varchar(200) not null,
    CONSTRAINT MP_fk foreign key(NID_ID) references NID(ID)
    on update CASCADE
    on delete CASCADE,
    index(NID_ID, Medical_Institution_Name)
);

create table Government_Employee(
    NID_ID bigint(10) primary key,
    Department varchar(150) not null,
    Job_Title varchar(100) not null,
    CONSTRAINT GE_fk foreign key(NID_ID) references NID(ID)
    on update CASCADE
    on delete CASCADE,
    index(NID_ID, Department)
);



create table Volunteering(
    NID_ID bigint(10) primary key,
    Organization varchar(150) not null,
    Job_Title varchar(100) not null,
    CONSTRAINT V_fk foreign key(NID_ID) references NID(ID)    
    on update CASCADE
    on delete CASCADE,
    index(NID_ID, Organization)
);

create table citizen(
    NID_ID bigint(10) primary key,
    Occupation varchar(200) not null,
    Job_Title varchar(100),
    CONSTRAINT Citizen_fk foreign key(NID_ID) references NID(ID)
    on update CASCADE
    on delete CASCADE,
    index(NID_ID, Occupation)
);


create table Center_Address(
    ID int primary key,
    Street_Address varchar(300) not null,
    Upazilla_City_Corporation varchar(50) not null,
    Ward_No int not null,
    District varchar(50) not null,
    Unionn varchar(50),
    index(ID, Ward_No, District)
);

create table Center(
    Center_ID int(9) primary key,
    Center_Name varchar(300) not null,
    Center_Address_ID int,
    constraint Center_fk foreign key(Center_Address_ID) references Center_Address(ID)
    on update CASCADE
    on delete CASCADE,
    index(Center_ID, Center_Address_ID)
    );

create table registration(
    NID bigint(10) primary key,
    Date Timestamp not null DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Center_ID int(9),
    Mobile_No int,
    Age int not null,
    CONSTRAINT R_fk1 foreign key(NID) references NID(ID) 
    on update CASCADE
    on delete CASCADE,
    CONSTRAINT R_fk2 foreign key(Center_ID) references Center(Center_ID)
    on update CASCADE
    on delete CASCADE,
    unique(Mobile_No, Center_ID),
    index(NID, Center_ID, Mobile_No)    
);

create table otp(
    otpkey int 
);
create table categorylist(
list varchar(50)
);