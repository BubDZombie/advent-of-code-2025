import copy
import datetime
import itertools
import re
import sys

class Machine():
    def __init__(self):
        self.buttons = []
        self.history = []
        self.indicator = None
        self.joltages = []
        self.state = 0

    def __str__(self):
        output = f"Indicator: [{bin(self.indicator)}]"
        output += f" State: [{bin(self.state)}]"
        output += ' Buttons: ('
        output += ' '.join([bin(button) for button in self.buttons])
        output += ')'
        return output

    def add_button(self, button):
        new_button = 0
        for i in button:
            new_button = new_button | 1<<i
        self.buttons.append(new_button)

    def on(self):
        return(self.state == self.indicator)

    def parse_line(self, line):
        matches = re.match('\\[(.+)\\] (\\(.+\\)) \\{(.+)\\}', line)
        indicator, buttons, joltages = matches.groups()
        self.set_indicator(indicator)
        for button_string in buttons.split():
            button = []
            for i in button_string[1:-1].split(','):
                button.append(int(i))
            self.add_button(button)
        self.set_joltages([int(joltage) for joltage in joltages.split(',')])

    def press(self, button_index):
        self.state ^= self.buttons[button_index]

    def reset(self):
        self.state = 0

    def set_indicator(self, indicator_string):
        self.indicator = 0
        for i, char in enumerate(indicator_string):
            if char == '#':
                self.indicator = self.indicator | 1<<i

    def set_joltages(self, joltages):
        self.joltages = joltages

    def similarity(self):
        return self.indicator & self.state

def turn_on(machine):
    q = [machine]
    best = None
    sequence = None
    while len(q):
        m = q.pop(0)
        buttons = [button for button in range(len(m.buttons))]
        presses = []
        for button in buttons:
                m2 = copy.deepcopy(m)
                m2.press(button)
                if m.on():
                    if not best or len(m.history) < best:
                        best = len(m.history)
                        sequence = m.history
                elif not best or len(m.history) < best:
                    presses.append(m2)
        for press in sorted(presses, key=lambda m: m.similarity(), reverse=True):
            q.append(press)
    return sequence

def turn_on_no_copy(machine):
    print(f"Starting {machine}")
    q = set()
    for button in machine.buttons:
        q.add((button,))
    best = None
    timestamp = datetime.datetime.now()
    while len(q):
        if datetime.datetime.now() - timestamp > datetime.timedelta(seconds=10):
            print(f"Queue depth {len(q)} at {datetime.datetime.now()}")
            timestamp = datetime.datetime.now()
        sequence = q.pop()
        state = 0
        for button in sequence:
            state ^= button
        if state == machine.indicator:
            if not best or len(sequence) < len(best):
                best = sequence
        elif not best or len(sequence) < len(best):
            for button in machine.buttons:
                if button not in sequence:
                    q.add(sequence + (button,))
    return best

def turn_on_itertools(machine):
    print(f"Starting {machine}")
    for i in range(len(machine.buttons)):
        sequence_len = i + 1
        for sequence in itertools.combinations(machine.buttons, sequence_len):
            state = 0
            for button in sequence:
                state ^= button
            if state == machine.indicator:
                return(sequence)

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            m = Machine()
            m.parse_line(line)
            sequence = turn_on_itertools(m)
            print(f"{m} {[bin(press) for press in sequence]}")
            sum += len(sequence)
    print(sum)
