import sys

if __name__ == '__main__':
    graph = {}
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            key, val_string = line.split(':')
            vals = val_string.strip().split()
            graph[key] = vals
            # for val in vals:
            #     print(f"{key} -> {val}")
    q = [['you']]
    num_paths = 0
    while len(q):
        path = q.pop(0)
        if 'out' in graph[path[-1]]:
            num_paths += 1
        elif len(path) < len(graph):
            for val in graph[path[-1]]:
                q.append(path + [val])
    print(f"{num_paths} paths from you to out.")
