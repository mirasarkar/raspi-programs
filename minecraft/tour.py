from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x=0
y=0
z=0
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=54
y=0
z=18
mc.player.setTilePos(x,y,z)

