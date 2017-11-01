import wx
from GraphicFrame import GraphicFrame
from Functions import Concept
from Functions import generate

class GeneratorApp(wx.App):
  def __init__(self):
    wx.App.__init__(self)
    #s = 'S[SPEAC]PEA[SPA[SPACE]CE]C'
    s = generate()
    self.concept = Concept()
    self.concept.makeStructure(s)
    self.graphicFrame = GraphicFrame(None, size = (wx.DisplaySize()[0], wx.DisplaySize()[1]), pos = (0,0), concept=self.concept)
    self.graphicFrame.Show()


    



if __name__ == '__main__':
  app = GeneratorApp()
  app.MainLoop()

