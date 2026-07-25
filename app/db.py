import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@123",
        database="RetailManagement"
    )

    if connection.is_connected():
        print("✅ Connected to MySQL successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()