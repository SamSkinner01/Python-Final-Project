def get_instructors():
    with open('instructor.txt') as f:
        inst = {}

        line = f.readline()

        while line != '':
            fields = line.split(',')
            id = fields[0]
            name = fields[1]
            dept_id = fields[2].rstrip('\n')
            inst[id] = [name, dept_id]
            line = f.readline()

    return inst
        
        
    
def get_department():
    with open('department.txt') as f:
        dept = {}

        line = f.readline()

        while line != '':
            fields = line.split(',')
            dept_name = fields[0]
            loc = fields[1]
            budget = fields[2].rstrip('\n')
            dept[dept_name] = [loc, budget]
            line = f.readline()

    return dept