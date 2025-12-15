import itertools
import re
import statistics
import sys

from datetime import datetime, timedelta
from part_1 import Machine

def sort_buttons_max_press(machine):
    button_scores = {}
    for i, joltage in enumerate(machine.joltage_diff):
        for button in machine.buttons:
            if button & 1<<i:
                if not button in button_scores or button_scores[button] > joltage:
                    button_scores[button] = joltage
    button_order = sorted([score for score in button_scores.items()], key=lambda s: abs(s[1]), reverse=False)
    return button_order

def sort_buttons_min_diff(machine):
        button_scores = {}
        for button in machine.buttons:
            button_scores[button] = 0
        min_delta = None
        max_delta = None
        for i, joltage_requirement in enumerate(machine.joltage_requirements):
            delta = joltage_requirement - machine.joltages[i]
            if not max_delta or delta > max_delta:
                max_delta = delta
            if not min_delta or delta < min_delta:
                min_delta = delta
        mean_delta = (min_delta + max_delta) / 2
        for i, joltage_requirement in enumerate(machine.joltage_requirements):
            if machine.joltages[i] < joltage_requirement:
                joltage_needed = joltage_requirement - machine.joltages[i]
                for button in machine.buttons:
                    if button & 1<<i:
                        button_scores[button] += max_delta - joltage_needed
                    else:
                        button_scores[button] += abs(joltage_needed - min_delta)

        button_order = sorted([score for score in button_scores.items()], key=lambda s: abs(s[1]), reverse=True)
        return button_order

def sort_buttons_min_range(machine):
    button_scores = {}
    for button in machine.buttons:
        borked = False
        joltage_diff_tmp = [diff for diff in machine.joltage_diff]
        for i in range(len(joltage_diff_tmp)):
            if button & 1<<i:
                joltage_diff_tmp[i] -= 1
                if joltage_diff_tmp[i] < 0:
                    borked = True
        if not borked:
            button_scores[button] = max(joltage_diff_tmp) - min(joltage_diff_tmp)
    button_order = sorted([score for score in button_scores.items()], key=lambda s: abs(s[1]), reverse=True)
    return button_order

def sort_buttons_stdev(machine):
    button_scores = {}
    for button in machine.buttons:
        joltage_diff_tmp = [diff for diff in machine.joltage_diff]
        for i in range(len(joltage_diff_tmp)):
            if button & 1<<i:
                joltage_diff_tmp[i] -= 1
        button_scores[button] = statistics.stdev(joltage_diff_tmp)
    button_order = sorted([score for score in button_scores.items()], key=lambda s: abs(s[1]), reverse=True)
    return button_order

def turn_on(machine):
    stack = [tuple()]
    tried = set()
    timestamp = datetime.now()
    verbose = True
    iterations = 0
    while len(stack):
        iterations += 1
        sequence = stack.pop(0)
        if datetime.now() - timestamp > timedelta(seconds=5):
            verbose = True
            print(f"Stack depth: {len(stack)}")
            timestamp = datetime.now()
            print(machine)
            print(f"{[bin(button) for button in sequence]}")
        machine.reset()
        for button in sequence:
            machine.press(button)
        if machine.jolted():
            return(sequence)
        else:
            borked = False
            for i, joltage in enumerate(machine.joltages):
                if joltage > machine.joltage_requirements[i]:
                    borked = True
                    break
            if borked:
                continue
        button_order = sort_buttons_stdev(machine)
        if not button_order:
            continue
        if iterations < 300 or verbose:
            print(f"{machine.joltage_diff} {bin(button_order[-1][0])}")
        for button, score in button_order:
            new_sequence = sequence + (button,)
            signature = tuple(sorted(new_sequence))
            if signature not in tried:
                stack.append(new_sequence)
                tried.add(signature)
        verbose = False
    return([])

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            print(f"\n{line}")
            m = Machine()
            m.parse_line(line)
            sequence = turn_on(m)
            print(f"\n{m} Sequence: {[bin(press) for press in sequence]}")
            sum += len(sequence)
    print(sum)
