from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# where to build the house
x=35
y=0
z=-56

# size of the house
width=3
height=3
length=3

# different types of blocks
ice=79
air=0
water=8
stone=1

# use setBlocks to make a building
mc.setBlocks(x,y,z,x+width,y+height,z+length,stone)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,ice)
mc.setBlocks(x+1,y,z+1,x+width-1,y+height,z+length-1,water)

#time.sleep(20)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,air)
