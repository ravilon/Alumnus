--CREATE USER alumnus WITH PASSWORD 'Inter@1234' SUPERUSER;

CREATE TABLE ConectUser (
    ConectUserID Varchar(50) PRIMARY KEY,
    ConectUserName Varchar(50),
    ConectUserPassword Varchar(50),
    Role Varchar(50) 
);

CREATE TABLE Room (
    RoomID Integer PRIMARY KEY,
    RoomDesc Varchar(50)
);

CREATE TABLE Lesson (
    LessonID Varchar(50) PRIMARY KEY,
    Room Integer,
    Teacher Varchar(50),
    Discipline Varchar(50),
    StartTime Timestamp,
    EndTime Timestamp,
    EnergyConsumed Float,
	FOREIGN KEY (Room) REFERENCES Room(RoomId),
	FOREIGN KEY (Teacher) REFERENCES ConectUser(ConectUserID)
);

CREATE TABLE Lesson_ConectUser (
    LessonID Varchar(50),
    StudentID Varchar(50),
    Checkin Timestamp,
    Checkout Timestamp,
    PRIMARY KEY (LessonID, StudentID),
    FOREIGN KEY (LessonID) REFERENCES Lesson(LessonID),
    FOREIGN KEY (StudentID) REFERENCES ConectUser(ConectUserID)
);

