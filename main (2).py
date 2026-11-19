import pyodbc

def main():
    # 1. Создание строки подключения
    # ВАЖНО: Замените SERVER_NAME на имя вашего сервера. 
    # Если используете локальный сервер по умолчанию, попробуйте 'localhost' или '.\SQLEXPRESS'
    server = 'localhost' 
    database = 'AdoNetCourseDB'
    username = 'sa' # Замените на вашего пользователя, если используется SQL-аутентификация
    password = 'YourPassword' # Замените на ваш пароль
    
    # Вариант строки подключения с использованием Trusted_Connection (Windows Authentication)
    # connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    
    # Вариант строки подключения с логином и паролем (SQL Authentication)
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # 3. Создаем соединение
        print("Подключение к базе данных...")
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print("Успешное подключение!")

        # 2. SELECT запрос к MSSQL Server
        sql_query = "SELECT Id, FirstName, LastName FROM Students"
        
        # Выполняем запрос
        cursor.execute(sql_query)

        # 4. Вывод результата в консоль с помощью цикла for
        print("\nСписок студентов:")
        print("-" * 30)
        for row in cursor:
            # row[0] - Id, row[1] - FirstName, row[2] - LastName
            print(f"ID: {row[0]} | Имя: {row[1]} | Фамилия: {row[2]}")
        print("-" * 30)

    except pyodbc.Error as e:
        print("Ошибка при работе с базой данных:")
        print(e)
    
    finally:
        # Закрываем соединение, если оно было открыто
        if 'conn' in locals() and conn:
            cursor.close()
            conn.close()
            print("Соединение закрыто.")

if __name__ == "__main__":
    main()