import renderer,lvl_loader
def controler():
    target = None
    inp=""
    while True:
        inp = input().split(" ")
        command = inp[0]
        arg1=inp[1]
        if command == "move":
            if arg1 == "up":
                renderer.player.move((0,-2))
            if arg1 == "down":
                renderer.player.move((0,2))
            if arg1 == "left":
                renderer.player.move((-2,0))
            if arg1 == "right":
                renderer.player.move((2,0))
        if command == "attack":
            if arg1 == "up":
                target=renderer.get_enemy_from_pos((renderer.player.pos[0],renderer.player.pos[1]-2))
            elif arg1 == "down":
                target=renderer.get_enemy_from_pos((renderer.player.pos[0],renderer.player.pos[1]+2))
            elif arg1 == "left":
                target=renderer.get_enemy_from_pos((renderer.player.pos[0]-2,renderer.player.pos[1]))
            elif arg1 == "right":
                target=renderer.get_enemy_from_pos((renderer.player.pos[0]+2,renderer.player.pos[1]))
            else:
                print("you didn't enter a position")
            if target != None:
                target.hp -= renderer.player.damage
                if target.hp <= 0:
                    renderer.enemies.pop(renderer.enemies.index(target))
            else:
                print("there is no target there")
        for i in renderer.enemies:
            if renderer.player.pos in [(i.pos[0],i.pos[1]+2),(i.pos[0],i.pos[1]-2),(i.pos[0]-2,i.pos[1]),(i.pos[0]+2,i.pos[1]+2)]:
                renderer.player.hp -= i.damage
                if renderer.player.hp <=0:
                    renderer.enemies.pop(renderer.enemies.index(renderer.player))

lvl_loader.load(input("input lvl"))


renderer.player =renderer.enemy((0,0,255),(9,9),9,20,1)
renderer.enemies.append(renderer.player)

renderer.Thread(target=controler).start()
