-- Создаем базу данных
CREATE DATABASE AdoNetCourseDB;
GO

USE AdoNetCourseDB;
GO

-- Создаем таблицу
CREATE TABLE Students (
    Id INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50)
);

-- Добавляем тестовые данные
INSERT INTO Students (FirstName, LastName) VALUES 
(N'Иван', N'Иванов'),
(N'Петр', N'Петров'),
(N'Анна', N'Сидорова');