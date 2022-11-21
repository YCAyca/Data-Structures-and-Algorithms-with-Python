from docplex.mp.model import Model

def minimum_cost_flow_problem(costs_file, capacities_file, flows_file):
    file = open(costs_file, "r")
    
    # costs (c)
    costs = []
    # capacities (u)
    capacities  = []
    # flows (b)
    flows = []
    
    
    for line in file:
        costs.append(line.strip(" ")[2])
    file.close()
    
    file = open(capacities_file, "r")
    for line in file:
        capacities.append(line.strip(" ")[2])
    file.close()
    
    file = open(flows_file, "r")
    for line in file:
        flows.append(line.strip(" ")[1])
    file.close()
    
    
    model = Model('Max Flow/Min Cost')
       
    # Node Names x[0], x[1], x[2], x[3], x[4], x[5], x[6] to solve
    names = ["12", "13", "14", "23", "35", "45", "54"] 
    # costs (c)
    costs = [2, 4, 9, 3, 1, 3, 2]
    # capacities (u)
    capacities = [10, 90, 90, 90, 80, 90, 90]
    # flows (b)
    flows = [50, 40, 0,-30,-60]
    #x
    x = model.continuous_var_list(7, name="x")
    
    objective = sum(costs[i]*x[i] for i in range(7)) 
    model.set_objective("min", objective)

    # constraints
    
    model.add_constraint(0 <= x[0])
    model.add_constraint(x[0] <= capacities[0])
    model.add_constraint(0 <= x[1])
    model.add_constraint(x[1] <= capacities[1])
    model.add_constraint(0 <= x[2])
    model.add_constraint(x[2] <= capacities[2])
    model.add_constraint(0 <= x[3])
    model.add_constraint(x[3] <= capacities[3])
    model.add_constraint(0 <= x[4])
    model.add_constraint(x[4] <= capacities[4])
    model.add_constraint(0 <= x[5])
    model.add_constraint(x[5] <= capacities[5])
    model.add_constraint(0 <= x[6])
    model.add_constraint(x[6] <= capacities[6])
    model.add_constraint((x[0] + x[1] + x[2]) == flows[0])
    model.add_constraint((-x[0] + x[3]) == flows[1])
    model.add_constraint((-x[1] + -x[3] + x[4]) == flows[2])
    model.add_constraint((-x[2] + x[5] - x[6]) == flows[3])
    model.add_constraint((-x[4] - x[5] + x[6]) == flows[4])
    
    model.print_information()
    solution = model.solve()
  
    model.print_solution()  
  
    objective = solution.get_objective_value()
    x = solution.get_value_list(x)
  
    return(x, objective)

def _main():
  
    minimum_cost_flow_problem("costs.txt", "capacities.txt", "flows.txt")    
  
    
if __name__ == "__main__":
    _main()