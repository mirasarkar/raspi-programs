from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# get the player position
(player_x, player_y, player_z) = mc.player.getTilePos()

# where to build the house
x=player_x-5
y=player_y
z=player_z-5
 
# size of the house
width=10
height=10
length=10

# different types of blocks
ice=79
air=0
water=8
stone=1

# use setBlocks to make a building
mc.setBlocks(x,y,z,x+width,y+height,z+length,stone)
mc.setBlocks(x+1,y,z+1,x+width-1,y+height-1,z+length-1,air)

time.sleep(10)
mc.setBlocks(x,y,z,x+width,y+height,z+length,air)


#mc.setBlocks(x,y,z,x+width,y+height,z+length,ice)
#time.sleep(20)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,air)
#mc.setBlocks(x,y+height,z,x+width,y+height*2,z+length,stone)
#mc.setBlocks(x+1,y+height+1,z+1,x+width-1,y+height*2-1,z+length-1,air)

