import os
import random
import sqlite3
import sys
import printing as pf
from ai_feedback import give_feedback
from input_validation import get_program, get_abcd_multi, check_program
from input_evaluation import check_answer

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

ABCD_TO_INDEX = {'a': 0, 'b': 1, 'c': 2, 'd': 3}


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
    while len(answers) < 4:
        extra = random.choice(sorted(answers_set - set(answers)))
        answers.append(extra)
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
        "SELECT question_id, title, question_text, tags, hints, difficulty, similar_ids FROM questions;"
    )
    rows = cur.fetchall()
    conn.close()

    buckets = {}
    id_map = {}
    for qid, title, text, raw_tags, raw_hints, difficulty, raw_sim in rows:
        tags = [t.strip() for t in raw_tags.strip('[]').replace("'", "").split(',') if t.strip()]
        hints_list = [h.strip() for h in raw_hints.split(';') if raw_hints and h.strip()]
        diff = (difficulty or '').lower()
        similar_ids = []
        if raw_sim:
            similar_ids = [int(x) for x in raw_sim.split(',') if x.strip().isdigit()]
        entry = {
            'id': qid,
            'title': title,
            'text': text.strip(),
            'tags': tags,
            'hints': hints_list,
            'difficulty': diff,
            'similar_ids': similar_ids
        }
        id_map[qid] = entry
        for tag in tags:
            buckets.setdefault(tag, []).append(entry)
    return buckets, id_map


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


def show_question_flow(topic, question_list, id_map):
    pf.print_general(f"Topic: {topic}", header=False)
    diff = prompt_difficulty()
    if diff != 'random':
        filtered = [q for q in question_list if q['difficulty'] == diff]
        if not filtered:
            print(f"No {diff.capitalize()} questions; defaulting to all difficulties.")
            filtered = question_list
    else:
        filtered = question_list

    # Let user select a specific question
    print("Select a question:")
    for idx, q in enumerate(filtered, start=1):
        print(f"  {idx}. {q['title']}")
    while True:
        sel = input(f"Enter question number (1-{len(filtered)}) or 'exit': ").strip().lower()
        if sel == 'exit':
            pf.print_general('Thank you for practicing with TechKnow!')
            sys.exit(0)
        if sel.isdigit() and 1 <= int(sel) <= len(filtered):
            question = filtered[int(sel)-1]
            break
        print('Invalid selection, please try again.')

    pf.print_general(f"{diff.capitalize()} question:", header=False, footer=False)
    pf.print_problem(question['title'], question['text'], header=False, footer=False)

    answers1, answers2, user_ans1, user_ans2 = None, None, None, None

    # Approach MCQ
    types = set(question['tags']) - DATA_STRUCTURES
    valid_type = len(types) != 0
    if valid_type:
        answers1 = get_answer_choice(types, TYPES)
        pf.print_approach_question(answers1)
        user_ans1 = get_abcd_multi()
        if user_ans1 == 'exit': sys.exit(0)
        if user_ans1 == 'next': return
        user_ans1 = {answers1[ABCD_TO_INDEX[c]] for c in user_ans1}

    # Data-structure MCQ
    ds = set(question['tags']) & DATA_STRUCTURES
    valid_ds = len(ds) != 0
    if valid_ds:
        answers2 = get_answer_choice(ds, DATA_STRUCTURES)
        pf.print_data_structures_question(answers2)
        user_ans2 = get_abcd_multi()
        if user_ans2 == 'exit': sys.exit(0)
        if user_ans2 == 'next': return
        user_ans2 = {answers2[ABCD_TO_INDEX[c]] for c in user_ans2}

    pf.print_feedback(user_ans1, user_ans2, types, ds, valid_type=valid_type, valid_ds=valid_ds)  # changed: pass displayed MCQ options lists instead of empty type/ds lists to avoid indexing errors  # changed: convert sets to lists to avoid indexing errors

    # Optional hint
    if question['hints']:
        print("Type 'hint' for a hint, or press Enter to continue.")
        if input('>>> ').strip().lower() == 'hint':
            for h in question['hints']:
                pf.print_general(f"Hint: {h}")

    # Similar question option
    if question['similar_ids']:
        print("Type 'similar' to try a related question.")

    # Code attempt loop
    while True:
        print("Enter 'similar', 'next', 'exit', or paste your code ending with ';'.")
        cmd = input('> ').strip().lower()
        if cmd == 'similar' and question['similar_ids']:
            sim_list = [id_map[i] for i in question['similar_ids'] if i in id_map]
            if sim_list:
                show_question_flow(topic, sim_list, id_map)
            return
        if cmd == 'next':
            return
        if cmd == 'exit':
            pf.print_general('Thank you for practicing with TechKnow!')
            sys.exit(0)
        # Treat cmd as code; validate syntax
        code = cmd
        while not check_program(code):
            print("There's an error in your code. Please try again.")
            code = get_program()
            if code.lower() in ('next', 'exit'):
                break
        if code.lower() == 'next':
            return
        if code.lower() == 'exit':
            pf.print_general('Thank you for practicing with TechKnow!')
            sys.exit(0)
        guidance = give_feedback(question['title'], question['text'], code)
        pf.print_general(guidance)


def main():
    pf.print_general(
        """
Welcome to TechKnow!
TechKnow is an interview prepper that lets you choose from 71 LeetCode topics and practice any question on the fly.
Simply type a topic number to get a random problem, or 'exit' to quit.
""",
        footer=False
    )

    buckets, id_map = load_buckets()
    topics = sorted(buckets.keys())

    while True:
        display_menu(topics, buckets)
        idx = prompt_choice(len(topics))
        if idx is None:
            break
        if idx == -1:
            print('Sorry, please try again.')
            continue

        show_question_flow(topics[idx], buckets[topics[idx]], id_map)

    pf.print_general('Thank you for practicing with TechKnow!')


if __name__ == '__main__':
    main()
