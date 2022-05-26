from manim import *
def get_path_pending(path,proportion,dx=0.001):
    if proportion<1:
        coord_y=path.point_from_proportion(proportion)
        coord_x=path.point_from_proportion(proportion+dx)
    else:
        coord_y=path.point_from_proportion(proportion-dx)
        coord_x=path.point_from_proportion(proportion)
    line=Line(coord_y,coord_x)
    return line.get_angle()
class ShiftAndRotateAlongPath(Animation):
    CONFIG={
        'run_time':5,
        'rate_func': smooth,
        'dx':0.001,
    }
    def __init__(self, mobject, path, dx=0.001, **kwargs):
        Animation.__init__(self, mobject, **kwargs)
        assert(isinstance(mobject, Mobject))
        self.mobject=mobject
        self.dx=dx
        self.path=path
    def interpolate_mobject(self,alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.move_to(self.path.point_from_proportion(alpha))
        angle=get_path_pending(self.path,alpha,self.dx)
        self.mobject.rotate(angle,about_point=self.mobject.get_center())
class MoveAlongPathWithRotation(Scene):
    def construct(self):
        path=Line(LEFT*5,RIGHT*5,stroke_opacity=1)
        path.points[0]+=DOWN
        path.points[1]+=UP*4
        path.points[2]+=DOWN*4
        start_angle=get_path_pending(path,0)
        triangle=Polygon(ORIGIN,UP,UP+RIGHT,color=RED)
        triangle.set_height(.8)
        triangle.rotate(get_path_pending(path,0)+PI,about_point=triangle.get_center())
        self.add(triangle,path)
        self.play(
            ShiftAndRotateAlongPath(triangle,path),
            runt_time=4
        )
        self.wait()