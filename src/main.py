import os
import random
import sqlite3
import sys
import printing as pf
from ai_feedback import give_feedback
from input_validation import get_program

DATA_STRUCTURES = {'Trie', 
                    'Binary Indexed Tree', 
                    'String', 
                    'Hash Table', 
                    'Graph', 
                    'Stack',
                    'Heap (Priority Queue)', 
                    'Array', 
                    'Binary Tree', 
                    'Ordered Set', 
                    'Tree', 
                    'Queue', 
                    'Binary Search Tree',
                    'Linked List',
                    'Monotonic Queue',
                    'Doubly-Linked List'
                    }

def load_buckets():
    src_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(src_dir, '..'))
    db_path = os.path.join(root_dir, 'leetcode.db')
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT question_id, title, question_text, tags, hints FROM questions;"
    )
    rows = cur.fetchall()
    conn.close()

    buckets = {}
    for qid, title, text, raw_tags, raw_hints in rows:
        tags = [t.strip() for t in raw_tags.strip('[]')
                .replace("'", "")
                .split(',') if t.strip()]
        hints_list = [h.strip() for h in raw_hints.split(';')
                      if raw_hints and h.strip()]
        data_structures = {i for i in raw_tags if i in DATA_STRUCTURES}
        entry = {
            'id': qid,
            'title': title,
            'text': text.strip(),
            'hints': hints_list,
            'data_structures' : data_structures,
            'type' : ''
        }

        for tag in tags:
            buckets.setdefault(tag, []).append(entry)
    return buckets


def display_menu(topics, buckets):
    pf.print_general('Select a topic by number:', footer=False)
    for i, topic in enumerate(topics, start=1):
        print(f"  {i:2d}. {topic} ({len(buckets[topic])} problems)")
    print()


def prompt_choice(num_topics):
    choice = input('Enter topic number (or "exit"): ').strip().lower()
    if choice == 'exit':
        return None
    if choice.isdigit() and 1 <= int(choice) <= num_topics:
        return int(choice) - 1
    return -1


def show_question_flow(topic, question):
    pf.print_general(f"Random {topic} question:", header=False)
    pf.print_problem(question['title'], question['text'])

    if question['hints']:
        print("Type 'hint' for a hint, or press Enter to continue.")
        if input('> ').strip().lower() == 'hint':
            for hint in question['hints']:
                pf.print_general(f"Hint: {hint}", header=False)

    while True:
        print(
            "Enter your solution attempt. When finished type a ';', to quit enter 'exit', for a new problem enter 'next'"
        )
        user_input = get_program()
        if user_input.lower() == 'next':
            return
        if user_input.lower() == 'exit':
            pf.print_general('Thank you for practicing with TechKnow!')
            sys.exit(0)
        guidance = give_feedback(
            question['title'], question['text'], user_input
        )
        pf.print_general(guidance, header=False)


def main():
    pf.print_general(
        """
Welcome to TechKnow!
TechKnow is an interview prepper that lets you choose from 71 LeetCode topics and practice random questions on the fly.
Simply type a topic number to get a random problem, or 'exit' to quit.
""", footer=False)

    buckets = load_buckets()
    topics = sorted(buckets.keys())

    while True:
        display_menu(topics, buckets)
        idx = prompt_choice(len(topics))
        if idx is None:
            break
        if idx == -1:
            print('Sorry, please try again.')
            continue

        topic = topics[idx]
        question = random.choice(buckets[topic])
        show_question_flow(topic, question)

    pf.print_general('Thank you for practicing with TechKnow!')


if __name__ == '__main__':
    main()
