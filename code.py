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
    def show(self):
        print("{} {} {} {} {} {}".format(self.name, self.days, self.score, self.bbefore, self.nroles, self.skills ))
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


while(projects):
    name = input[i][0]
    days = int(input[i][1])
    score  = int(input[i][2])
    bbefore = int(input[i][3])
    nroles = int(input[i][4])
    i += 1
    skills = dict()
    for _ in range(nroles):
        skills[input[i][0]] = input[i][1]
        i +=1
    new_project = project(name, days, score, bbefore, nroles, skills)
    projects_list.append(new_project)
    projects -=1    