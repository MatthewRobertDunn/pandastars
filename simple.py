
from math import cos, pi, sin
from random import random

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # render.setShaderAuto()
        base.setBackgroundColor(0, 0, 0)
        lens = PerspectiveLens()
        lens.setFilmSize(80*0.8, 60*0.8)  # Or whatever is appropriate for your scene
        lens.setNearFar(0.1,1000)
        base.cam.node().setLens(lens)
        base.cam.setPos(0,-100,0)
        
        self.squares()
        self.accept('c',self.ShowCamPos)
        self.taskMgr.add(self.task, "MyTask")
    
    
    def ShowCamPos(self):
#        position = environ.getPos()
        x=base.camera.getX()
        y=base.camera.getY()
        z=base.camera.getZ()
        print(str(x)+":"+str(y)+":"+str(z))

    def task(self, task):
        #viewTransform =self.camLens.getProjectionMatInv()
        #up = viewTransform.xform(Vec4F(0.0,-1.0,0, 0)).normalized()
        #right = viewTransform.xform(Vec4F(1.0,0.0,0, 0)).normalized()
        
        up = render.getRelativeVector(base.camera, Vec3F(0.0,0.0,-1.0)).normalized()
        right = render.getRelativeVector(base.camera, Vec3F(1.0,0.0,0.0)).normalized()
        self.star_path.set_shader_input("camUp", up)
        self.star_path.set_shader_input("camRight", right)
        
        
        return Task.cont

    def get_random(self, s):
        return (random() - 0.5) * s

    def squares(self):
        myShader = Shader.load(lang = Shader.SL_GLSL,
                        vertex="starshader.vert",
                        fragment="starshader.frag",
                        geometry="starshader.geom")
                        
        format = GeomVertexFormat.getV3c4();
        vdata = GeomVertexData('my list', format, Geom.UHStatic)
        vertex = GeomVertexWriter(vdata, 'vertex')
        color = GeomVertexWriter(vdata, 'color')
        
        num_points = 1000000
        
        for _ in range(num_points):
            vertex.addData3(self.get_random(100),self.get_random(100),self.get_random(100))
            color.addData4(random(),random(),random(), 1.0)
        
        gpoints = GeomPoints(Geom.UHStatic)
        
        


        
        gpoints.add_consecutive_vertices(0,num_points)


        geom = Geom(vdata)
        geom.addPrimitive(gpoints)
        snode = GeomNode('points')
        snode.addGeom(geom)

        
        path = NodePath(snode)
        
        #path.setRenderModeThickness(100)
        #path.setRenderModePerspective(True)        
        #path.setTexGen(TextureStage.getDefault(), TexGenAttrib.MPointSprite)
        #path.setRenderMode(RenderModeAttrib.MPoint, 1)
        

        viewTransform = LMatrix4f(base.camLens.getProjectionMat())
        viewTransform.invertInPlace()
        up = viewTransform.xform(Vec4F(0.0,-1.0,0, 0)).normalized()
        right = viewTransform.xform(Vec4F(1.0,0.0,0, 0)).normalized()
        path.set_shader_input("camUp", up)
        path.set_shader_input("camRight", right)
        path.set_shader(myShader)

        self.star_path = path
        
        render.attachNewNode(snode)


app = MyApp()
app.run()
