
# case_assignment.py

import logging

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/CaseManagement/Logs/case_assignment.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example dictionary to represent agent availability
agent_availability = {
    'A001': {'available': True, 'level': 'Senior'},
    'A002': {'available': False, 'level': 'Junior'},
    'A003': {'available': True, 'level': 'Mid-Level'},
    'A004': {'available': True, 'level': 'Senior'},
}

def find_available_agent(priority_level):
    """
    Finds an available agent suitable for the given priority level.
    Args:
        priority_level (str): Priority level of the case ('High', 'Medium', 'Low').
    Returns:
        str: The ID of an available agent, or None if no suitable agent is found.
    """
    for agent_id, info in agent_availability.items():
        if info['available']:
            if priority_level == 'High' and info['level'] == 'Senior':
                return agent_id
            elif priority_level == 'Medium' and info['level'] in ['Mid-Level', 'Senior']:
                return agent_id
            elif priority_level == 'Low':
                return agent_id
    return None

def assign_case(case_id, priority_level):
    """
    Assigns a case to the most suitable available agent based on priority level.
    Args:
        case_id (int): Unique identifier for the case.
        priority_level (str): Priority level of the case ('High', 'Medium', 'Low').
    Returns:
        str: The assigned agent's ID, or None if assignment fails.
    """
    try:
        # Validate inputs
        if not isinstance(case_id, int) or not isinstance(priority_level, str):
            raise ValueError("Invalid input types")

        # Find a suitable available agent
        agent_id = find_available_agent(priority_level)
        if not agent_id:
            raise ValueError("No suitable available agent found")

        # Mark the agent as not available
        agent_availability[agent_id]['available'] = False

        # Log the assignment
        logging.info(f'Case {case_id} assigned to Agent {agent_id} ({agent_availability[agent_id]["level"]})')
        print(f'Case {case_id} assigned to Agent {agent_id} ({agent_availability[agent_id]["level"]})')
        return agent_id

    except ValueError as e:
        logging.error(f'Error in assigning case {case_id}: {e}')
        print(f'Error: {e}')
        return None

# Example usage
if __name__ == "__main__":
    assign_case(case_id=12345, priority_level='High')
