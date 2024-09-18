DELETE FROM test_datas;
DELETE FROM questions;
DELETE FROM practice_sections;
DELETE FROM learns;
DELETE FROM categorys;
DELETE FROM subjects;

INSERT OR IGNORE INTO auth_user
(password, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name)
VALUES ('1234', 0, 'test@test.com', 'McTest', 'test@test.com', 0, 1, '1970-01-01 00:00:00', 'Test');

INSERT INTO subjects
(name, description, user_id)
VALUES 
('Spanish', 'Learn Spanish', 1),
('French', 'Learn French', 1),
('Stuff', 'Learn Stuff', 2);

INSERT INTO categorys
(name, subject_id, user_id)
VALUES 
('Subjunctive', 1, 1),
('Greetings', 1, 1),
('Days', 2, 1),
('Stuff', 1, 2);

INSERT INTO learns
(name, author, body, date_created, category_id, user_id)
VALUES 
('Espero que', 'Matt Clifford', 'Test body of learns', '2024-09-18 14:05:00', 1, 1),
('Hasta que', 'Matt Clifford', 'Test body of learns two', '2024-09-18 14:07:00', 1, 1),
('Antes de que', 'Matt Clifford', 'Test body of learns three', '2024-09-18 14:09:00', 1, 1),
('Hola', 'Matt Clifford', 'Test body of learns hola', '2024-09-18 14:05:00', 2, 1),
('Adios', 'Matt Clifford', 'Test body of learns adios', '2024-09-18 14:05:00', 2, 1),
('Monday', 'Matt Clifford', 'Test body of learns Mondat', '2024-09-18 14:05:00', 3, 1),
('Stuff to learn', 'Matt Clifford', 'Test body of stuff to learn', '2024-09-18 14:05:00', 1, 2);

INSERT INTO practice_sections
(instruction, learn_id, user_id)
VALUES ('Write your answer', 1, 1),
('Select the correct one', 2, 1),
('Listen and write', 3, 1),
('Write your answer', 4, 1),
('Select the correct one', 5, 1),
('Listen and write', 6, 1),
('Write your answer', 7, 2)
;

INSERT INTO questions
(test_type, question, answer, option_one, option_two, option_three, feedback, practice_section_id, user_id)
VALUES 
-- 17 Questions for user_id = 1 (practice_section_id between 1 and 6)
(1, 'What is 2+2?', '4', '3', '4', '5', 'Correct!', 1, 1),
(2, 'What is the capital of France?', 'Paris', 'Rome', 'Paris', 'Berlin', 'Correct!', 2, 1),
(3, 'What is the chemical symbol for water?', 'H2O', 'HO', 'H2O', 'O2', 'Correct!', 3, 1),
(1, 'Who wrote "Hamlet"?', 'Shakespeare', 'Dante', 'Shakespeare', 'Cervantes', 'Correct!', 4, 1),
(2, 'What is the largest planet in our solar system?', 'Jupiter', 'Earth', 'Jupiter', 'Mars', 'Correct!', 5, 1),
(3, 'What is 5 multiplied by 6?', '30', '25', '30', '35', 'Correct!', 6, 1),
(1, 'What is the boiling point of water?', '100°C', '90°C', '100°C', '110°C', 'Correct!', 1, 1),
(2, 'Who painted the Mona Lisa?', 'Leonardo da Vinci', 'Michelangelo', 'Leonardo da Vinci', 'Raphael', 'Correct!', 2, 1),
(3, 'What is the speed of light?', '299,792,458 m/s', '150,000,000 m/s', '299,792,458 m/s', '1,000,000 m/s', 'Correct!', 3, 1),
(1, 'What is the square root of 64?', '8', '7', '8', '9', 'Correct!', 4, 1),
(2, 'What is 10 divided by 2?', '5', '6', '5', '4', 'Correct!', 5, 1),
(3, 'What is the freezing point of water?', '0°C', '-5°C', '0°C', '5°C', 'Correct!', 6, 1),
(1, 'Who discovered gravity?', 'Isaac Newton', 'Albert Einstein', 'Isaac Newton', 'Galileo', 'Correct!', 1, 1),
(2, 'What is the chemical formula for salt?', 'NaCl', 'H2O', 'NaCl', 'CO2', 'Correct!', 2, 1),
(3, 'What is the capital of Germany?', 'Berlin', 'Munich', 'Berlin', 'Hamburg', 'Correct!', 3, 1),
(1, 'Who wrote "Pride and Prejudice"?', 'Jane Austen', 'Charlotte Bronte', 'Jane Austen', 'George Eliot', 'Correct!', 4, 1),
(2, 'What is the second planet from the Sun?', 'Venus', 'Mars', 'Venus', 'Earth', 'Correct!', 5, 1),

-- 3 Questions for user_id = 2 (practice_section_id = 7)
(3, 'Who discovered penicillin?', 'Alexander Fleming', 'Marie Curie', 'Alexander Fleming', 'Louis Pasteur', 'Correct!', 7, 2),
(1, 'What is the formula for the area of a circle?', 'πr²', '2πr', 'πr²', 'πd', 'Correct!', 7, 2),
(2, 'What is the tallest mountain in the world?', 'Mount Everest', 'K2', 'Mount Everest', 'Kangchenjunga', 'Correct!', 7, 2);


INSERT INTO test_datas
(date_taken, learn_id, user_id)
VALUES 
('2024-09-18 14:15:00', 1, 1),
('2024-09-18 14:15:00', 2, 1),
('2024-09-18 14:15:00', 3, 1),
('2024-09-18 14:15:00', 4, 1),
('2024-09-18 14:15:00', 5, 1),
('2024-09-18 14:15:00', 6, 1),
('2024-09-18 14:15:00', 7, 1);