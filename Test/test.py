from manimlib import *
import numpy 

def TextBox(StringinBox: str, BoxScale: float=1) -> VGroup:
  StringLen = len(StringinBox)
  StrtoText = Text(StringinBox).scale(BoxScale)
  VerL = Rectangle(BoxScale * 0.266, BoxScale * 0.5).get_grid(1, StringLen, buff=0)
  return VGroup(VerL, StrtoText)

def CharaBox(CharinBox: str, BoxScale: float=1) -> VGroup:
  ChrtoText = Text(CharinBox).scale(BoxScale)
  VerL = Rectangle(BoxScale * 0.266, BoxScale * 0.5)
  return VGroup(VerL, ChrtoText)



class TextTest(Scene):
  def construct(self) :
    Textt = "12345678"
    Texttl = len(Textt)
    Theme = VGroup()
    TList = []
    for i in range(0, Texttl):
      TmpC = CharaBox(Textt[i], 2)
      Theme += TmpC
      TList.append(TmpC)
    Theme.arrange(buff=0)
    self.play(FadeIn(Theme))
    Here = TList[3][1].copy()
    Here.set_color(RED)
    self.play(ReplacementTransform(TList[3][1], Here))
    self.play(Transform(TList[2].copy(), TList[5]))
    self.wait(1)

class Test(Scene):
  CONFIG={
		"camera_config":{"background_color":"#000000"}
	}
  def construct(self) :
    Logo = SVGMobject("new logo.svg")
    Logo.set_fill(opacity=0)
    Logo.set_stroke(WHITE, 10)
    self.play(Write(Logo))
    self.play(Logo.animate.shift(UP))
    Theme = Text("AlgoRhythm")
    Theme.move_to(DOWN)
    self.play(Write(Theme))
    self.play(FadeOut(Theme, shift=DOWN))
    self.play(Logo.animate.shift([-5.5,2,0]).scale(0.5).set_stroke("#101010", 5))
    self.wait(1)
# manimgl test.py Test -o -c "BLACK"
# manimgl test.py TextTest -o -c "BLACK"