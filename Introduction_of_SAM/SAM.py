from manimlib import *
import numpy 
CharaWid = 0.266
HeiRat = 0.589
RuntimeLog = open("Log.txt", "w")

def MyText(Txt: str, BoxScale: float=1) -> Text:
  return Text(text=Txt,font_size=(int)(24*BoxScale))

def CharaBox(CharinBox: str, BoxScale: float=1) -> VGroup:
  ChrtoText = MyText(CharinBox).scale(BoxScale)
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
  SufT.append(MyText(Strings,BoxScale))
  MyNode += SufT[0]
  for i in range(0,Hei - 1):
    Strings = Strings[1:]
    SufT.append(MyText(Strings,BoxScale))
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

def Trape(Len:int, BoxScale: float=1, Hei: int=1) -> VGroup:
  # RuntimeLog.write("\nLen:")
  # RuntimeLog.write(str(Len))
  if(Len == 0):
    # RuntimeLog.write("\nHere")
    return Polygon([BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0], 
                   [BoxScale * CharaWid * 0.5, 0.5 * HeiRat * BoxScale, 0],
                   [-BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0])

  LeUp = [(2 * Hei - 2 - Len) * BoxScale * CharaWid * 0.5, (Hei - 0.5) * HeiRat * BoxScale, 0]
  RiUp = [+Len * BoxScale * CharaWid * 0.5, (Hei - 0.5) * HeiRat * BoxScale, 0]
  LeDown = [LeUp[0] - Hei * CharaWid, -0.5 * HeiRat * BoxScale, 0]
  RiDown = [+Len * BoxScale * CharaWid * 0.5, -0.5 * HeiRat * BoxScale, 0]
  return Polygon(LeDown, RiDown, RiUp, LeUp)

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
    GridV.append(1.4)
    GridV.append(-1.1)
    GridV.append(1.7)
    GridV.append(-1.3)
    GridV.append(2)
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
    GridH.append(GridH[2])
    GridH[2] = GridH[2] + 0.8
    GridH[3] = GridH[3] + 0.8
    GridH[4] = GridH[4] + 0.8
    TmpA1 = Arrow(start=(UP * GridV[4] + RIGHT * (GridH[3] - 0.03)), end=Dots[14], buff=0.05, stroke_width=3)
    TmpA2 = Arrow(end=(UP * GridV[7] + RIGHT * (GridH[3] - 0.03)), start=Dots[10], buff=0.05, stroke_width=3)
    TmpA3 = Arrow(end=(UP * GridV[9] + RIGHT * (GridH[3] - 0.03)), start=Dots[12], buff=0.05, stroke_width=3)
    TmpA4 = Arrow(end=(UP * GridV[5] + RIGHT * (GridH[2] - 0.03)), start=Dots[6], buff=0.05, stroke_width=3)
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
    Arrows[3] = TmpA4
    Dots.append(Dot(point=[GridH[2], GridV[11], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[3], GridV[11], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[16], end=Dots[17], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[7], GridV[0], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[2], GridV[0], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[19], end=Dots[18], buff=0.05, stroke_width=3))
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    self.play(FadeIn(Arrows[8]),FadeIn(Arrows[9]), FadeIn(Dots[16]), FadeIn(Dots[17]), FadeIn(Dots[18]), FadeIn(Dots[19]))
    Nodes.append(Tmp3)
    Dots.append(Dot(point=[GridH[3], GridV[1], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[4], GridV[1], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[20], end=Dots[21], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[7], GridV[8], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[4], GridV[8], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[23], end=Dots[22], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[10]), FadeIn(Arrows[11]), FadeIn(Dots[20]), FadeIn(Dots[21]), FadeIn(Dots[22]), FadeIn(Dots[23]))

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
    GridH.append(GridH[3])
    GridH[3] = GridH[3] + 1.1
    GridH[4] = GridH[4] + 1.1
    GridH[5] = GridH[5] + 1.1
    TmpA1 = Arrow(start=(UP * GridV[8] + RIGHT * (GridH[4] - 0.03)), end=Dots[22], buff=0.05, stroke_width=3) 
    self.play(TmpG.animate.shift(RIGHT * 1.1),
              ReplacementTransform(Arrows[11], TmpA1),
              VGroup(Arrows[10], Dots[20], Dots[21]).animate.shift(RIGHT * 1.1),
              Dots[23].animate.shift(RIGHT * 1.1))
    Arrows[11] = TmpA1
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    Dots.append(Dot(point=[GridH[8], GridV[6], 0], radius=0.03)) # Useless
    Dots.append(Dot(point=[GridH[3], GridV[4], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[25], end=Dots[15], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[2], GridV[1], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[26], end=Dots[20], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[8], GridV[3], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[4], GridV[3], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[27], end=Dots[28], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[12]), FadeIn(Arrows[13]), FadeIn(Arrows[14]),
              FadeIn(Dots[25]), FadeIn(Dots[26]), FadeIn(Dots[27]), FadeIn(Dots[28]))
    Nodes.append(Tmp3)
    Dots.append(Dot(point=[GridH[8], GridV[10], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[5], GridV[10], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[30], end=Dots[29], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[5], GridV[1], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[21], end=Dots[31], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[15]), FadeIn(Arrows[16]), FadeIn(Dots[29]), FadeIn(Dots[30]), FadeIn(Dots[31]))

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
    GridH.append(GridH[4])
    GridH[4] = GridH[4] + 1.4
    GridH[5] = GridH[5] + 1.4
    GridH[6] = GridH[6] + 1.4
    TmpA1 = Arrow(end=(UP * GridV[1] + RIGHT * (GridH[4] - 0.03)), start=Dots[20], buff=0.05, stroke_width=3)
    TmpA2 = Arrow(start=(UP * GridV[10] + RIGHT * (GridH[5] - 0.03)), end=Dots[29], buff=0.05, stroke_width=3)
    self.play(TmpG.animate.shift(RIGHT * 1.4),
              ReplacementTransform(Arrows[10], TmpA1),
              ReplacementTransform(Arrows[15], TmpA2),
              VGroup(Dots[21], Dots[30], Dots[31], Arrows[16]).animate.shift(RIGHT * 1.4))
    Arrows[10] = TmpA1
    Arrows[15] = TmpA2
    self.play(Tmp3.animate.shift(DOWN * HeiRat + LEFT * CharaWid))
    Nodes.append(Tmp3)
    Dots.append(Dot(point=[GridH[5], GridV[3], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[28], end=Dots[32], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[9], GridV[4], 0], radius=0.03))
    Dots.append(Dot(point=[GridH[4], GridV[4], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[34], end=Dots[33], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[17]), FadeIn(Arrows[18]), FadeIn(Dots[32]), FadeIn(Dots[33]), FadeIn(Dots[34]))
    Dots[24] = Dot(point=[GridH[6], GridV[1], 0], radius=0.03)
    Arrows.append(Arrow(start=Dots[31], end=Dots[24], buff=0.05, stroke_width=3))
    Dots.append(Dot(point=[GridH[6], GridV[8], 0], radius=0.03))
    Arrows.append(Arrow(start=Dots[35], end=Dots[23], buff=0.05, stroke_width=3))
    self.play(FadeIn(Arrows[19]), FadeIn(Arrows[20]), FadeIn(Dots[24]), FadeIn(Dots[35]))

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
    Numb.append(MyText("0"))
    Numb.append(MyText("1"))
    Numb.append(MyText("2"))
    Numb.append(MyText("3"))
    Numb.append(MyText("4"))
    Numb.append(MyText("5"))
    Numb.append(MyText("6"))

    EP = []
    EP.append(MyText("{0,1,2,3,4,5,6}"))
    EP.append(MyText("{2,4,6}"))
    EP.append(MyText("{3,5}"))
    EP.append(MyText("{4,6}"))
    EP.append(MyText("{1}"))
    EP.append(MyText("{2}"))
    EP.append(MyText("{3}"))
    EP.append(MyText("{4}"))
    EP.append(MyText("{5}"))
    EP.append(MyText("{6}"))
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
    SubStr.append(TextBox("bana"))
    SubStr[4].next_to(EP[7], RIGHT)
    SubStr.append(TextBox("nana"))
    SubStr[5].next_to(EP[9], RIGHT)
    SubStr.append(TextBox("anana"))
    SubStr[6].next_to(SubStr[5], RIGHT)
    SubStr.append(TextBox("banana"))
    SubStr[7].next_to(SubStr[6], RIGHT)
    SubStr.append(TextBox("ba"))
    SubStr[8].next_to(EP[5], RIGHT)
    SubStr.append(TextBox("n"))
    SubStr[9].next_to(EP[2], RIGHT)
    SubStr.append(TextBox("an"))
    SubStr[10].next_to(SubStr[9], RIGHT)
    SubStr.append(TextBox("ban"))
    SubStr[11].next_to(EP[6], RIGHT)
    SubStr.append(TextBox("nan"))
    SubStr[12].next_to(EP[8], RIGHT)
    SubStr.append(TextBox("anan"))
    SubStr[13].next_to(SubStr[12], RIGHT)
    SubStr.append(TextBox("banan"))
    SubStr[14].next_to(SubStr[13], RIGHT)
    SubStr.append(TextBox("b"))
    SubStr[15].next_to(EP[4], RIGHT)

    TmpG = VGroup()
    for i in range(0,10):
      TmpG.add(EP[i])
    self.play(FadeIn(TmpG))

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
    self.play(FadeIn(StrSq[0]), FadeIn(StrSq[1]), FadeIn(StrSq[2]))
    Tmp3 = StrSq[0].copy()
    Tmp4 = StrSq[1].copy()
    Tmp5 = StrSq[2].copy()
    self.play(ReplacementTransform(VGroup(StrSq[0], StrSq[1], StrSq[2]), SubStr[1]))
    StrSq[0] = Tmp3
    StrSq[1] = Tmp4
    StrSq[2] = Tmp5

    StrSq.append(Rectangle(4 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[3].move_to(S)
    StrSq.append(StrSq[3].copy())
    StrSq[4].shift(RIGHT * CharaWid * 4)
    self.play(FadeIn(StrSq[1]), FadeIn(StrSq[2]))
    self.play(ReplacementTransform(StrSq[1], StrSq[3]),
              ReplacementTransform(StrSq[2], StrSq[4]))
    Tmp1 = StrSq[3].copy()
    Tmp2 = StrSq[4].copy()
    self.play(ReplacementTransform(VGroup(StrSq[3], StrSq[4]), SubStr[2]))
    StrSq[3] = Tmp1
    StrSq[4] = Tmp2
    self.play(FadeIn(StrSq[3]), FadeIn(StrSq[4]))

    StrSq.append(Rectangle(6 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[5].move_to(S)
    StrSq[5].shift(LEFT * CharaWid)
    StrSq.append(StrSq[5].copy())
    StrSq[6].shift(RIGHT * CharaWid * 4)
    self.play(ReplacementTransform(StrSq[3], StrSq[5]),
              ReplacementTransform(StrSq[4], StrSq[6]))
    Tmp1 = StrSq[5].copy()
    Tmp2 = StrSq[6].copy()
    self.play(ReplacementTransform(VGroup(StrSq[5], StrSq[6]), SubStr[3]))
    StrSq[5] = Tmp1
    StrSq[6] = Tmp2

    StrSq.append(Rectangle(8 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[7].move_to(S)
    StrSq[7].shift(LEFT * CharaWid * 2)
    self.play(FadeIn(StrSq[5]))
    self.play(ReplacementTransform(StrSq[5], StrSq[7]))
    self.play(ReplacementTransform(StrSq[7], SubStr[4]))

    StrSq.append(Rectangle(8 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[8].move_to(S)
    StrSq[8].shift(RIGHT * CharaWid * 2)
    self.play(FadeIn(StrSq[6]))
    self.play(ReplacementTransform(StrSq[6], StrSq[8]))
    Tmp1 = StrSq[8].copy()
    self.play(ReplacementTransform(StrSq[8], SubStr[5]))
    StrSq[8] = Tmp1

    StrSq.append(Rectangle(10 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[9].move_to(S)
    StrSq[9].shift(RIGHT * CharaWid)
    self.play(FadeIn(StrSq[8]))
    self.play(ReplacementTransform(StrSq[8], StrSq[9]))
    Tmp1 = StrSq[9].copy()
    self.play(ReplacementTransform(StrSq[9], SubStr[6]))
    StrSq[9] = Tmp1

    StrSq.append(Rectangle(12 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[10].move_to(S)
    self.play(FadeIn(StrSq[9]))
    self.play(ReplacementTransform(StrSq[9], StrSq[10]))
    Tmp1 = StrSq[10].copy()
    self.play(ReplacementTransform(StrSq[10], SubStr[7]))
    StrSq[10] = Tmp1

    StrSq.append(Rectangle(4 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[11].move_to(S)
    StrSq[11].shift(LEFT * CharaWid * 4)
    self.play(FadeIn(StrSq[0]))
    self.play(ReplacementTransform(StrSq[0], StrSq[11]))
    self.play(ReplacementTransform(StrSq[11], SubStr[8]))

    StrSq.append(Rectangle(2 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[12].move_to(S)
    StrSq[12].shift(LEFT * CharaWid)
    StrSq.append(StrSq[12].copy())
    StrSq[13].shift(RIGHT * CharaWid * 4)
    self.play(FadeIn(StrSq[12]), FadeIn(StrSq[13]))
    Tmp1 = StrSq[12].copy()
    Tmp2 = StrSq[13].copy()
    self.play(ReplacementTransform(VGroup(StrSq[12], StrSq[13]), SubStr[9]))
    StrSq[12] = Tmp1
    StrSq[13] = Tmp2

    StrSq.append(Rectangle(4 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[14].move_to(S)
    StrSq[14].shift(LEFT * CharaWid * 2)
    StrSq.append(StrSq[14].copy())
    StrSq[15].shift(RIGHT * CharaWid * 4)
    self.play(FadeIn(StrSq[12]), FadeIn(StrSq[13]))
    self.play(ReplacementTransform(StrSq[12], StrSq[14]),ReplacementTransform(StrSq[13], StrSq[15]))
    Tmp1 = StrSq[14].copy()
    Tmp2 = StrSq[15].copy()
    self.play(ReplacementTransform(VGroup(StrSq[14], StrSq[15]), SubStr[10]))
    StrSq[14] = Tmp1
    StrSq[15] = Tmp2

    StrSq.append(Rectangle(6 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[16].move_to(S)
    StrSq[16].shift(LEFT * CharaWid * 3)
    self.play(FadeIn(StrSq[14]))
    self.play(ReplacementTransform(StrSq[14], StrSq[16]))
    self.play(ReplacementTransform(StrSq[16], SubStr[11]))

    StrSq.append(Rectangle(6 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[17].move_to(S)
    StrSq[17].shift(RIGHT * CharaWid)
    self.play(FadeIn(StrSq[15]))
    self.play(ReplacementTransform(StrSq[15], StrSq[17]))
    Tmp1 = StrSq[17].copy()
    self.play(ReplacementTransform(StrSq[17], SubStr[12]))
    StrSq[17] = Tmp1

    StrSq.append(Rectangle(8 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[18].move_to(S)
    self.play(FadeIn(StrSq[17]))
    self.play(ReplacementTransform(StrSq[17], StrSq[18]))
    Tmp1 = StrSq[18].copy()
    self.play(ReplacementTransform(StrSq[18], SubStr[13]))
    StrSq[18] = Tmp1

    StrSq.append(Rectangle(10 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[19].move_to(S)
    StrSq[19].shift(LEFT * CharaWid)
    self.play(FadeIn(StrSq[18]))
    self.play(ReplacementTransform(StrSq[18], StrSq[19]))
    self.play(ReplacementTransform(StrSq[19], SubStr[14]))

    StrSq.append(Rectangle(2 * CharaWid, 1, stroke_opacity=0, fill_opacity=0.3, fill_color=BLUE))
    StrSq[20].move_to(S)
    StrSq[20].shift(LEFT * CharaWid * 5)
    self.play(FadeIn(StrSq[20]))
    self.play(ReplacementTransform(StrSq[20], SubStr[15]))

    self.wait()

class EC3(Scene):
  def construct(self):
    Tit = MyText("{5}")
    Str1 = MyText("banan")
    Str2 = MyText("anan")
    Str3 = MyText("nan")
    VGroup(Tit, Str3, Str2, Str1).arrange(DOWN)
    Str2.align_to(Str1,RIGHT)
    Str3.align_to(Str2,RIGHT)
    self.play(FadeIn(Tit))
    self.play(FadeIn(Str1))
    self.play(TransformFromCopy(Str1, Str2))
    self.play(TransformFromCopy(Str2, Str3))
    self.play(FadeOut(VGroup(Tit, Str3, Str2, Str1)))

class Intro1(Scene):
  def construct(self):
    Str1 = MyText("SAM", 2)
    Str2 = MyText("String", 2)
    A1 = Arrow(LEFT, RIGHT)
    A2 = Arrow(RIGHT, LEFT)
    TmpG1 = VGroup(A1, A2).arrange(DOWN)
    TmpG2 = VGroup(Str1, TmpG1, Str2).arrange(RIGHT)
    self.play(Write(TmpG2))
    self.wait(1)

class Intro2(Scene):
  def construct(self):
    Str1 = Tex("S","A","M", font_size=200)
    Str2 = Tex("S","uffix~","A","uto","M","aton", font_size=100)
    self.play(Write(Str1))
    self.play(TransformMatchingTex(Str1, Str2, ))
    self.wait(1)

class ShowNode(Scene):
  def construct(self):
    Tit = MyText("{5}").shift(LEFT * 2.5)
    Tmp1 = SAMNode("banan", 1, 3).shift(DOWN + LEFT)
    self.play(Write(Tmp1), Write(Tit))
    Ar1 = Arrow(start=LEFT, end=RIGHT, stroke_width=3, color="#8080FF").shift([1.5, 0.5,0])
    Tit1 = MyText("Link").next_to(Ar1, DOWN)
    Ar2 = Arrow(start=LEFT, end=RIGHT, stroke_width=3, color="#FF8080").shift([1.5,-0.5,0])
    Tit2 = MyText("Transition").next_to(Ar2, DOWN)
    self.play(Write(Ar1), Write(Ar2), Write(Tit1), Write(Tit2))
    self.wait(1)

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

class LinkTree(Scene):
  def construct(self):
    Nodes = []
    Dots = []
    EP = []
    Edges = []
    Nodes.append(SAMNode("", 1, 0).move_to([0,3.5,0]))
    Nodes.append(SAMNode("b", 1, 1).move_to([0 - 0.5 * CharaWid,2.3,0]))
    Nodes.append(SAMNode("a", 1, 1).move_to([-1,2.3,0]))
    Nodes.append(SAMNode("ba", 1, 1).move_to([-4 + 1 * CharaWid,0.5 + 0.5 * HeiRat,0]))
    Nodes.append(SAMNode("an", 1, 2).move_to([2,2.3 - 0.5 * HeiRat,0]))
    Nodes.append(SAMNode("ban", 1, 1).move_to([0.5 - 0.5 * CharaWid,0.5,0]))
    Nodes.append(SAMNode("ana", 1, 2).move_to([-1 - CharaWid,0.5,0]))
    Nodes.append(SAMNode("bana", 1, 1).move_to([-4,-2 + HeiRat,0]))
    Nodes.append(SAMNode("banan", 1, 3).move_to([2 - 1.5 * CharaWid,0.5 - HeiRat,0]))
    Nodes.append(SAMNode("banana", 1, 3).move_to([-1 - 2.5 * CharaWid,-2,0]))
    EP.append(MyText("{0,1,2,3,4,5,6}"))
    EP[0].next_to(Nodes[0], RIGHT)
    EP.append(MyText("{1}"))
    EP[1].next_to(Nodes[1], RIGHT)
    EP.append(MyText("{2,4,6}"))
    EP[2].next_to(Nodes[2], LEFT)
    EP.append(MyText("{2}"))
    EP[3].next_to(Nodes[3], LEFT)
    EP.append(MyText("{3,5}"))
    EP[4].next_to(Nodes[4], RIGHT)
    EP.append(MyText("{3}"))
    EP[5].next_to(Nodes[5], DOWN)
    EP.append(MyText("{4,6}"))
    EP[6].next_to(Nodes[6], LEFT)
    EP[6].shift(RIGHT * 0.4)
    EP.append(MyText("{4}"))
    EP[7].next_to(Nodes[7], LEFT)
    EP.append(MyText("{5}"))
    EP[8].next_to(Nodes[8], RIGHT)
    EP.append(MyText("{6}"))
    EP[9].next_to(Nodes[9], RIGHT)
    for i in range(0,10):
      self.play(FadeIn(Nodes[i]), FadeIn(EP[i]))
    for i in range(0,9):
      Dots.append(Dot(radius=0.03))
      Dots[i].next_to(Nodes[i + 1], UP, buff=0.05)
    for i in range(0,4):
      Dots.append(Dot(radius=0.03))
    Dots[9].next_to(Nodes[0], DOWN, buff=0.05)
    Dots[10].next_to(Nodes[2], DOWN, buff=0.05)
    Dots[11].next_to(Nodes[4], DOWN, buff=0.05)
    Dots[12].next_to(Nodes[6], DOWN, buff=0.05)
    GDots = VGroup()
    for i in range(0,13):
      GDots.add(Dots[i])
    Edges.append(Arrow(start=Dots[0], end=Dots[9], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[1], end=Dots[9], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[3], end=Dots[9], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[2], end=Dots[10], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[5], end=Dots[10], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[4], end=Dots[11], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[7], end=Dots[11], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[6], end=Dots[12], buff = 0.05, stroke_width=3, color="#8080FF"))
    Edges.append(Arrow(start=Dots[8], end=Dots[12], buff = 0.05, stroke_width=3, color="#8080FF"))
    for i in range(0,9):
      GDots.add(Edges[i])
    self.play(FadeIn(GDots))
    TmpE1 = EP[6].copy()
    TmpE1.set_color(RED)
    self.play(TransformFromCopy(EP[9], TmpE1))
    TmpE2 = EP[2].copy()
    TmpE2.set_color(RED)
    self.play(TransformFromCopy(TmpE1, TmpE2))

class DAG(Scene):
  def construct(self):
    Nodes = []
    Dots = []
    EP = []
    Edges = []
    GDots = VGroup()
    Nodes.append(SAMNode("", 1, 0).move_to([-6,0,0]))
    Nodes.append(SAMNode("b", 1, 1).move_to([-5,-1,0]))
    Nodes.append(SAMNode("a", 1, 1).move_to([-5,1,0]))
    Nodes.append(SAMNode("ba", 1, 1).move_to([-3.7,-1,0]))
    Nodes.append(SAMNode("an", 1, 2).move_to([-2,1,0]))
    Nodes.append(SAMNode("ban", 1, 1).move_to([-2 - 0.5 * CharaWid,-1,0]))
    Nodes.append(SAMNode("ana", 1, 2).move_to([0,1,0]))
    Nodes.append(SAMNode("bana", 1, 1).move_to([0 - 0.5 * CharaWid,-1,0]))
    Nodes.append(SAMNode("banan", 1, 3).move_to([2,-1 + HeiRat,0]))
    Nodes.append(SAMNode("banana", 1, 3).move_to([4.5,-1 + HeiRat,0]))
    for i in range(0,9):
      Dots.append(Dot(radius=0.03))
      Dots[i].next_to(Nodes[i], RIGHT, buff=0.05)
    for i in range(1,10):
      Dots.append(Dot(radius=0.03))
      Dots[i + 8].next_to(Nodes[i], LEFT, buff=0.05)
    for i in range(0,18):
      GDots.add(Dots[i])
    Dots[9].shift(RIGHT * 0.1)
    Dots[10].shift(RIGHT * 0.1)
    Dots[11].shift(RIGHT * 0.1)
    Dots[13].shift(RIGHT * 0.1)
    Dots[15].shift(RIGHT * 0.1)
    Dots[12].shift(RIGHT * 0.2)
    Dots[14].shift(RIGHT * 0.2)
    Dots[16].shift(RIGHT * 0.3)
    Dots[17].shift(RIGHT * 0.3)
    Edges.append(Arrow(start=Dots[0], end=Dots[9], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[0], end=Dots[10], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[0], end=Dots[12], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[1], end=Dots[11], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[2], end=Dots[12], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[3], end=Dots[13], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[4], end=Dots[14], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[5], end=Dots[15], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[6], end=Dots[16], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[7], end=Dots[16], buff = 0.05, stroke_width=3, color="#FF8080"))
    Edges.append(Arrow(start=Dots[8], end=Dots[17], buff = 0.05, stroke_width=3, color="#FF8080"))
    for i in range(0,10):
      GDots.add(Nodes[i])
    self.play(FadeIn(GDots))
    EP.append(MyText("b", 0.5))
    EP.append(MyText("a", 0.5))
    EP.append(MyText("a", 0.5))
    EP.append(MyText("n", 0.5))
    EP.append(MyText("n", 0.5))
    EP.append(MyText("n", 0.5))
    EP.append(MyText("a", 0.5))
    EP.append(MyText("a", 0.5))
    EP.append(MyText("n", 0.5))
    EP.append(MyText("n", 0.5))
    EP.append(MyText("a", 0.5))
    for i in range(0,11):
      EP[i].move_to(Edges[i])
      EP[i].shift(UP * 0.3)
    for i in range(0,11):
      self.play(FadeIn(VGroup(Edges[i], EP[i])))

class Transition(Scene):
  def construct(self):
    Node1 = SAMNode("banan", 1, 3).move_to([2,0,0])
    Node2 = SAMNode("bana", 1, 1).move_to([-2,-1,0])
    Node3 = SAMNode("ana", 1, 2).move_to([-2,1,0])
    Dot1 = Dot(radius=0.03).next_to(Node1, LEFT, buff=0.05)
    Dot1.shift(RIGHT * 0.3)
    Dot2 = Dot(radius=0.03).next_to(Node2, RIGHT, buff=0.05)
    Dot3 = Dot(radius=0.03).next_to(Node3, RIGHT, buff=0.05)
    Edge1 = Arrow(start=Dot2, end=Dot1, buff = 0.05, stroke_width=3, color="#FF8080")
    Edge2 = Arrow(start=Dot3, end=Dot1, buff = 0.05, stroke_width=3, color="#FF8080")
    HLi1 = MyText("n").move_to(Node1)
    HLi2 = MyText("n").move_to(Node1)
    HLi3 = MyText("n").move_to(Node1)
    HLi1.set_color(RED)
    HLi2.set_color(RED)
    HLi3.set_color(RED)
    HLi1.shift(RIGHT * 2.5 * CharaWid)
    HLi2.shift(UP * HeiRat + RIGHT * 2.5 * CharaWid)
    HLi3.shift(DOWN * (HeiRat + 0.05) + RIGHT * 2.5 * CharaWid)
    EP1 = MyText("n", 0.5).move_to(Edge1)
    EP2 = MyText("n", 0.5).move_to(Edge2)
    EP1.shift(UP * 0.2)
    EP2.shift(UP * 0.2)
    self.play(FadeIn(VGroup(Node2, Node3)))
    self.play(TransformFromCopy(VGroup(Node2, Node3), Node1))
    self.play(FadeIn(VGroup(HLi1, HLi2, HLi3)))
    self.play(FadeIn(VGroup(Edge1, Edge2, Dot2, Dot3, Dot1, EP1, EP2)))
    self.wait(1)

class ComplAdd(Scene):
  def construct(self):
    T1 = Tex("O(n)").scale(3)
    T1.move_to([-2, 0, 0])
    T2 = Tex("Time").move_to([1, 1, 0])
    T3 = Tex("Space").move_to([1, -1, 0])
    self.play(Write(T1))
    self.play(Write(T2))
    self.play(Write(T3))
    self.wait(1)
    self.play(FadeOut(VGroup(T1, T2, T3)))

    MyTS = "banana"
    MyT = []
    Tri = []
    GrLi = []
    GrT = VGroup()
    for i in range(0, 6):
      MyT.append(MyText(MyTS[i]).set_color(RED))
      Tmpi = []
      Gri = VGroup()
      for j in range (1, i + 1):
        Tmpj = []
        Grj = VGroup()
        for k in range (j, i + 1):
          Tmpj.append(MyText(MyTS[k]))
          Grj.add(Tmpj[k - j])
        Grj.arrange(RIGHT)
        Gri.add(Grj)
        Tmpj[i - j].set_color(RED)
        Tmpi.append(Grj)
      Tri.append(Tmpi)
      Gri.arrange(UP)
      GrLi.append(Gri)
      Gri.shift(UP * (i + 1) * 0.24)

    for i in range(0, 6):
      GrT.add(MyT[i])
    GrT.arrange(RIGHT)
    GrT.move_to([0, 0, 0])

    for i in range(0, 6):
      for j in range(0, i):
        Tri[i][j].align_to(MyT[i], RIGHT)

    for i in range(0, 6):
      self.play(FadeIn(MyT[i]))
      self.play(FadeIn(GrLi[i]))
      self.wait(1)
      self.play(FadeOut(GrLi[i]))
      self.play(FadeToColor(MyT[i],WHITE))
    self.wait(1)

class Trian(Scene):
  def construct(self):
    T1 = SAMNode("banana", 1, 7).move_to([-2, 0, 0])
    T2 = SAMNode("", 1, 0)
    T3 = SAMNode("a", 1, 1)
    T4 = SAMNode("ana", 1, 2)
    T5 = SAMNode("banana", 1, 3)

    VG = VGroup(T2, T3, T4, T5).arrange(DOWN, buff=0)
    VG.align_to(T1, DOWN)
    T2.align_to(T1, RIGHT)
    T3.align_to(T1, RIGHT)
    T4.align_to(T1, RIGHT)
    T5.align_to(T1, RIGHT)

    self.play(FadeIn(T1))
    self.play(FadeIn(VGroup(T2, T3, T4, T5)))
    self.remove(T1)
    self.play(T2.animate.shift(UP), T3.animate.shift(UP * 0.5), T5.animate.shift(DOWN * 0.5))
    self.wait(1)
    
    EC1 = MyText("{0,1,2,3,4,5,6}").next_to(T2,RIGHT)
    EC2 = MyText("{2,4,6}").next_to(T3,RIGHT)
    EC3 = MyText("{4,6}").next_to(T4,RIGHT)
    EC4 = MyText("{6}").next_to(T5,RIGHT)
    self.play(FadeIn(VGroup(EC1, EC2, EC3, EC4)))
    self.wait(1)

class Jump (Scene):
  def construct(self):
    Whole = VGroup(MyText("PreFix"), Trape(7, 1, 3))
    New = VGroup(MyText("PreFix").shift(LEFT * 0.2), MyText("C").set_color(YELLOW).shift(RIGHT * 0.9), Trape(8, 1, 3))
    N = VGroup(Rectangle(height=3*HeiRat, width=CharaWid, stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(New, RIGHT).align_to(New, DOWN), New)
    New_New = VGroup(MyText("PreFix").shift(LEFT * 0.2), MyText("C").set_color(YELLOW).shift(RIGHT * 0.9), Trape(8, 1, 4))
    New_N = VGroup(Rectangle(height=4*HeiRat, width=CharaWid, 
    stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(New, RIGHT).align_to(New, DOWN), New_New)
    NewText = MyText("N", 2).move_to(New_N).set_color(YELLOW).shift(RIGHT * 0.5 + DOWN * 0.1)
    New_N.add(NewText)
    Whole.shift([-1.5, -3, 0])
    N.shift([1.5, -3, 0])

    Fa = VGroup(Trape(4, 1, 1), MyText("...", 1.5)).next_to(Whole, UP, buff=1).align_to(Whole, RIGHT)
    Y = VGroup(Trape(3, 1, 2)).next_to(Fa, UP, buff=1).align_to(Whole, RIGHT)
    New_N.align_to(N, DOWN).align_to(N, RIGHT)
    T_Base = Trape(6, 1, 4)
    Ts_Base = Trape(4, 1, 2)
    T = VGroup(T_Base, Rectangle(height=4*HeiRat, width=CharaWid, 
    stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(T_Base, RIGHT).align_to(T_Base, DOWN)).next_to(New_N, UP, buff = 1).align_to(New_N, RIGHT)
    Ts = VGroup(Ts_Base, Rectangle(height=2*HeiRat, width=CharaWid, 
    stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(Ts_Base, RIGHT).align_to(Ts_Base, DOWN)).next_to(New_N, UP, buff = 1).align_to(New_N, RIGHT)

    Uncle = Trape(5, 1, 2).next_to(Fa, LEFT, buff=0.5).shift(DOWN * HeiRat * 0.5)
    T1_Base = Trape(4, 1, 2).align_to(T, UP).align_to(T, RIGHT)
    T2_Base = Trape(6, 1, 2).align_to(T, DOWN).align_to(T, RIGHT)
    T1 = VGroup(T1_Base, MyText("T1", 1.5).set_color(YELLOW).move_to(T1_Base).shift(DOWN * 0.2), Rectangle(height=2*HeiRat, width=CharaWid, 
    stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(T1_Base, RIGHT).align_to(T1_Base, DOWN))
    T2 = VGroup(T2_Base, MyText("T2", 1.5).set_color(YELLOW).move_to(T2_Base).shift(DOWN * 0.2), Rectangle(height=2*HeiRat, width=CharaWid, 
    stroke_opacity = 0).set_fill(YELLOW, 0.3).align_to(T2_Base, RIGHT).align_to(T2_Base, DOWN))

    Dots = []
    for i in range(0, 20) :
      Dots.append(Dot(radius=0.03))
    Dots[3].next_to(Y, DOWN, buff=0.05)
    Dots[0].next_to(Whole, UP, buff=0.05).align_to(Dots[3], RIGHT)
    Dots[1].next_to(Fa, UP, buff=0.05).align_to(Dots[3], RIGHT)
    Dots[2].next_to(Fa, DOWN, buff=0.05).align_to(Dots[3], RIGHT)
    Dots[4].next_to(New_N, LEFT).shift(RIGHT * 0.7)
    Dots[5].next_to(Whole, RIGHT, buff=0.05)
    Dots[6].next_to(Fa, RIGHT, buff=0.05)
    Dots[7].next_to(Y, RIGHT, buff=0.05)
    Dots[8].next_to(Ts, LEFT).shift(RIGHT * 0.4)
    Dots[9].next_to(Uncle, RIGHT, buff=0.05).shift(UP * 0.5)
    Dots[10].next_to(Uncle, UP, buff=0.05)
    Dots[11].next_to(Fa, RIGHT, buff=0.05)
    Dots[12].next_to(Fa, RIGHT, buff=0.05)
    Dots[13].next_to(Whole, DOWN, buff=0.2).align_to(Whole, LEFT)
    Dots[14].next_to(Whole, DOWN, buff=0.2).align_to(Whole, RIGHT)
    Dots[15].next_to(Ts, DOWN, buff=0.05)
    Dots[16].next_to(New_N, UP, buff=0.05).align_to(Dots[15], RIGHT)


    Link1 = VGroup(Dots[0], Dots[2], Arrow(start=Dots[0], end=Dots[2], buff=0.05, stroke_width=3, color="#8080FF"))
    Link2 = VGroup(Dots[1], Dots[3], Arrow(start=Dots[1], end=Dots[3], buff=0.05, stroke_width=3, color="#8080FF"))
    Link3 = VGroup(Dots[10], Arrow(start=Dots[10], end=Dots[3], buff=0.05, stroke_width=3, color="#8080FF"))
    Link4 = VGroup(Dots[16], Dots[15], Arrow(start=Dots[16], end=Dots[15], buff=0.05, stroke_width=3, color="#8080FF"))
    
    Trans1 = VGroup(Dots[5], Dots[4], Arrow(start=Dots[5], end=Dots[4], buff=0.05, stroke_width=3, color="#FF8080"))
    Char1 = MyText("C", 0.5).move_to(Trans1).shift(UP * 0.2)
    Trans2 = VGroup(Dots[6], Arrow(start=Dots[6], end=Dots[4], buff=0.05, stroke_width=3, color="#FF8080"))
    Char2 = MyText("C", 0.5).move_to(Trans2).shift(UP * 0.3)
    Trans3 = VGroup(Dots[7], Dots[8], Arrow(start=Dots[7], end=Dots[8], buff=0.05, stroke_width=3, color="#FF8080"))
    Char3 = MyText("C", 0.5).move_to(Trans3).shift(UP * 0.2)

    self.play(FadeIn(Whole))
    XTex = MyText("X", 2).move_to(Whole).set_color(YELLOW).shift(RIGHT * 0.5 + UP * 0.2)
    self.play(FadeIn(XTex))
    Whole.add(XTex)
    self.wait(1)

    self.play(FadeIn(N))
    NTex = MyText("N", 2).move_to(N).set_color(YELLOW).shift(RIGHT * 0.5 + UP * 0.2)
    self.play(FadeIn(NTex))
    N.add(NTex)
    self.wait(1)

    self.play(FadeIn(VGroup(Trans1, Char1)))
    
    self.play(FadeIn(VGroup(Fa, Link1)))
    self.play(FadeIn(VGroup(Trans2, Char2)), Transform(N, New_N))

    self.play(FadeIn(VGroup(Y, Link2)))

    self.play(FadeIn(VGroup(Ts, Trans3, Char3)))
    TsTex = MyText("T", 2).move_to(Ts).set_color(YELLOW).shift([0, -0.2, 0])
    TTex = MyText("T", 2).move_to(T).set_color(YELLOW).shift([0.3, 0, 0])
    YTex = MyText("Y", 2).move_to(Y).set_color(YELLOW).shift([0.2, -0.1, 0])
    self.play(FadeIn(YTex))
    self.play(FadeIn(TsTex))
    Y.add(YTex)
    T.add(TTex)
    Ts.add(TsTex)
    self.wait(1)

    MarkUp = VGroup(Dots[13], Dots[14])
    MarkUp.add(Arrow(start=Dots[13], end=Dots[14], buff=0.05, stroke_width=3))
    MarkUp.add(Arrow(start=Dots[14], end=Dots[13], buff=0.05, stroke_width=3))
    MarkUp.add(MyText("Length", 0.5).set_color(GREEN).next_to(MarkUp, DOWN))
    self.play(FadeIn(MarkUp))
    self.wait(1)
    self.play(FadeOut(MarkUp))
    self.wait(1)

    Myy = MyText("y").set_color(GREEN).next_to(Y, LEFT).shift(RIGHT * 0.5)
    Myt = MyText("t=y+1").set_color(GREEN).next_to(Ts, RIGHT, buff = 0.1)
    self.play(FadeIn(Myy))
    self.play(FadeIn(Myt))
    self.wait(1)

    self.play(FadeIn(Link4))

    TmpD = Dot(radius=0.03).next_to(T, LEFT).shift(RIGHT * 0.7)
    TmpT = VGroup(Dots[7], TmpD, Arrow(start=Dots[7], end=TmpD, buff=0.05, stroke_width=3, color="#FF8080"))
    TmpCh = MyText("C", 0.5).move_to(TmpT).shift(UP * 0.2)
    self.play(ReplacementTransform(Trans3, TmpT), ReplacementTransform(Char3, TmpCh), ReplacementTransform(Ts, T))
    self.wait(1)
    
    Dots[8] = TmpD
    Char3 = TmpCh
    Trans4 = VGroup(Dots[9], Arrow(start=Dots[9], end=Dots[8], buff=0.05, stroke_width=3, color="#FF8080"))
    Char4 = MyText("C", 0.5).move_to(Trans4).shift(UP * 0.2)
    self.play(FadeIn(VGroup(Uncle, Link3, Trans4, Char4)))
    self.wait(1)


    

    self.play(FadeOut(VGroup(Trans3, Trans4, Char3, Char4)))
    self.play(ReplacementTransform(T, VGroup(T1, T2)))
    self.play(T1.animate.shift(UP))



    Trans5 = VGroup(Dots[5])


    self.wait(1)

# manimgl SAM.py EC -o -c "BLACK"
# manimgl SAM.py EC2 -o -c "BLACK"
# manimgl SAM.py Constru -o -c "BLACK"
# manimgl SAM.py BANANA -o -c "BLACK"
# manimgl SAM.py EC2 -o -c "BLACK" --frame_rate 60
# manimgl SAM.py DAG -o -c "BLACK" --frame_rate 30
# manimgl SAM.py Transition -o -c "BLACK" --frame_rate 30
# manimgl SAM.py ComplAdd -o -c "BLACK" --frame_rate 30
# manimgl SAM.py Trian -o -c "BLACK" --frame_rate 30