def calculate_agent_costs(path):
    if not path:
        return []

    positions, _ = path[0]
    agent_costs = [0] * len(positions)

    for i in range(1, len(path)):
        previous_positions, _ = path[i - 1]
        current_positions, _ = path[i]

        for agent_index in range(len(positions)):
            if previous_positions[agent_index] != current_positions[agent_index]:
                agent_costs[agent_index] += 1

    return agent_costs