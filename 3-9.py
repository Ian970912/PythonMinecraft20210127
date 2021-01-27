from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
B =18
H =(B//2)+1

for I in range(H):
    X1=x+I
    Y1=y+I
    Z1=z+I
    X2=x+B-I
    Z2=z+B-I
    mc.setBlocks(X1,Y1,Z1,X2,Y1,Z2,24)