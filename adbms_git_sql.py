# Connect to the MySQL server
conn = myconn.connect(
    host="localhost",
    user="sudip",
    password="sudip@123",
    database="Anshu"
)

cursor = conn.cursor()

# 1. Create a view of instructors without their salary
cursor.execute("CREATE VIEW IF NOT EXISTS faculty AS SELECT ID, name, dept_name FROM instructor")

# 2. Create a view of department salary totals
cursor.execute("CREATE VIEW IF NOT EXISTS dept_salary_totals AS SELECT dept_name, SUM(salary) AS total_salary FROM instructor GROUP BY dept_name")

# 3. Create a role of student
try:
    cursor.execute("CREATE ROLE 'student'")
except:
    print("Role 'student' may already exist.")

# 4. Give select privileges on the view faculty to the role student
cursor.execute("GRANT SELECT ON Anshu.faculty TO 'student'")

# 5. Create a new user and assign her the role of student
try:
    cursor.execute("CREATE USER 'jane_doe'@'localhost' IDENTIFIED BY 'password123'")
except:
    print("User 'jane_doe' may already exist.")

cursor.execute("GRANT 'student' TO 'jane_doe'@'localhost'")

# 6. Revoke privileges of the new user
cursor.execute("REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'jane_doe'@'localhost'")

# 7. Remove the role of student
cursor.execute("DROP ROLE IF EXISTS 'student'")

# 8. Give select privileges on the view faculty to the new user
cursor.execute("GRANT SELECT ON Anshu.faculty TO 'jane_doe'@'localhost'")

# 9. Create table teaches2 with same structure as teaches
cursor.execute("CREATE TABLE IF NOT EXISTS teaches2 LIKE teaches")

# Alter teaches2 to add semester constraint
cursor.execute("ALTER TABLE teaches2 MODIFY semester ENUM('Fall', 'Winter', 'Spring', 'Summer')")

# 10. Create index on ID column of teaches
cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON teaches(ID)")

# Measure query performance
start_time = time.time()
cursor.execute("SELECT * FROM teaches WHERE ID = 10101")
print("With Index Query Time:", time.time() - start_time)

cursor.execute("DROP INDEX IF EXISTS idx_id ON teaches")

start_time = time.time()
cursor.execute("SELECT * FROM teaches WHERE ID = 10101")
print("Without Index Query Time:", time.time() - start_time)

# Commit and close
conn.commit()
cursor.close()
conn.close()
