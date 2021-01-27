from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
O=8
nuber=1
for i in range(O):
    for j in range(nuber):
        mc.spawnEntity(x,y,z,60)
    nuber=nuber*2
    mc.postToChat("生成了"+str(nuber)+"隻蠹魚")