import math
import sys

class Circuit():
    def __init__(self):
        self.nodes = set()

    def __str__(self):
        output = '\nCircuit:\n'
        for node in self.nodes:
            output += f"{node}\n"
        return output

    def add(self, node):
        self.nodes.add(node)
        node.circuit = self

    def combine(self, circuit):
        for node in circuit.nodes:
            self.nodes.add(node)
            node.circuit = self


class Node():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = None

    def __str__(self):
        output = f"{self.x},{self.y},{self.z}"
        return output

    def distance(self, node):
        return math.sqrt(
            abs(self.x - node.x)**2
            + abs(self.y - node.y)**2
            + abs(self.z - node.z)**2
        )


if __name__ == "__main__":
    nodes = []
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            x, y, z = line.strip().split(',')
            nodes.append(Node(int(x), int(y), int(z)))

    distances = set()
    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2:
                distance = n1.distance(n2)
                if n1.x < n2.x:
                    distances.add((n1, n2, distance))
                else:
                    distances.add((n2, n1, distance))

    linked = 0
    linked_target = 1000
    circuits = []
    if len(nodes) < 1000:
        linked_target = 10
    print(f"{len(distances)} distances")
    for n1, n2, distance in sorted(distances, key=lambda d: d[2]):
        print(f"{n1} {n2} {distance}")
        connecting = False
        if not n1.circuit and not n2.circuit:
            circuit = Circuit()
            circuit.add(n1)
            circuit.add(n2)
            circuits.append(circuit)
            connecting = True
            linked += 1
        elif not n1.circuit and n2.circuit:
            n2.circuit.add(n1)
            connecting = True
            linked += 1
        elif not n2.circuit and n1.circuit:
            n1.circuit.add(n2)
            connecting = True
            linked += 1
        elif n1.circuit != n2.circuit:
            tmp = n2.circuit
            n1.circuit.combine(n2.circuit)
            circuits.remove(tmp)
            connecting = True
            linked += 1

        if len(circuits[0].nodes) == len(nodes):
            print(n1.x * n2.x)
            break
