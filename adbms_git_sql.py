import mysql.connector as myconn
print(myconn.__version__)


# Connect to the MySQL server
conn = myconn.connect(
    host="localhost",  # Replace with your MySQL host
    user="sudip",       # Replace with your MySQL username
    password="sudip@123",
    database="Anshu" # Replace with your MySQL password
)

cursor = conn.cursor()
# 1. Create a view of instructors without their salary
cursor.execute("CREATE VIEW faculty AS SELECT ID, name, dept_name FROM instructor")

# 2. Create a view of department salary totals
cursor.execute("CREATE VIEW dept_salary_totals AS SELECT dept_name, SUM(salary) AS total_salary FROM instructor GROUP BY dept_name")

# 3. Create a role of student
cursor.execute("CREATE ROLE 'student'")

# 4. Give select privileges on the view faculty to the role student
cursor.execute("GRANT SELECT ON university_db.faculty TO 'student'")

# 5. Create a new user and assign her the role of student
cursor.execute("CREATE USER 'jane_doe'@'localhost' IDENTIFIED BY 'password123'")
cursor.execute("GRANT 'student' TO 'jane_doe'@'localhost'")

# 6. Revoke privileges of the new user
cursor.execute("REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'jane_doe'@'localhost'")

# 7. Remove the role of student
cursor.execute("DROP ROLE 'student'")

# 8. Give select privileges on the view faculty to the new user
cursor.execute("GRANT SELECT ON university_db.faculty TO 'jane_doe'@'localhost'")

# 9. Create table teaches2 with semester constraint
cursor.execute('''
CREATE TABLE teaches2 (
    ID INT,
    Course_id VARCHAR(10),
    sec_id INT,
    semester ENUM('Fall', 'Winter', 'Spring', 'Summer'),
    year INT
)
''')

# 10. Create index on ID column of teaches
cursor.execute("CREATE INDEX idx_id ON teaches(ID)")

# Measure query performance
import time
start_time = time.time()
cursor.execute("SELECT * FROM teaches WHERE ID = 10101")
print("With Index Query Time:", time.time() - start_time)

cursor.execute("DROP INDEX idx_id ON teaches")  # Step 11: Drop index

start_time = time.time()
cursor.execute("SELECT * FROM teaches WHERE ID = 10101")
print("Without Index Query Time:", time.time() - start_time)

# Commit and close
conn.commit()
cursor.close()
conn.close()

