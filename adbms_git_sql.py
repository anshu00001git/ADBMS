import mysql.connector as myconn
print(myconn.__version__)


# Connect to the MySQL server
conn = myconn.connect(
    host="localhost",  # Replace with your MySQL host
    user="sudip",       # Replace with your MySQL username
    password="sudip@123",
    database="Anshu" # Replace with your MySQL password
)


