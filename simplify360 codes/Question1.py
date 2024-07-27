def calculate_schedule(tasks):
    est = {}  
    eft = {}  
    lst = {} 
    lft = {}  
    # Step 1: Calculate EST and EFT
    for task in tasks:
        if task == 'T_START':
            est[task] = 0
        else:
            est[task] = max(eft[dep] for dep in tasks[task]['dependencies'])
        eft[task] = est[task] + tasks[task]['duration']

    # Step 2: Calculate LFT and LST
    end_tasks = [task for task in tasks if not any(task in dep_list for dep_list in tasks.values())]
    max_eft = max(eft[task] for task in end_tasks)
    for task in end_tasks:
        lft[task] = eft[task]
    for task in sorted(tasks, key=lambda t: -eft[t]):
        if task not in lft:
            lft[task] = min(lst[dep] for dep in tasks[task]['dependencies'])
        lst[task] = lft[task] - tasks[task]['duration']
    # Determine critical path
    critical_path = [task for task in tasks if est[task] == lst[task]]
    # Output the results
    earliest_completion_time = max(eft.values())
    latest_completion_time = max(lft.values())
    return {
        'earliest_completion_time': earliest_completion_time,
        'latest_completion_time': latest_completion_time,
        'critical_path': critical_path,
    }

# Example usage
tasks = {
    'T_START': {'duration': 0, 'dependencies': []},
    'A': {'duration': 3, 'dependencies': ['T_START']},
    'B': {'duration': 2, 'dependencies': ['T_START']},
    'C': {'duration': 4, 'dependencies': ['A', 'B']},
    'D': {'duration': 2, 'dependencies': ['C']},
    'E': {'duration': 1, 'dependencies': ['C']},
}
schedule = calculate_schedule(tasks)
print(f"Earliest Completion Time: {schedule['earliest_completion_time']}")
print(f"Latest Completion Time: {schedule['latest_completion_time']}")
print(f"Critical Path: {schedule['critical_path']}")