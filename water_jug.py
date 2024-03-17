def water_jug_problem(capacity_jug1, capacity_jug2, target):
    state = [0, 0]  
    visited_states = set()  

    while tuple(state) not in visited_states:
        visited_states.add(tuple(state))

        
        if state[0] == target or state[1] == target:
            print("Target amount reached:", state)
            return

      
        if state[0] < capacity_jug1:
            new_state = [capacity_jug1, state[1]]
            if tuple(new_state) not in visited_states:
                print("Fill jug 1:", new_state)
                state = new_state
                continue

     
        if state[1] < capacity_jug2:
            new_state = [state[0], capacity_jug2]
            if tuple(new_state) not in visited_states:
                print("Fill jug 2:", new_state)
                state = new_state
                continue

     
        if state[0] > 0:
            new_state = [0, state[1]]
            if tuple(new_state) not in visited_states:
                print("Empty jug 1:", new_state)
                state = new_state
                continue

      
        if state[1] > 0:
            new_state = [state[0], 0]
            if tuple(new_state) not in visited_states:
                print("Empty jug 2:", new_state)
                state = new_state
                continue

       
        pour_amount = min(state[0], capacity_jug2 - state[1])
        if pour_amount > 0:
            new_state = [state[0] - pour_amount, state[1] + pour_amount]
            if tuple(new_state) not in visited_states:
                print("Pour water from jug 1 to jug 2:", new_state)
                state = new_state
                continue

      
        pour_amount = min(state[1], capacity_jug1 - state[0])
        if pour_amount > 0:
            new_state = [state[0] + pour_amount, state[1] - pour_amount]
            if tuple(new_state) not in visited_states:
                print("Pour water from jug 2 to jug 1:", new_state)
                state = new_state
                continue

    print("Target amount cannot be reached.")

print("Dhruv Varshney")
print("A2305221157")
water_jug_problem(4, 3, 2)
