import os
import random
import sqlite3
import sys
import printing as pf
from ai_feedback import give_feedback
from input_validation import get_program, get_abcd_multi, check_program
from input_evaluation import check_answer

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

TYPES = {
            'Number Theory', 
            'Recursion', 
            'Design', 
            'Brainteaser', 
            'Reservoir Sampling', 
            'Greedy', 
            'Enumeration', 
            'Math', 
            'Quickselect', 
            'String Matching', 
            'Divide and Conquer', 
            'Memoization', 
            'Hash Function', 
            'Interactive', 
            'Randomized', 
            'Binary Search', 
            'Bit Manipulation',
            'Bitmask', 
            'Biconnected Component', 
            'Rolling Hash', 
            'Data Stream', 
            'Eulerian Circuit', 
            'Strongly Connected Component', 
            'Line Sweep', 
            'Monotonic Stack', 
            'Prefix Sum', 
            'Simulation', 
            'Merge Sort', 
            'Matrix',
            'Game Theory', 
            'Rejection Sampling', 
            'Minimum Spanning Tree', 
            'Depth-First Search', 
            'Dynamic Programming', 
            'Sorting', 
            'Segment Tree', 
            'Database',
            'Iterator', 
            'Counting', 
            'Two Pointers',
            'Sliding Window', 
            'Suffix Array', 
            'Backtracking', 
            'Shortest Path', 
            'Bucket Sort', 
            'Geometry', 
            'Combinatorics', 
            'Concurrency', 
            'Breadth-First Search', 
            'Counting Sort',
            'Shell', 
            'Union Find', 
            'Probability and Statistics', 
            'Topological Sort', 
            'Radix Sort'
        }



ABCD_TO_INDEX = {'a':0, 'b':1, 'c':2, 'd':3}

# Difficulty modes
def prompt_difficulty():
    options = {'1': 'easy', '2': 'medium', '3': 'hard', '4': 'random'}
    while True:
        print("Select difficulty: 1) Easy  2) Medium  3) Hard  4) Random")
        choice = input('>>> ').strip()
        if choice in options:
            return options[choice]
        print('Invalid selection. Choose 1, 2, 3, or 4.')

def get_answer_choice(correct_answers, answers_set):
    answers = list(correct_answers)
    answers += random.sample(sorted(set(answers_set) - set(correct_answers)), 4 - len(correct_answers))
    random.shuffle(answers)
    return answers


def load_buckets():
    src_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(src_dir, '..'))
    db_path = os.path.join(root_dir, 'leetcode.db')
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT question_id, title, question_text, tags, hints, difficulty FROM questions;"
    )
    rows = cur.fetchall()
    conn.close()

    buckets = {}
    for qid, title, text, raw_tags, raw_hints, difficulty in rows:
        tags = [t.strip() for t in raw_tags.strip('[]').replace("'", "").split(',') if t.strip()]
        hints_list = [h.strip() for h in raw_hints.split(';') if raw_hints and h.strip()]
        data_structures = {i for i in tags if i in DATA_STRUCTURES}
        entry = {
            'id': qid,
            'title': title,
            'text': text.strip(),
            'hints': hints_list,
            'data_structures': data_structures,
            'type' : set(tags) - data_structures,
            'difficulty': difficulty.lower()
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


def show_question_flow(topic, question_list):
    pf.print_general(f"Topic: {topic}", header=False)
    diff = prompt_difficulty()
    if diff != 'random':
        filtered = [q for q in question_list if q.get('difficulty') == diff]
        if not filtered:
            print(f"No {diff.capitalize()} questions; defaulting to all difficulties.")
            filtered = question_list
    else:
        filtered = question_list
    question = random.choice(filtered)

    pf.print_general(f"{diff.capitalize()} question:", header=False, footer=False)
    pf.print_problem(question['title'], question['text'], header=False)

    # do approach and ds problems
    types = question['type']
    data_structures = question['data_structures']
    answers1 = get_answer_choice(types, TYPES)
    answers2 = get_answer_choice(data_structures, DATA_STRUCTURES)

    #prompt for approach question
    pf.print_approach_question(answers1, header=False)
    user_answers1 = get_abcd_multi()

    if user_answers1 == 'exit':
        pf.print_general('Thank you for practicing with TechKnow!')
        sys.exit(0)
    if user_answers1 =='next':
        return
    
    user_answers1 = {answers1[ABCD_TO_INDEX[i]] for i in user_answers1}

    # prompt for ds question
    pf.print_data_structures_question(answers2)
    user_answers2 = get_abcd_multi()
    if user_answers2 == 'exit':
        pf.print_general('Thank you for practicing with TechKnow!')
        sys.exit(0)
    if user_answers2 =='next':
        return
    
    user_answers2 = {answers2[ABCD_TO_INDEX[i]] for i in user_answers2}
    
    pf.print_feedback(user_answers1,  user_answers2, types, data_structures)
    
    # prompt user for hints
    if question['hints']:
        print("Type 'hint' for a hint, or press Enter to continue.")
        if input('>>> ').strip().lower() == 'hint':
            for hint in question['hints']:
                pf.print_general(f"Hint: {hint}", header=False)

    # Code attempts
    while True:
        print("Enter your solution attempt (end with ';'), or type 'next' for new question, 'exit' to quit.")
        user_input = get_program()
        if user_input.lower() == 'next':
            return
        if user_input.lower() == 'exit':
            pf.print_general('Thank you for practicing with TechKnow!')
            sys.exit(0)

        while not check_program(user_input):
            print("There's an error in your code. Please try again")
            user_input = get_program()
            if user_input.lower() == 'next':
                return
            if user_input.lower() == 'exit':
                pf.print_general('Thank you for practicing with TechKnow!')
                sys.exit(0)

        guidance = give_feedback(question['title'], question['text'], user_input)
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

        show_question_flow(topics[idx], buckets[topics[idx]])

    pf.print_general('Thank you for practicing with TechKnow!')


if __name__ == '__main__':
    main()
