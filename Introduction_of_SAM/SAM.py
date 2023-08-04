from manimlib import *
import numpy 
CharaWid = 0.266
HeiRat = 0.589
# RuntimeLog = open("Log.txt", "w")

def CharaBox(CharinBox: str, BoxScale: float=1) -> VGroup:
  ChrtoText = Text(CharinBox).scale(BoxScale)
  VerL = Rectangle(BoxScale * CharaWid, BoxScale * 0.5)
  return VGroup(VerL, ChrtoText)

def TextBox(StringinBox: str, BoxScale: float=1) -> VGroup:
  StringLen = len(StringinBox)
  TextB = VGroup()
  for i in range(0, StringLen):
    TextB += CharaBox(StringinBox[i], BoxScale)
  TextB.arrange(buff=0)
  return TextB

def SAMNode(Strings: str, BoxScale: float=1, Hei: int=1) -> VGroup:
  Len = len(Strings)
  # RuntimeLog.write("\nLen:")
  # RuntimeLog.write(str(Len))
  if(Len == 0):
    # RuntimeLog.write("\nHere")
    return Polygon([BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0], 
                   [BoxScale * CharaWid * 0.5, 0.5 * HeiRat * BoxScale, 0],
                   [-BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0])
  MyNode = VGroup()
  SufT = []
  SufT.append(Text(text=Strings,font_size=BoxScale*24))
  MyNode += SufT[0]
  for i in range(0,Hei - 1):
    Strings = Strings[1:]
    SufT.append(Text(text=Strings,font_size=BoxScale*24))
    SufT[i + 1].move_to(SufT[i])
    SufT[i + 1].shift(UP * HeiRat * BoxScale)
    SufT[i + 1].align_to(SufT[i],RIGHT)
    MyNode += SufT[i + 1]
  LeUp = [(2 * Hei - 2 - Len) * BoxScale * CharaWid * 0.5, (Hei - 0.5) * HeiRat * BoxScale, 0]
  RiUp = [+Len * BoxScale * CharaWid * 0.5, (Hei - 0.5) * HeiRat * BoxScale, 0]
  LeDown = [LeUp[0] - Hei * CharaWid, -0.5 * HeiRat * BoxScale, 0]
  RiDown = [+Len * BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0]
  MyNode += Polygon(LeDown, RiDown, RiUp, LeUp)
  return MyNode

