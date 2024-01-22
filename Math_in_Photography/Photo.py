from manimlib import *
import numpy

RuntimeLog = open("Log.txt", "w")

def Lens(Rad:float=2, ArRad:float=5) -> VGroup:
  ArcDeg = (float)(np.arcsin(Rad / ArRad))
  RuntimeLog.write("\FlR" + str(Rad) +  " " + str(ArRad))
  RuntimeLog.write("\nFaaq" + str(ArcDeg))
  Right = Arc(radius = ArRad, start_angle = -ArcDeg, angle = ArcDeg * 2)
  Left = Right.copy().flip().next_to(Right, LEFT, buff=0)
  VGroup(Right, Left).move_to([0,0,0])
  return VGroup(Right, Left)

class XYLine():
  """ y = ax + b"""
  def __init__(self, a_val, b_val):
    self.a = a_val
    self.b = b_val
  def Intersection(self, Other):
    if(self.a - Other.a == 0):
      return [100, 100, 0]
    X = (Other.b - self.b) / (self.a - Other.a)
    return [X, self.a * X + self.b, 0]

class UsageofLens(Scene):
  def construct(self):
    R = 2
    Focu = 2.5
    u_val = 6
    PCnt = 11

    CLens = Lens(R, 5).set_color(BLUE)
    Cent = Dot([0,0,0])
    Focus1 = Dot([-Focu,0,0])
    Focus2 = Dot([Focu,0,0])
    Obj = Dot([-u_val,R,0])
    NewObj = Dot([-u_val,-R,0])
    self.play(FadeIn(VGroup(CLens, Cent, Focus1, Focus2)))
    
    LB2 = XYLine(-(R / u_val), 0)
    LB3 = XYLine(-(R / Focu), R)
    InterP = LB2.Intersection(LB3)
    Inter = Dot(InterP)
    Sensor = Line([InterP[0], -3, 0], [InterP[0], 3, 0]).set_color(YELLOW)
    self.play(FadeIn(VGroup(Obj, Sensor)))
    
    BeamsG = VGroup()
    Beams = []
    CurY = R
    Del = 2 * R / (PCnt - 1)

    for i in range(0, PCnt) :
      if(i * 2 + 1 == PCnt):
        Beam2 = Line([-u_val,R,0], [2 * u_val,-2 * R,0]).set_color(BLUE)
        Beams.append(Beam2)
      else:
        Beam1 = Line([-u_val,R,0], [0,CurY,0]).set_color(BLUE)
        Beam3 = Line([0,CurY,0], [3 * InterP[0], CurY - (3 * (CurY - InterP[1])),0]).set_color(BLUE)
        Beams.append(VGroup(Beam1, Beam3))
      BeamsG.add(Beams[i])
      CurY = CurY - Del

    self.play(Write(BeamsG))
    self.play(FadeIn(Inter))

    NewBeamsG = VGroup()
    NewBeams = []
    InterP[1] = -InterP[1]
    NewInter = Dot(InterP)

    CurY = R

    for i in range(0, PCnt) :
      if(i * 2 + 1 == PCnt):
        Beam2 = Line([-u_val,-R,0], [2 * u_val,2 * R,0]).set_color(BLUE)
        NewBeams.append(Beam2)
      else:
        Beam1 = Line([-u_val,-R,0], [0,CurY,0]).set_color(BLUE)
        Beam3 = Line([0,CurY,0], [3 * InterP[0], CurY - (3 * (CurY - InterP[1])),0]).set_color(BLUE)
        NewBeams.append(VGroup(Beam1, Beam3))
      NewBeamsG.add(NewBeams[i])
      CurY = CurY - Del

    self.play(ReplacementTransform(BeamsG, NewBeamsG),ReplacementTransform(Inter, NewInter),ReplacementTransform(Obj, NewObj))

    self.wait(1)

