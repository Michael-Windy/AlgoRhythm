from manimlib import *
import numpy 
CharaWid = 0.266

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