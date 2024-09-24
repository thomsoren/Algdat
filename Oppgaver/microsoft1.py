from collections import defaultdict

def solution(V, A, B):
    N = len(V)
    graph = defaultdict(list)
    for a, b in zip(A, B):
        graph[b].append(a)  # b depends on a

    memo = {}

    def get_dependencies(node, visiting):
        if node in memo:
            return memo[node]
        if node in visiting:
            return None  # Cycle detected
        visiting.add(node)
        deps = set()
        for dep in graph.get(node, []):
            result = get_dependencies(dep, visiting)
            if result is None:
                return None  # Cycle detected
            deps.add(dep)
            deps.update(result)
        visiting.remove(node)
        memo[node] = deps
        return deps

    max_value = float('-inf')

    # Consider initiating one project
    for i in range(N):
        visiting = set()
        deps = get_dependencies(i, visiting)
        if deps is None:
            continue  # Skip projects involved in cycles
        total_projects = len(deps) + 1  # Including the project itself
        if total_projects <= 2:
            total_value = V[i] + sum(V[dep] for dep in deps)
            max_value = max(max_value, total_value)

    # Consider initiating two projects
    for i in range(N):
        for j in range(i + 1, N):
            visiting_i = set()
            deps_i = get_dependencies(i, visiting_i)
            visiting_j = set()
            deps_j = get_dependencies(j, visiting_j)
            if deps_i is None or deps_j is None:
                continue  # Skip if any project is involved in a cycle
            included_projects = set([i, j]) | deps_i | deps_j
            total_projects = len(included_projects)
            if total_projects <= 2:
                total_value = sum(V[k] for k in included_projects)
                max_value = max(max_value, total_value)

    return max_value if max_value != float('-inf') else max(V)

# Example test cases:
print(solution([-3, 5, 7, 2, 3], [3, 1], [2, 4]))  # Expected Output: 9
print(solution([1, 1, 5], [0, 1], [2, 2]))        # Expected Output: 2
print(solution([5, 6, 6, 7, -10], [0, 0, 0, 1, 2, 3], [1, 2, 3, 1, 2, 3]))  # Expected Output: 5