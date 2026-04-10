casha = dict()
for _ in range(int(input())):
    name, *food = input().split()
    for x in food:
        if x not in casha:
            casha[x] = [name]
        else:
            casha[x].append(name)
z = input()
if z not in casha:
    print('Таких нет')
else:
    print(*sorted(casha[z]), sep='\n')
