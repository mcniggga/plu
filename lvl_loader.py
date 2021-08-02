import renderer

def load(file_name:str):
    assets=[]
    data=open(file_name,"r").read().split("\n")
    for i in data:
        assets=i.split(" ")
        if assets[0]=="enemy":
            print(assets)
            renderer.enemies.append(renderer.enemy((255,0,0),(int(assets[1]),int(assets[2])),renderer.size/80,int(assets[3]),int(assets[4])))