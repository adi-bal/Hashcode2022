class contributer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills #dictionary that holds skill - levels
    def show(self):
        print("{} {}".format(self.name, self.skills ))

class project:
    def __init__(self, name, days, score, bbefore, nroles, skills):
        self.name = name
        self.days = days
        self.score = score
        self.bbefore = bbefore
        self.nroles = nroles
        self.skills = skills
contributer_list = list()
projects_list = list() 

f = open("a_an_example.in.txt", "r")
input = f.readlines()
f.close()
new_input = list()
for line in input:
    line = line.split(" ")
    new_input.append(line)
print(new_input)

input = new_input


contributers = int(input[0][0])
projects = int(input[0][1])
i =1
while(contributers):
    name = input[i][0]
    n = int(input[i][1])
    i+=1
    skills = dict()
    for _ in range(n):
        skills[input[i][0]] = input[i][1]
        i +=1
    new_contributer = contributer(name, skills)
    contributer_list.append(new_contributer)
    contributers -=1
"""        
while(projects):
    name = input[i][0]
    i += 1
    days = input[i][0]
    i += 1
    score  = input[i][0]
    i += 1
    bbefore = input[i][0]
    i += 1
    nroles = int(input[i][0])
    i += 1
    skills = dict()
    for _ in range(nroles):
        skills[input[i][0]] = input[i][1]
        i +=1
    new_project = project(name, days, score, bbefore, nroles, skills)
    projects_list.append(new_project)    
"""

for c in contributer_list:
    c.show()