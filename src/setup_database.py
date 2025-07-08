import os
import sqlite3
import csv
import kagglehub

DB_FILE = "leetcode.db"

DATA_STRUCTURES = {
    'Trie', 'Binary Indexed Tree', 'String', 'Hash Table', 'Graph', 'Stack',
    'Heap (Priority Queue)', 'Array', 'Binary Tree', 'Ordered Set', 'Tree', 'Queue',
    'Binary Search Tree', 'Linked List', 'Monotonic Queue', 'Doubly-Linked List'
}

TYPES = {
    'Number Theory', 'Recursion', 'Design', 'Brainteaser', 'Reservoir Sampling', 'Greedy',
    'Enumeration', 'Math', 'Quickselect', 'String Matching', 'Divide and Conquer',
    'Memoization', 'Hash Function', 'Interactive', 'Randomized', 'Binary Search',
    'Bit Manipulation', 'Bitmask', 'Biconnected Component', 'Rolling Hash', 'Data Stream',
    'Eulerian Circuit', 'Strongly Connected Component', 'Line Sweep', 'Monotonic Stack',
    'Prefix Sum', 'Simulation', 'Merge Sort', 'Matrix', 'Game Theory', 'Rejection Sampling',
    'Minimum Spanning Tree', 'Depth-First Search', 'Dynamic Programming', 'Sorting',
    'Segment Tree', 'Database', 'Iterator', 'Counting', 'Two Pointers', 'Sliding Window',
    'Suffix Array', 'Backtracking', 'Shortest Path', 'Bucket Sort', 'Geometry',
    'Combinatorics', 'Concurrency', 'Breadth-First Search', 'Counting Sort', 'Shell',
    'Union Find', 'Probability and Statistics', 'Topological Sort', 'Radix Sort'
}

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

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        first_line = next(reader) 
        
        for row in reader:
            if row[3]:
                cursor.execute("""
                    INSERT INTO questions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, row)

    conn.commit()
    print("Database created.")

    conn.close()

if __name__ == "__main__":
    create_database()