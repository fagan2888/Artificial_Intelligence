
import csv
with open('suinput.txt','r') as filein:
    csvreader = csv.reader(filein)
    table = []
    for line in csvreader:
        for num in range(9):
            table.append((line[num]))
table1 = "".join(table)
suinput = table1

def cross(X,Y):
    return [x+y for x in X for y in Y]


col = '123456789'
row = 'ABCDEFGHI'
index = cross(row, col)
namelist = ([cross(row, c) for c in col] +
            [cross(r, col) for r in row] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in namelist if s in u]) for s in index)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in index)


def solve(grid):
    values = dict((s, col) for s in index)
    for s,d in initial_values(grid).items():
        if d in col and not assign_value(values, s, d):
            return False
    return values

def initial_values(grid):
    chars = [c for c in str(grid) if c in col or c in '0']
    return dict(zip(index, chars))


def assign_value(values, s, d):
    others = values[s].replace(d,'')
    if all(delete(values, s, d2) for d2 in others):
        return values
    else:
        return False


def delete(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(delete(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dposition = [s for s in u if d in values[s]]
        if len(dposition) == 0:
            return False
        elif len(dposition) == 1:
            if not assign_value(values, dposition[0], d):
                return False
    return values


def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in index):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in index if len(values[s]) > 1)
    return exit(search(assign_value(values.copy(), s, d))
		for d in values[s])


def exit(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

list = []
num = 0
for i in index:
    num = num + 1
    list.append(int(search(solve(suinput))[i]))


count = 0
for i in range(0,81):
    file = open('suoutput.txt','a')
    file.write(str(list[i]))
    file.write(',')
    count += 1
    if((count % 9)== 0):
        file.write("\n")
file.close()

