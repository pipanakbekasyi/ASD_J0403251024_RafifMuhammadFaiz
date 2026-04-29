#=========================================
# Rafif Muhammad Faiz
# J0403251024 TPL B2
# Implementasi Graf
#=========================================

graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C'],
}

for node in graph:
    print(node, '->', graph[node])