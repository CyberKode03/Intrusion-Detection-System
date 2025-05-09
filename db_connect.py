import mysql.connector

def insert_alert(timestamp, src_ip, dest_ip, message):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="idsdb",
            port=3377
        )
        cursor = conn.cursor()

        query = "INSERT INTO alerts (timestamp, src_ip, dest_ip, message) VALUES (%s, %s, %s, %s)"
        values = (timestamp, src_ip, dest_ip, message)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Alert inserted successfully.")

    except mysql.connector.Error as err:
        print("❌ Database Error:", err)

def get_alerts():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="idsdb",
            port=3377
        )
        cursor = conn.cursor()

        query = "SELECT id, timestamp, src_ip, dest_ip, message FROM alerts ORDER BY timestamp DESC"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    except mysql.connector.Error as err:
        print("❌ Database Error:", err)
        return []
