import sqlite3


def createDatabase(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = 1")

    c.execute("CREATE TABLE IF NOT EXISTS STUDENT("
              "studentID INTEGER PRIMARY KEY,"
              "studentName TEXT,"
              "major TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS COURSE("
              "courseCode TEXT PRIMARY KEY,"
              "courseName TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS STUDENTCOURSE("
              "studentID INTEGER,"
              "courseCode TEXT,"
              "semester INTEGER,"
              "grade TEXT,"
              "FOREIGN KEY (studentID) REFERENCES STUDENT(studentID),"
              "FOREIGN KEY (courseCode) REFERENCES COURSE(courseCode),"
              "PRIMARY KEY(studentID, courseCode, semester))")

    conn.commit()
    conn.close()


def insertRecords(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    students = [(1, "Olivia Ethan", "CNG"), (2, "William Harper", "CNG"), (3, "Sophia Charlotte", "EEE")]
    c.executemany("INSERT INTO STUDENT VALUES(?, ?, ?)", students)

    courses = [("CNG140", "C Programming"), ("CNG213", "Data Structures"), ("CNG315", "Algorithms")]
    c.executemany("INSERT INTO COURSE VALUES(?,?)", courses)

    studentCourses = [(1, "CNG140", 20192, "AA"), (2, "CNG140", 20192, "BB"), (2, "CNG140", 20202, "AA")]
    c.executemany("INSERT INTO STUDENTCOURSE VALUES(?, ?, ?, ?)", studentCourses)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    dbname = input("Enter db name: ")
    #createDatabase(dbname)
    #insertRecords(dbname)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Print the names of the students who took CNG140 in 20192.
    c.execute(
        "SELECT studentName FROM STUDENT s, STUDENTCOURSE c WHERE s.studentID = c.studentID AND c.courseCode = "
        "'CNG140' AND semester = 20192")

    row = c.fetchone()
    while row != None:
        print("Student Name: " + row[0])
        row = c.fetchone()

    # Print the courses order by name
    c.execute("SELECT * FROM COURSE ORDER BY courseName DESC")
    courses = c.fetchall()
    for course in courses:
        print("Course code: {}, Course name: {}".format(course[0], course[1]))

    # Print the number of students in each major
    c.execute("SELECT major, COUNT(*) FROM STUDENT GROUP BY major HAVING COUNT(*) >= 2")
    majors = c.fetchall()
    print(majors)

    courseCode = input("Enter the course code: ")
    c.execute("SELECT * FROM COURSE WHERE courseCode LIKE '%{}%'".format(courseCode))
    courses = c.fetchone()
    print(courses)



    conn.close()