class Spherical(Scene):
  def construct(self):
    BCnt = 7
    Focu = 4
    Focus = Dot([Focu,0,0])

    CLens = Lens(3, 10).set_color(BLUE)
    RCir = Circle(radius=9.8).align_to(CLens, LEFT)
    LCir = Circle(radius=9.8).align_to(CLens, RIGHT)
    self.play(FadeIn(RCir), FadeIn(LCir))
    self.play(FadeIn(Line([-8,0,0],[8,0,0])), FadeIn(CLens), FadeIn(Focus))
    self.play(FadeOut(RCir), FadeOut(LCir))
    self.wait(1)
    
    CurY = 2.5
    Del = CurY * 2 / (BCnt - 1)
    Beams = VGroup()

    for i in range (0, BCnt) :
      Beam1 = Line([-8, CurY, 0], [0, CurY, 0]).set_color(GREEN)
      Beam2 = Line([0, CurY, 0], [3*(Focu - abs(CurY) * 0.5), -2 * CurY, 0]).set_color(GREEN)
      Beams.add(VGroup(Beam1, Beam2))
      CurY -= Del

    self.play(Write(Beams, run_time = 2))

    self.wait(1)

class Frequency(Scene):
  def construct(self):
    BCnt = 7
    Focu = 4
    Focus = Dot([Focu,0,0])

    CLens = Lens(3, 10).set_color(BLUE)
    self.play(FadeIn(Line([-8,0,0],[8,0,0])), FadeIn(CLens), FadeIn(Focus))
    self.wait(1)
    
    CurY = 2.3
    Beam0 = Line([-8, CurY, 0], [0, CurY, 0])
    Beam1 = Line([0, CurY, 0], [3*(Focu), -2 * CurY, 0]).set_color(GREEN)
    Beam2 = Line([0, CurY, 0], [3*(Focu) + 1.5, -2 * CurY, 0]).set_color(YELLOW)
    Beam3 = Line([0, CurY, 0], [3*(Focu) + 3, -2 * CurY, 0]).set_color(RED)
    Beam4 = Line([0, CurY, 0], [3*(Focu) - 1.5, -2 * CurY, 0]).set_color(BLUE)
    Beam5 = Line([0, CurY, 0], [3*(Focu) - 3, -2 * CurY, 0]).set_color(PURPLE)
    Beams = VGroup(Beam0, VGroup(Beam3, Beam2, Beam1, Beam4, Beam5))

    self.play(Write(Beams, run_time = 2))

    self.wait(1)

class ComplAdd(Scene):
  def construct(self):
    MyLens = Lens(2, 5).set_color(BLUE)
    NewLens1 = Lens(5, 100).set_color(BLUE)
    NewLens2 = Line([0, -10, 0], [0, 10, 0]).set_color(BLUE)
    self.play(Write(MyLens, run_time=2))
    self.wait(1)
    self.play(ReplacementTransform(MyLens, NewLens1))
    self.play(ReplacementTransform(NewLens1, NewLens2))
    self.wait(1)

class Perpendicular(Scene):
  def construct(self):
    Focu = 4
    Focus = Dot([Focu,0,0])
    Cent = Dot([0,0,0])
    CLens = Line([0, -5, 0], [0, 5, 0]).set_color(BLUE)

    self.add(VGroup(Focus, Cent, CLens))

    Beam1 = Line([-8,3,0], [0,3,0])
    Beam2 = Line([0,3,0], [Focu * 2,-3,0])
    self.play(ShowCreation(VGroup(Beam1, Beam2)))

    Beam3 = Line([-8,-3,0], [0,-3,0])
    Beam4 = Line([0,-3,0], [Focu * 2,3,0])
    self.play(ReplacementTransform(VGroup(Beam1, Beam2), VGroup(Beam3, Beam4)))

