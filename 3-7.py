def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)

from mcpi.minecraft import Minecraft
mc=Minecraft.creaft()
x,y,z=mc.player.getTilepos()
for i in range(10):
    plantTree(x+i*5,y,z)