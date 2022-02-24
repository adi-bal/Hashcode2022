class contributer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills #dictionary that holds skill - levels
    def show():
        print("{} {}".format(name ))

class project:
    def __init__(self, name, days, score, bbefore, nroles, skills):
        self.name = name
        self.days = days
        self.score = score
        self.bbefore = bbefore
        self.nroles = nroles
        self.skills = skills
contributers = list()
projects = list() 

f = open("a_an_example.in.txt", "r")
input = f.readlines()
f.close()
contributers = input[0][0]
projects = input[0][1]
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
    contributers.append(new_contributer)
    contributers -=1
        
while(projects):
    name = input[i][0]
    i += 1
    days = input[i][0]
    i += 1
    score  = input[i][0]
    i += 1
    bbefore = input[i][0]
    i += 1
    nroles = input[i][0]
    i += 1
    skills = dict()
    for _ in range(nroles):
        skills[input[i][0]] = input[i][1]
        i +=1
    new_project = project(name, days, score, bbefore, nroles, skills)    


for c in contributer:
    c.show()