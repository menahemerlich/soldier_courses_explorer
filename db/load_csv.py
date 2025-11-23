import csv

def load_csv(cunn):
    row_count = 0
    cursor = cunn.cursor()
    with open("data/courses.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cursor.execute("INSERT INTO courses (institution, city, address, course, district, telephone, email)VALUES (%s, %s, %s, %s, %s, %s, %s);", row)
            row_count += 1

    print(f"{row_count} rows loaded successfully!")

    cunn.commit()
    cursor.close()
    cunn.close()