class Straight(Scene):
  def construct(self):
    Focu = 4
    Focus = Dot([Focu,0,0])
    Cent = Dot([0,0,0])
    CLens = Line([0, -5, 0], [0, 5, 0]).set_color(BLUE)

    self.add(VGroup(Focus, Cent, CLens))

    Beam1 = Line([-8,5,0], [8,-5,0])
    Beam2 = Line([-8,-5,0], [8,5,0])

    self.play(ShowCreation(Beam1))
    self.play(ReplacementTransform(Beam1, Beam2))

class PointLight(Scene):
  def construct(self):
    R = 3
    Focu = 3
    u_val = 6.5
    PCnt = 11

    CLens = Line([0, -5, 0], [0, 5, 0]).set_color(BLUE)
    Cent = Dot([0,0,0])
    Focus = Dot([Focu,0,0])
    Obj = Dot([-u_val,R + 0.5,0])
    NewObj = Dot([-u_val,-R - 0.5,0])
    self.add(VGroup(Focus, Cent, CLens))
    self.play(FadeIn(VGroup(Obj)))
    
    BeamsG = VGroup()
    CurY = R
    Del = 2 * R / (PCnt - 1)
    LB2 = XYLine(-((R + 0.5) / u_val), 0)
    LB3 = XYLine(-((R + 0.5) / Focu), R)
    InterP = LB2.Intersection(LB3)

    for i in range(0, PCnt) :
      Beam1 = Line([-u_val,R + 0.5,0], [0,CurY,0])
      Beam3 = Line([0,CurY,0], [3 * InterP[0], CurY - (3 * (CurY - InterP[1])),0])
      BeamsG.add(VGroup(Beam1, Beam3))
      CurY = CurY - Del

    self.play(Write(BeamsG))

    NewBeamsG = VGroup()
    InterP[1] = -InterP[1]

    CurY = R

    for i in range(0, PCnt) :
      Beam1 = Line([-u_val,-R-0.5,0], [0,CurY,0])
      Beam3 = Line([0,CurY,0], [3 * InterP[0], CurY - (3 * (CurY - InterP[1])),0])
      NewBeamsG.add(VGroup(Beam1, Beam3))
      CurY = CurY - Del

    self.play(ReplacementTransform(BeamsG, NewBeamsG),ReplacementTransform(Obj, NewObj))

    self.wait(1)

class TitleModel(Scene):
  def construct(self):
    Text0 = VGroup(Text("Simplified Optical Model"), Text("of a Camera")).arrange(DOWN)
    Text1 = Text("Optics", size=50).shift(LEFT * 3)
    Text2 = Text("Physics", size=50).shift(RIGHT * 3)
    Text3 = Text("Geometry", size=50)
    Text4 = Tex(R"f(x)").scale(3)
    Text5 = Tex(R"f(x) = ...").scale(3)

    self.play(FadeIn(Text0))
    self.play(FadeOut(Text0))
    self.wait(1)

    self.play(Write(Text1))
    self.play(Write(Text2))
    self.play(ReplacementTransform(VGroup(Text1, Text2), Text3))
    self.wait(1)
    self.play(FadeOut(Text3))

    Text4.align_to(Text5, LEFT)
    self.play(Write(Text4))
    self.wait(1)
    self.play(FadeIn(Text5))
    self.remove(Text4)

# manimgl Photo.py ShowLens -o -c "BLACK" --frame_rate 10
# manimgl Photo.py UsageofLens -o -c "BLACK" --frame_rate 10
# manimgl Photo.py Spherical -o -c "BLACK" --frame_rate 10
# manimgl Photo.py Perpendicular -o -c "BLACK" --frame_rate 10
# manimgl Photo.py PointLight -o -c "BLACK" --frame_rate 10
# manimgl Photo.py Straight -o -c "BLACK" --frame_rate 10
# manimgl Photo.py Frequency -o -c "BLACK" --frame_rate 10
# manimgl Photo.py TitleModel -o -c "BLACK" --frame_rate 10