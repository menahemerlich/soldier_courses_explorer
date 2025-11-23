from db.connection import get_connection
from db.load_csv import load_csv
from db.queries import search_by_institution, search_by_course, get_most_common_course, get_least_common_course, get_course_count_per_district, run_free_query

menu = "== menu==\n1. Load CSV into DB.\n2. Search records by institution name.\n3. Search records by course name\n4. Find most/least common course.\n5. Show course count per district\n6. Free SQL query.\n7. Exit."

def print_in_row(my_list):
    for row in my_list:
        print(row)

while True:
    cunn = get_connection()
    print(menu)
    choice = input("Your choice: ")
    if choice == "1":
        load_csv(cunn)
    elif choice == "2":
        keyword = input("Your keyword: ")
        my_list = search_by_institution(cunn, keyword)
        print_in_row(my_list)
    elif choice == "3":
        keyword = input("Your keyword: ")
        my_list = search_by_course(cunn, keyword)
        print_in_row(my_list)
    elif choice == "4":
        keyword = input("Your keyword (most/least): ")
        if keyword == "most":
            print(get_most_common_course(cunn))
        elif keyword == "least":
            print(get_least_common_course(cunn))
        else:
            print("Typo error, try again.")
    elif choice == "5":
        my_list = get_course_count_per_district(cunn)
        print_in_row(my_list)
    elif choice == "6":
        sql = input("Your SQL command: ")
        my_list = run_free_query(cunn, sql)
        if my_list != None:
            print_in_row(my_list)

    elif choice == "7":
        break
    else:
        print("Typo error, try again.")