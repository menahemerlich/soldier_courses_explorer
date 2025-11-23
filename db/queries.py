
def search_by_institution(conn, keyword):
    sql = """
        SELECT id, institution, city, course, district, telephone, email
        FROM courses
        WHERE institution LIKE CONCAT('%', %s, '%')
        LIMIT 50;
        """
    cur = conn.cursor()
    cur.execute(sql, (keyword,))
    return cur.fetchall()

def search_by_course(conn, keyword):
    sql = """
        SELECT id, institution, city, course, district, telephone, email
        FROM courses
        WHERE course LIKE CONCAT('%', %s, '%')
        LIMIT 50;
        """
    cur = conn.cursor()
    cur.execute(sql, (keyword,))
    return cur.fetchall()

def get_most_common_course(conn):
    sql = """
        SELECT course, COUNT(*) AS num
        FROM courses
        GROUP BY course
        ORDER BY num DESC
        LIMIT 1;
        """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def get_least_common_course(conn):
    sql = """
        SELECT course, COUNT(*) AS num
        FROM courses
        GROUP BY course
        ORDER BY num ASC
        LIMIT 1;
        """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def get_course_count_per_district(conn):
    sql = """
        SELECT district, COUNT(*) AS num_courses
        FROM courses
        GROUP BY district
        ORDER BY num_courses DESC;
        """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def run_free_query(conn, sql):
    if sql.strip().upper().startswith("SELECT"):
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    else:
        print("Typo error, try again.")
        return None






