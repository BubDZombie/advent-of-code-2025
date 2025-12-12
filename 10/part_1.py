import itertools
import re
import sys

class Machine():
    def __init__(self):
        self.buttons = []
        self.history = []
        self.indicator = None
        self.joltages = []
        self.joltage_requirements = []
        self.state = 0

    def __str__(self):
        output = f"Indicator: [{bin(self.indicator)}]"
        output += f" State: [{bin(self.state)}]"
        output += '\n  Buttons: ('
        output += ' '.join([bin(button) for button in self.buttons])
        output += ')'
        output += f"\n  Joltage Req: {self.joltage_requirements}"
        output += f" Curr: {self.joltages}"
        output += f" Need: {[self.joltage_requirements[i] - self.joltages[i] for i in range(len(self.joltages))]}"
        return output

    def add_button(self, button):
        new_button = 0
        for i in button:
            new_button = new_button | 1<<i
        self.buttons.append(new_button)

    def jolted(self):
        return self.joltages == self.joltage_requirements

    def on(self):
        return self.state == self.indicator

    def parse_line(self, line):
        matches = re.match('\\[(.+)\\] (\\(.+\\)) \\{(.+)\\}', line)
        indicator, buttons, joltages = matches.groups()
        self.set_indicator(indicator)
        for button_string in buttons.split():
            button = []
            for i in button_string[1:-1].split(','):
                button.append(int(i))
            self.add_button(button)
        self.set_joltage_requirements([int(joltage) for joltage in joltages.split(',')])

    def press(self, button):
        self.state ^= button
        for i in range(len(self.joltages)):
            if button & 1<<i:
                self.joltages[i] += 1

    def reset(self):
        self.state = 0
        self.joltages = [0 for joltage in self.joltage_requirements]

    def set_indicator(self, indicator_string):
        self.indicator = 0
        for i, char in enumerate(indicator_string):
            if char == '#':
                self.indicator = self.indicator | 1<<i

    def set_joltage_requirements(self, joltages):
        self.joltage_requirements = joltages
        self.joltages = [0 for joltage in joltages]

    def similarity(self):
        return self.indicator & self.state

def turn_on(machine):
    print(f"Starting {machine}")
    for i in range(len(machine.buttons)):
        sequence_len = i + 1
        for sequence in itertools.combinations(machine.buttons, sequence_len):
            machine.reset()
            for button in sequence:
                machine.press(button)
            if machine.on():
                return(sequence)

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            m = Machine()
            m.parse_line(line)
            sequence = turn_on(m)
            print(f"{m} {[bin(press) for press in sequence]}")
            sum += len(sequence)
    print(sum)
