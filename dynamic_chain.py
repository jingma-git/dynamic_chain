import maya.cmds as cmds

joint = cmds.ls(selection=True, type="joint")
joints = cmds.listRelatives(joint, allDescendents=True)
joints += joint
joints = joints[::-1]
positions = []
for joint in joints:
    print(joint)
    jpos = cmds.xform(joint, query=True, translation=True, worldSpace=True)
    positions.append(jpos)

cmds.curve(p=positions)