import sqlite3


def connection():
    connect = None
    try:
        connect = sqlite3.connect('hw.db')
        return connect
    except sqlite3.Error as e:
        print(e)
    return connect


def get_cities(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print("Список городов:")
    for city in cities:
        print(f" {city[0]}, {city[1]}")


def get_students_by_city_id(connect, city_id):
    cursor = connect.cursor()
    query = """
    SELECT s.first_name, s.last_name, c.title AS city, c.area, cn.title AS country
    FROM students s
    JOIN cities c ON s.city_id = c.id
    JOIN countries cn ON c.country_id = cn.id
    WHERE s.city_id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()
    if students:
        print(f"Ученики, проживающие в городе с ID {city_id}:")
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Город: {student[2]}, Площадь города: {student[3]}, Страна: {student[4]}")
    else:
        print(f"В городе с ID {city_id} нет учеников.")


def main():
    connect = connection()
    if connect:
        get_cities(connect)
        city_id = input("Введите ID города, чтобы получить список учеников: ")
        if city_id.isdigit():
            get_students_by_city_id(connect, int(city_id))
        else:
            print("Некорректный ввод. Пожалуйста, введите числовой ID города.")
        connect.close()


main()
