from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x=45.2
y=0.0
z=95.4
mc.player.setTilePos(x,y,z)
time.sleep(2)

x=7.3
y=9.0
z=65.8
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=45.2
y=0.0
z=95.4
mc.player.setTilePos(x,y,z)