class BANANA(Scene):
  def construct(self):
    GridH = []
    GridV = []
    Nodes = []
    Dots = []
    Arrows = []

    Nodes.append(SAMNode("", 1, 0)) # root
    Nodes.append(SAMNode("b", 1, 2))
    Nodes.append(SAMNode("ba", 1, 3))
    Nodes.append(SAMNode("ban", 1, 4))
    Nodes.append(SAMNode("bana", 1, 5))
    Nodes.append(SAMNode("banan", 1, 6)) 
    Nodes.append(SAMNode("banana", 1, 7))
    
    for i in range(0, 7):
      GridH.append(0)
    
    GridV.append(0.5)
    GridV.append(-0.5)
    GridV.append(0.8)
    GridV.append(-0.7)
    GridV.append(1.1)
    GridV.append(-0.9)
    GridV.append(1.9)
    GridV.append(-1.1)
    GridV.append(1.9)
    GridV.append(-1.3)
    GridV.append(1.9)
    GridV.append(-1.5)

    GridH[0] = -6.8  # add root
    Nodes[0].move_to(RIGHT * GridH[0])
    self.play(FadeIn(Nodes[0]))

    GridH[1] = GridH[0] + 0.5  # add B
    Nodes[1].move_to(UP * 0.5 * HeiRat + RIGHT * GridH[1])
    self.play(FadeIn(Nodes[1]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("b", 1, 1)
    Tmp1.move_to(Nodes[1])
    Tmp1.shift(UP * HeiRat * 0.5)
    Tmp2.next_to(Tmp1, DOWN, buff=0)
    Tmp1.shift(RIGHT * CharaWid * 0.5)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2))
    self.remove(Nodes[1])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 1 + LEFT * (CharaWid * 0.5 + 0.5)))
    self.remove(Tmp1)
    Nodes[1] = Tmp2
    Dots.append(Dot(point=[GridH[0], GridV[1], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[1], GridV[1], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[0], end=Dots[1], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[0]), FadeIn(Dots[0]), FadeIn(Dots[1]))
    Dots.append(Dot(point=[GridH[0], GridV[0], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[1], GridV[0], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[3], end=Dots[2], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[1]), FadeIn(Dots[3]), FadeIn(Dots[2]))

    GridH[2] = GridH[1] + 0.8  # add A
    Nodes[2].move_to(UP * 1 * HeiRat + RIGHT * GridH[2])
    self.play(FadeIn(Nodes[2]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("ba", 1, 2)
    Tmp1.move_to(Nodes[2])
    Tmp1.shift(UP * HeiRat * 1)
    Tmp2.next_to(Tmp1, DOWN, buff=0)
    Tmp1.shift(RIGHT * CharaWid * 1)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2))
    self.remove(Nodes[2])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 2 + LEFT * (CharaWid * 1 + 1.3)))
    self.remove(Tmp1)
    Nodes[2] = Tmp2
    Dots.append(Dot(point=[GridH[0], GridV[3], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[2], GridV[3], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[4], end=Dots[5], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[1], GridV[5], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[2], GridV[5], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[6], end=Dots[7], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[2]),FadeIn(Arrows[3]), FadeIn(Dots[4]), FadeIn(Dots[5]), FadeIn(Dots[6]), FadeIn(Dots[7]))
    Dots.append(Dot(point=[GridH[0], GridV[2], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[2], GridV[2], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[9], end=Dots[8], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[4]), FadeIn(Dots[8]), FadeIn(Dots[9]))

    GridH[3] = GridH[2] + 1.1  # add N
    Nodes[3].move_to(UP * 1.5 * HeiRat + RIGHT * GridH[3])
    self.play(FadeIn(Nodes[3]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("ban", 1, 3)
    Tmp1.move_to(Nodes[3])
    Tmp1.shift(UP * HeiRat * 1.5)
    Tmp2.next_to(Tmp1, DOWN, buff=0)
    Tmp1.shift(RIGHT * CharaWid * 1.5)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2))
    self.remove(Nodes[3])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 3 + LEFT * (CharaWid * 1.5 + 2.4)))
    self.remove(Tmp1)
    Nodes[3] = Tmp2
    Dots.append(Dot(point=[GridH[0], GridV[7], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[3], GridV[7], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[10], end=Dots[11], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[2], GridV[9], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[3], GridV[9], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[12], end=Dots[13], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[5]),FadeIn(Arrows[6]), FadeIn(Dots[10]), FadeIn(Dots[11]), FadeIn(Dots[12]), FadeIn(Dots[13]))
    Dots.append(Dot(point=[GridH[0], GridV[4], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[3], GridV[4], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[15], end=Dots[14], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[7]), FadeIn(Dots[14]), FadeIn(Dots[15]))

    GridH[4] = GridH[3] + 1.4  # add A
    Nodes[4].move_to(UP * 2 * HeiRat + RIGHT * GridH[4])
    self.play(FadeIn(Nodes[4]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("bana", 1, 3)
    Tmp3 = SAMNode("a", 1, 1)
    Tmp1.move_to(Nodes[4])
    Tmp1.shift(UP * HeiRat * 2)
    Tmp3.next_to(Tmp1, DOWN, buff=0)
    Tmp2.next_to(Tmp3, DOWN, buff=0)
    Tmp3.shift(RIGHT * CharaWid * 1.5)
    Tmp1.shift(RIGHT * CharaWid * 2)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2),FadeIn(Tmp3))
    self.remove(Nodes[4])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 4 + LEFT * (CharaWid * 2 + 3.8)))
    self.play(Tmp3.animate.shift(DOWN * HeiRat * 2 + LEFT * (CharaWid * 1 + 2.5)))
    self.remove(Tmp1)
    Nodes[4] = Tmp2

    Tmp1 = SAMNode("ba", 1, 1)  # Split
    Tmp1.next_to(Tmp3, DOWN, buff=0)
    Tmp1.shift(LEFT * CharaWid * 0.5)
    self.add(Tmp1), self.remove(Nodes[2])
    Nodes[2] = Tmp1
    TmpG = VGroup(Nodes[2], Nodes[3], Nodes[4])
    GridH[2] = GridH[2] + 0.8
    GridH[3] = GridH[3] + 0.8
    GridH[4] = GridH[4] + 0.8
    TmpA1 = Arrow(start=(UP * GridV[4] + RIGHT * GridH[3]), end=Dots[14], buff=0.05, stroke_width=3)
    TmpA2 = Arrow(end=(UP * GridV[7] + RIGHT * GridH[3]), start=Dots[10], buff=0.05, stroke_width=3)
    TmpA3 = Arrow(end=(UP * GridV[9] + RIGHT * GridH[3]), start=Dots[12], buff=0.05, stroke_width=3)
    TmpA4 = Arrow(end=(UP * GridV[5] + RIGHT * GridH[2]), start=Dots[6], buff=0.05, stroke_width=3)
    self.play(TmpG.animate.shift(RIGHT * 0.8),
              ReplacementTransform(Arrows[7], TmpA1),
              ReplacementTransform(Arrows[5], TmpA2),
              ReplacementTransform(Arrows[6], TmpA3),
              ReplacementTransform(Arrows[3], TmpA4),
              Dots[15].animate.shift(RIGHT * 0.8),
              Dots[11].animate.shift(RIGHT * 0.8),
              Dots[13].animate.shift(RIGHT * 0.8),
              Dots[7].animate.shift(RIGHT * 0.8))
    Arrows[7] = TmpA1
    Arrows[5] = TmpA2
    Arrows[6] = TmpA3
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    Nodes.append(Tmp3), GridH.append(GridH[2] - 0.8)

    GridH[5] = GridH[4] + 1.7  # add N
    Nodes[5].move_to(UP * 2.5 * HeiRat + RIGHT * GridH[5])
    self.play(FadeIn(Nodes[5]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("banan", 1, 3)
    Tmp3 = SAMNode("an", 1, 2)
    Tmp1.move_to(Nodes[5])
    Tmp1.shift(UP * HeiRat * 2.5)
    Tmp3.next_to(Tmp1, DOWN, buff=0)
    Tmp2.next_to(Tmp3, DOWN, buff=0)
    Tmp3.shift(RIGHT * CharaWid * 1.5)
    Tmp1.shift(RIGHT * CharaWid * 2.5)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2),FadeIn(Tmp3))
    self.remove(Nodes[5])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 5 + LEFT * (CharaWid * 2.5 + 6.3)))
    self.play(Tmp3.animate.shift(DOWN * HeiRat * 2 + LEFT * (CharaWid * 1 + 3.1)))
    self.remove(Tmp1)
    Nodes[5] = Tmp2

    Tmp1 = SAMNode("ban", 1, 1)  # Split
    Tmp1.next_to(Tmp3, DOWN, buff=0)
    Tmp1.shift(LEFT * CharaWid * 0.5)
    self.add(Tmp1), self.remove(Nodes[3])
    Nodes[3] = Tmp1
    TmpG = VGroup(Nodes[3], Nodes[4], Nodes[5])
    GridH[3] = GridH[3] + 1.1
    GridH[4] = GridH[4] + 1.1
    GridH[5] = GridH[5] + 1.1
    self.play(TmpG.animate.shift(RIGHT * 1.1))
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    Nodes.append(Tmp3), GridH.append(GridH[3] - 1.1)

    GridH[6] = GridH[5] + 2  # add A
    Nodes[6].move_to(UP * 3 * HeiRat + RIGHT * GridH[6])
    self.play(FadeIn(Nodes[6]))
    Tmp1 = SAMNode("", 1, 0)
    Tmp2 = SAMNode("banana", 1, 3)
    Tmp3 = SAMNode("ana", 1, 2)
    Tmp4 = SAMNode("a", 1, 1)
    Tmp1.move_to(Nodes[6])
    Tmp1.shift(UP * HeiRat * 3)
    Tmp4.next_to(Tmp1, DOWN, buff=0)
    Tmp3.next_to(Tmp4, DOWN, buff=0)
    Tmp2.next_to(Tmp3, DOWN, buff=0)
    Tmp4.shift(RIGHT * CharaWid * 2.5)
    Tmp3.shift(RIGHT * CharaWid * 1.5)
    Tmp1.shift(RIGHT * CharaWid * 3)
    self.play(FadeIn(Tmp1),FadeIn(Tmp2),FadeIn(Tmp3),FadeIn(Tmp4))
    self.remove(Nodes[6])
    self.play(Tmp1.animate.shift(DOWN * HeiRat * 6 + LEFT * (CharaWid * 3 + 9.4)))
    self.play(Tmp4.animate.shift(DOWN * HeiRat * 5 + LEFT * (CharaWid * 3 + 8.1)))
    self.play(Tmp3.animate.shift(DOWN * HeiRat * 2 + LEFT * (CharaWid * 1 + 3.7)))
    self.remove(Tmp1)
    self.remove(Tmp4)
    Nodes[6] = Tmp2

    Tmp1 = SAMNode("bana", 1, 1)  # Split
    Tmp1.next_to(Tmp3, DOWN, buff=0)
    Tmp1.shift(LEFT * CharaWid * 0.5)
    self.add(Tmp1), self.remove(Nodes[4])
    Nodes[4] = Tmp1
    TmpG = VGroup(Nodes[4], Nodes[5], Nodes[6])
    GridH[4] = GridH[4] + 1.4
    GridH[5] = GridH[5] + 1.4
    GridH[6] = GridH[6] + 1.4
    self.play(TmpG.animate.shift(RIGHT * 1.4))
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    Nodes.append(Tmp3), GridH.append(GridH[4] - 1.4)

    self.wait(1)

