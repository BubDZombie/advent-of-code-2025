import sys

if __name__ == '__main__':
    graph = {}
    doppelgraph = {}
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            key, val_string = line.split(':')
            vals = val_string.strip().split()
            graph[key] = vals
            for val in vals:
                if val not in doppelgraph:
                    doppelgraph[val] = []
                doppelgraph[val].append(key)

    path_counts = []
    for alpha, omega in [('dac', 'out'), ('fft', 'dac'), ('svr', 'fft')]:
        print(f"{len(graph)} nodes in graph")
        q = [[alpha]]
        num_paths = 0
        while len(q):
            path = q.pop(0)
            if path[-1] == omega:
                num_paths += 1
            elif path[-1] in graph:
                for val in graph[path[-1]]:
                    q.insert(0, path + [val])
        print(f"{num_paths} from {alpha} to {omega}")
        path_counts.append(num_paths)

        print('Finding nodes to keep...')
        useful = set()
        q = [alpha]
        while len(q):
            key = q.pop(0)
            useful.add(key)
            for val in doppelgraph.get(key, []):
                if val not in useful:
                    useful.add(val)
                    q.append(val)
        keys = list(graph.keys())
        for key in keys:
            if key not in useful:
                del(graph[key])

    accum = 1
    for count in path_counts:
        accum *= count
    print(f"For a grand total of {accum} paths")
