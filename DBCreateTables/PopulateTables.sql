-- Populating the CONNECTUSER table
INSERT INTO CONNECTUSER (USERID, NAME, PASSWORD, ROLE, EMAIL)
VALUES ('user1', 'John Doe', 'password1', 'student', 'john@example.com'),
       ('user2', 'Jane Smith', 'password2', 'teacher', 'jane@example.com'),
       ('user3', 'Admin User', 'password3', 'admin', 'admin@example.com');

-- Populating the ROOM table
INSERT INTO ROOM (ROOMID, ROOMDESC)
VALUES (1, 'Room A'),
       (2, 'Room B'),
       (3, 'Room C');

-- Populating the LESSON table
INSERT INTO LESSON (LESSONID, ROOM, TEACHER, DISCIPLINE, STARTTIME, ENDTIME, ENERGYCONSUMED)
VALUES ('lesson1', 1, 'user2', 'Mathematics', '2024-03-01 09:00:00', '2024-03-01 11:00:00', 50.5),
       ('lesson2', 2, 'user2', 'Science', '2024-03-01 13:00:00', '2024-03-01 15:00:00', 45.2),
       ('lesson3', 3, 'user2', 'History', '2024-03-02 10:00:00', '2024-03-02 12:00:00', 60.8);

-- Populating the LESSON_CONECTUSER table
INSERT INTO LESSON_CONECTUSER (LESSONID, STUDENTID, CHECKIN, CHECKOUT)
VALUES ('lesson1', 'user1', '2024-03-01 08:45:00', '2024-03-01 11:05:00'),
       ('lesson2', 'user1', '2024-03-01 12:45:00', '2024-03-01 15:05:00'),
       ('lesson3', 'user1', '2024-03-02 09:45:00', '2024-03-02 12:05:00');
