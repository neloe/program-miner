import json
from collections import defaultdict


def rtopo(g, vis, n, ordering):
    vis.add(n)
    for neighbor in g[n]:
        if not neighbor in vis:
            rtopo(g, vis, neighbor, ordering)
    ordering.append(n)

def toposort(g, classes):
    visited = set()
    ordering = []
    for c in classes:
        if not c in visited:
            rtopo(g, visited, c, ordering)
    ordering.reverse()
    #print(ordering)
    maths = [c for c in ordering if c.startswith('17')]
    cs = [c for c in ordering if c.startswith('44')]
    neither = [c for c in ordering if not c.startswith('17') and not c.startswith('44')]
    return sorted(maths) + neither + sorted(cs)


if __name__ == '__main__':
    with open('2020-2021/dsireqs.json', 'r') as f:
        classes = json.load(f)
    with open('2020-2021/allprereqs.json', 'r') as f:
        prereqs = json.load(f)
    interesting_courses = {c: prereqs[c] for c in classes}
    graph = defaultdict(list)
    for c in interesting_courses:
        for pr in interesting_courses[c]:
            graph[pr].append(c)

    l = toposort(graph, interesting_courses.keys())
    print(l)
    '''
    l.reverse()
    prefixes = []
    prefixindex = dict()
    index = 0
    for c in l:
        if c[:2] not in prefixindex:
            prefixes.append([])
            prefixindex[c[:2]] = index
            index += 1
        prefixes[prefixindex[c[:2]]].append(c)
    order = []
    for p in prefixes:
        order.extend(sorted(p))
    print(order)'''
