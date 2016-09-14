import bpy
import csv
import math

r = bpy.data.scenes["Scene"].render

try:
  f = open( "data.csv" )
  reader = csv.reader(f)
  row = next(reader)
  r.resolution_x                       = int(row[0])
  r.resolution_y                       = int(row[1])
  r.tile_x                             = int(row[2])
  r.tile_y                             = int(row[3])
  current_x                            = int(row[4])
  current_y                            = int(row[5])
  bpy.data.scenes["Scene"].cycles.seed = int(row[6])
  r.resolution_percentage              = int(row[7])
  f.close()
  file_name = "rows.png"
except:
  current_x = 0
  current_y = 0
  file_name = "out.png"
finally:  
  width = r.resolution_x
  height = r.resolution_y
  x = r.tile_x
  y = r.tile_y
  seed = bpy.data.scenes["Scene"].cycles.seed
  factor = r.resolution_percentage
  r.use_border = True
  
  """
  if current_x > 0:
    output_name = "row.png"
    r.border_min_x = 100*current_x*x/(width*factor)
    r.border_min_y = 100*current_y*y/(height*factor)
    r.border_max_x = 1
    r.border_max_y = 100*(current_y+1)*y/(height*factor)
    bpy.ops.render.render( use_viewport=True )
    bpy.data.images['Render Result'].save_render(filepath="row.png")
  """

  if 100*current_y*y/(height*factor) <= 1:
    output_name = "rows.png"
    r.border_min_x = 100*current_x*x/(width*factor)
    r.border_min_y = 100*current_y*y/(height*factor)
    r.border_max_x = 1
    r.border_max_y = 1
    bpy.ops.render.render( use_viewport=True )
    bpy.data.images['Render Result'].save_render(filepath=file_name)
  
  tiles_done = int(input("Enter last tile worked on: ")) - 4
  num_per_row = math.ceil( width*factor/(100 * x) )
  current_y += tiles_done // num_per_row
  f = open( "data.csv", 'w' )
  writer = csv.writer(f)
  writer.writerow([width,height,x,y,current_x,current_y,seed,factor])
  f.close()

