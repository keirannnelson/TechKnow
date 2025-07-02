import os
import sqlite3
import csv
import kagglehub

DB_FILE = "leetcode.db"

def create_database():
    # remove existing DB if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    # download dataset from kaggle
    dataset_path = kagglehub.dataset_download("manthansolanki/leetcode-questions")

    csv_path = os.path.join(dataset_path, "leetcode_questions.csv")


    # create DB and insert data
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE questions (
        question_id INTEGER,
        title TEXT,
        slug TEXT,
        question_text TEXT,
        tags TEXT,
        difficulty TEXT,
        success_rate REAL,
        total_submission INTEGER,
        total_accepted INTEGER,
        likes INTEGER,
        dislikes INTEGER,
        hints TEXT,
        similar_ids TEXT,
        similar_text TEXT
    )
    """)

    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        first_line = next(reader)

        for row in reader:
            cursor.execute("""
                INSERT INTO questions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)

    conn.commit()
    print("Database created.")

    conn.close()

if __name__ == "__main__":
    create_database()
