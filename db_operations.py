import sqlite3

#Initilise DATABASE
def init_db():
    # Connecting to the database
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    print('Database initialized.')

    # cursor.execute("DROP TABLE costTable")

    # Create the table with a UNIQUE constraint on 'material'
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS costTable (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material TEXT NOT NULL UNIQUE,  -- Ensure 'material' is unique
        base_rate REAL NOT NULL,
        maintenance_rate REAL NOT NULL,
        repair_rate REAL NOT NULL,
        demolition_rate REAL NOT NULL,
        environmental_factor REAL NOT NULL,
        social_factor REAL NOT NULL,
        delay_factor REAL NOT NULL
    )
    """)

    # Prepopulate with data
    data = [
        ("Steel", 3000, 50, 200, 100, 10, 0.5, 0.3),
        ("Concrete", 2500, 75, 150, 80, 8, 0.6, 0.2)
    ]

    # Insert data with exception handling for duplicates
    for row in data:
        try:
            cursor.execute("""
            INSERT INTO costTable (
                material, base_rate, maintenance_rate, repair_rate, demolition_rate, environmental_factor, social_factor, delay_factor
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        except sqlite3.IntegrityError:
            print(f"Duplicate material found: {row[0]}")


    # Verify data in the table
    cursor.execute("SELECT * FROM costTable")
    res = cursor.fetchall()
    print("Database contents:", res)

    conn.commit()
    conn.close()

def fetch_material_data(material):
    try:
        conn = sqlite3.connect('sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM costTable WHERE material = ?", (material,))
        data = cursor.fetchone()
        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"Error fetching data for {material}: {e}")
        return None

# Function to update material data
def update_material_data(material, data):
    try:
        conn = sqlite3.connect('sql.db')
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE costTable SET 
            base_rate = ?, maintenance_rate = ?, repair_rate = ?, 
            demolition_rate = ?, environmental_factor = ?, 
            social_factor = ?, delay_factor = ? 
            WHERE material = ?
        """, (*data, material))
        
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error updating data for {material}: {e}")
        return False
