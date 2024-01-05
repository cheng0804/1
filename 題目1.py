class member:
    def __init__(self,name,id,gender):
        self.name = name 
        self.id = id
        self.gender = gender
c1 = member ("小明","01","男")
c2 = member ("小華","02","女")
c3 = member ("小王","03","男")
print("名字:",c1.name)
print("編號:",c2.id)
print("名字:",c2.name)
print("編號:",c1.id)
print("性別:",c1.gender)
print("性別:",c2.gender)
print("名字:",c3.name)
print("編號:",c3.id)
print("性別:",c3.gender)