class Constru(Scene):
  def construct(self):
    # Node1 = SAMNode("helloworld", 1, 7)
    Node2 = SAMNode("loworld", 1, 4).shift(UP * 3 * HeiRat + RIGHT * 1.5 * CharaWid)
    Node3 = SAMNode("helloworld", 1, 3)
    # self.play(FadeIn(Node1))
    VGroup(Node2, Node3).shift(DOWN * 2)
    self.play(FadeIn(Node2))
    self.play(FadeIn(Node3))
    Node2.generate_target()
    Node2.target.shift(UP)
    Node3.generate_target()
    Node3.target.shift(DOWN)
    self.play(MoveToTarget(Node2), MoveToTarget(Node3))
    self.wait(1)

class EC2(Scene):
  def construct(self):
    Numb = []
    Numb.append(Text("0"))
    Numb.append(Text("1"))
    Numb.append(Text("2"))
    Numb.append(Text("3"))
    Numb.append(Text("4"))
    Numb.append(Text("5"))
    Numb.append(Text("6"))

    EP = []
    EP.append(Text("{0,1,2,3,4,5,6}"))
    EP.append(Text("{2,4,6}"))
    EP.append(Text("{3,5}"))
    EP.append(Text("{4,6}"))
    EP.append(Text("{1}"))
    EP.append(Text("{2}"))
    EP.append(Text("{3}"))
    EP.append(Text("{4}"))
    EP.append(Text("{5}"))
    EP.append(Text("{6}"))
    EP[0].to_corner(UL)
    for i in range(0,9):
      EP[i + 1].next_to(EP[i],DOWN)
      EP[i + 1].align_to(EP[i],LEFT)

    SubStr = []
    SubStr.append(Tex(R"\varnothing"))
    SubStr[0].next_to(EP[0], RIGHT)
    SubStr.append(TextBox("a"))
    SubStr[1].next_to(EP[1], RIGHT)
    SubStr.append(TextBox("na"))
    SubStr[2].next_to(EP[3], RIGHT)
    SubStr.append(TextBox("ana"))
    SubStr[3].next_to(SubStr[2], RIGHT)

    for i in range(0,10):
      self.play(FadeIn(EP[i]))
    S = TextBox("banana", 2).to_corner(UR)
    self.play(FadeIn(S))
    EmpTy = Line(DOWN * 0.5, UP * 0.5, color=BLUE)
    EmpTy.move_to(S)
    EmpTy.shift(LEFT * 3 * CharaWid * 2)
    Numb[0].next_to(EmpTy, DOWN)
    self.play(FadeIn(EmpTy), FadeIn(Numb[0]))

    for i in range(0,6):
      Numb[i + 1].move_to(Numb[i])
      Numb[i + 1].shift(RIGHT * CharaWid * 2)
      self.play(EmpTy.animate.shift(RIGHT * CharaWid * 2),
                ReplacementTransform(Numb[i], Numb[i + 1]))
    self.play(ReplacementTransform(Numb[6], SubStr[0]), FadeOut(EmpTy))

    StrSq = []
    StrSq.append(Rectangle(2 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[0].move_to(S)
    StrSq[0].shift(LEFT * CharaWid * 3)
    StrSq.append(StrSq[0].copy())
    StrSq[1].shift(RIGHT * CharaWid * 4)
    StrSq.append(StrSq[1].copy())
    StrSq[2].shift(RIGHT * CharaWid * 4)
    self.play(FadeIn(VGroup(StrSq[0], StrSq[1], StrSq[2])))
    self.play(ReplacementTransform(VGroup(StrSq[0], StrSq[1], StrSq[2]).copy(), SubStr[1]))

    StrSq.append(Rectangle(4 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[3].move_to(S)
    StrSq.append(StrSq[3].copy())
    StrSq[4].shift(RIGHT * CharaWid * 4)
    self.play(FadeOut(StrSq[0]))
    self.play(ReplacementTransform(StrSq[1], StrSq[3]),
              ReplacementTransform(StrSq[2], StrSq[4]))
    self.play(TransformFromCopy(VGroup(StrSq[3], StrSq[4]), SubStr[2]))

    StrSq.append(Rectangle(6 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[5].move_to(S)
    StrSq[5].shift(LEFT * CharaWid)
    StrSq.append(StrSq[5].copy())
    StrSq[6].shift(RIGHT * CharaWid * 4)
    self.play(ReplacementTransform(StrSq[3], StrSq[5]),
              ReplacementTransform(StrSq[4], StrSq[6]))
    self.play(TransformFromCopy(VGroup(StrSq[5], StrSq[6]), SubStr[3]))

    self.wait()

class EC(Scene):
  def construct(self):
    EndPosT = Text("EndPos:").to_corner(UL)
    self.add(EndPosT)
    S = TextBox("banana", 3).move_to(UP * 2)
    self.play(Write(S))

    NA = TextBox("na", 3).move_to(UP * 2)
    NAE = Text("na:{}").next_to(EndPosT, DOWN)
    self.play(FadeIn(NAE))
    self.add(NA)
    self.play(NA.animate.shift(DOWN * 2))
    Lable = []
    Lable.append(Text("4").next_to(NA, DOWN))
    self.play(Write(Lable[0]))
    NAEN = Text("na:{4}").next_to(EndPosT, DOWN)
    self.play(ReplacementTransform(VGroup(NAE, Lable[0]), NAEN))
    self.play(NA.animate.shift(RIGHT * 3 * CharaWid * 2))
    Lable.append(Text("6").next_to(NA, DOWN))
    self.play(Write(Lable[1]))
    NAE6 = Text("na:{4,6}").next_to(EndPosT, DOWN)
    self.play(ReplacementTransform(VGroup(NAEN, Lable[1]), NAE6))
    self.play(FadeOut(NA))

    NA = TextBox("ana", 3).move_to(UP * 2 + LEFT * CharaWid * 3 * 0.5)
    ANAE = Text("ana:{}").next_to(NAE6, DOWN)
    self.play(FadeIn(ANAE))
    self.add(NA)
    self.play(NA.animate.shift(DOWN * 2))
    Lable[0] = Text("4").next_to(NA, DOWN)
    self.play(Write(Lable[0]))
    ANAEN = Text("ana:{4}").next_to(NAE6, DOWN)
    self.play(ReplacementTransform(VGroup(ANAE, Lable[0]), ANAEN))
    self.play(NA.animate.shift(RIGHT * 3 * CharaWid * 2))
    Lable[1] = Text("6").next_to(NA, DOWN)
    self.play(Write(Lable[1]))
    ANAE6 = Text("ana:{4,6}").next_to(NAE6, DOWN)
    self.play(ReplacementTransform(VGroup(ANAEN, Lable[1]), ANAE6))
    self.play(FadeOut(NA))

    self.wait(1)
# manimgl SAM.py EC -o -c "BLACK"
# manimgl SAM.py EC2 -o -c "BLACK"
# manimgl SAM.py Constru -o -c "BLACK"
# manimgl SAM.py BANANA -o -c "BLACK"