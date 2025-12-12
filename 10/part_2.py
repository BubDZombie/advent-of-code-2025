import itertools
import re
import sys

from datetime import datetime, timedelta
from part_1 import Machine

def turn_on(machine):
    print(f"\n\nStarting {machine}")
    stack = [tuple()]
    tried = set()
    timestamp = datetime.now()
    verbose = True
    while len(stack):
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
        if verbose:
            print(f"min_delta: {min_delta} max_delta: {max_delta}")
        # These buttons shall not be pressed.
        verboten = set()
        for i, joltage_requirement in enumerate(machine.joltage_requirements):
            if machine.joltages[i] < joltage_requirement:
                joltage_needed = joltage_requirement - machine.joltages[i]
                for button in machine.buttons:
                    if button & 1<<i:
                        button_scores[button] += max_delta - joltage_needed
                    else:
                        button_scores[button] += joltage_needed
            elif machine.joltages[i] > joltage_requirement:
                for button in machine.buttons:
                    verboten.add(button)
            else:
                # Joltage == requirement, don't press any matching buttons.
                for button in machine.buttons:
                    if button & 1<<i:
                        verboten.add(button)

        button_order = sorted([score for score in button_scores.items()], key=lambda s: abs(s[1]), reverse=True)
        if verbose:
            print(f"{[(bin(button), score) for button, score in button_order]}")
        for button, score in button_order:
            new_sequence = sequence + (button,)
            signature = tuple(sorted(new_sequence))
            if signature not in tried and button not in verboten:
                stack.insert(0, new_sequence)
                tried.add(signature)
        verbose = False
    return([])

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            m = Machine()
            m.parse_line(line)
            sequence = turn_on(m)
            print(f"\n{m} Sequence: {[bin(press) for press in sequence]}")
            sum += len(sequence)
    print(sum)
