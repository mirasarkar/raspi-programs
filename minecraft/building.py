from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# where to build the house
x=-95
y=9.0
z=74.8
 
# size of the house
width=5
height=4
length=7

# different types of blocks
ice=79
air=0
water=8
stone=1

# use setBlocks to make a building
mc.setBlocks(x,y,z,x+width,y+height,z+length,stone)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,ice)
mc.setBlocks(x+1,y,z+1,x+width-1,y+height-1,z+length-1,air)

#time.sleep(20)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,air)
mc.setBlocks(x,y+height,z,x+width,y+height*2,z+length,stone)
mc.setBlocks(x+1,y+height+1,z+1,x+width-1,y+height*2-1,z+length-1,air)
