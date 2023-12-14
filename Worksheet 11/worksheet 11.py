import sqlite3


def createDatabase(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = 1")

    c.execute("CREATE TABLE IF NOT EXISTS Researcher("
              "orcidid TEXT PRIMARY KEY,"
              "firstname TEXT,"
              "lastname TEXT,"
              "university TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS Project("
              "projectid INTEGER PRIMARY KEY,"
              "projectname TEXT,"
              "startyear DATE,"
              "finishyear DATE,"
              "budget INTEGER)")

    c.execute("CREATE TABLE IF NOT EXISTS Work("
              "orcidid TEXT,"
              "projectid INTEGER,"
              "Roles Text,"
              "FOREIGN KEY (orcidid) REFERENCES Researcher(orcidid),"
              "FOREIGN KEY (projectid) REFERENCES Project(projectid),"
              "PRIMARY KEY(orcidid, projectid))")
    conn.commit()
    conn.close()


def insertRecords(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    researchers = [("0000-1111-2222-3333", "James", "Smith", "Manchester University"),
                   ("4444-5555-6666-7777", "Robert", "Jones", "Wolverhampton University"),
                   ("1111-1111-2222-3333", "John", "Taylor", "Manchester University"),
                   ("4444-4444-6666-7777", "David", "Evans", "Middlesex University")]

    cursor.executemany("INSERT INTO Researcher VALUES(?, ?, ?, ?)", researchers)

    projects = [(1, "Educational Data Mining", "2020", "2021", 50000),
                (2, "Medical Informatics", "2021", "2022", 150000)]

    cursor.executemany("INSERT INTO Project VALUES(?, ?, ?, ?, ?)", projects)

    works = [("0000-1111-2222-3333", 1, "Data Scientist"),
             ("0000-1111-2222-3333", 2, "Data Scientist"),
             ("1111-1111-2222-3333", 2, "Medical Doctor"),
             ("4444-4444-6666-7777", 1, "Education Specialist"),
             ("4444-5555-6666-7777", 1, "Programmer")]

    cursor.executemany("INSERT INTO Work VALUES(?, ?, ?)", works)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    db_name = "research_projects.db"
    createDatabase(db_name)
    # insertRecords(db_name)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    print("1. Show the researchers with their details who are working in a given project. The project id will be "
          "taken from the user.")
    proj_id = int(input("Enter the project id: "))

    c.execute(f"SELECT r.* FROM Researcher r, Work w WHERE w.projectid={proj_id} AND w.orcidid=r.orcidid")
    results = c.fetchall()
    print(f"Researchers working on Project: {proj_id}")
    for result in results:
        print(f"Orcid ID: {result[0]}, Full Name: {result[1]} {result[2]}, University: {result[3]}")

    print("\n")

    print("2. Show the number of researchers in each project.")
    c.execute("SELECT projectid, COUNT(*) FROM Work GROUP BY projectid")
    results = c.fetchall()
    for result in results:
        print(f"Project id: {result[0]} has {result[1]} researchers working on it.")

    print("\n")

    print("3. Show the names of the researchers who are participating in a project with a budget greater than 100000 "
          "and from Manchester University.")
    c.execute("SELECT r.firstname, r.lastname FROM Researcher r, Project p, Work w WHERE "
              "w.orcidid = r.orcidid AND w.projectid=p.projectid AND p.budget>100000 AND "
              "r.university = 'Manchester University'")
    results = c.fetchall()

    for result in results:
        print("Full Name: " + " ".join(result))

    print("\n")

    print("4. Show the projects with a researcher whose role is Programmer.")
    c.execute("SELECT DISTINCT p.* FROM Project p, Work w WHERE w.Roles='Programmer'")
    results = c.fetchall()
    print("Projects with a programmer: ")

    for result in results:
        print(f"Project ID: {result[0]}, Name: {result[1]}, Start Year={result[2]}, End Year={result[3]}, Budget={result[4]}")

    conn.close()

