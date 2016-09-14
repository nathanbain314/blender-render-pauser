import bpy
import csv

r = bpy.data.scenes["Scene"].render

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

bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree

# clear default nodes
for node in tree.nodes:
  tree.nodes.remove(node)

# create input image nodes
bpy.ops.image.open(filepath="//out.png")
previous_node = tree.nodes.new(type='CompositorNodeImage')
previous_node.image = bpy.data.images['out.png']
previous_node.location = 0,0

bpy.ops.image.open(filepath="//rows.png")
rows_node = tree.nodes.new(type='CompositorNodeImage')
rows_node.image = bpy.data.images['rows.png']
rows_node.location = 0,-300

alpha_node = tree.nodes.new(type='CompositorNodeAlphaOver')
alpha_node.location = 200,0

comp_node = tree.nodes.new('CompositorNodeComposite')
comp_node.location = 400,0

links = tree.links
link = links.new(previous_node.outputs[0], alpha_node.inputs[1])
link = links.new(rows_node.outputs[0], alpha_node.inputs[2])
link = links.new(alpha_node.outputs[0], comp_node.inputs[0])

bpy.data.scenes['Scene'].render.filepath = '//out.png'
bpy.ops.render.render( write_still=True ) 