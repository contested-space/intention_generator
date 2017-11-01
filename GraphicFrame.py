import wx
from Functions import *

class GraphicFrame(wx.Frame):
  def __init__(self, parent, size = (300,300), pos = (0,0), data = None, concept=None):
    wx.Frame.__init__(self, parent, -1, 'Parameters', size = size, pos = pos)
    self.panel = wx.Panel(self)
    self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    #self.createMenuBar()
    self.parent = parent
    self.concept = concept
    self.isFocused = True
    #self.SetBackgroundColour('blue')

  def OnIdle(self, event):
    self.Refresh()
    event.Skip()


  def drawGraph(self, event = None):
    dc = wx.PaintDC(event.GetEventObject())
    dc.Clear()
    dc.SetPen(wx.Pen("BLACK", 2))
    posList = []


    def paintStructure(concept, i, j):  
      def contains(poslist, pt):
        if poslist == None:
          return False
        elif len(poslist) == 0:
          return False
        if poslist[0].y == pt.y and poslist[0].x == pt.x:
          return True
        else:
          return contains(poslist[1:], pt)

      if concept != None:
        if concept.getConcept() != None:
          while (contains(posList, Point(i * 50, j * 50))):
            j += 1
            
          concept.setPos(Point(i * 50, j * 50))
          posList.append(Point(i * 50, j * 50))
          dc.DrawCircle(i * 50, j * 50, 15)
          dc.DrawText(concept.getConcept(), 50 * i - 6,  50 * j - 4)
          if concept.getNext() != None:
            paintStructure(concept.getNext(), i + 1 , j)
          if concept.getChild() != None:
           paintStructure(concept.getChild(), i + 1, j + 1)

    paintStructure(self.concept, 2, 2)
    def paintLinks(concept):
      if concept != None:
        if concept.getConcept() != None:
          #dc.DrawCircle(i * 50, j * 50, 15)
          #dc.DrawText(concept.getConcept(), 50 * i - 6,  50 * j - 4)
          if concept.getNext() != None:
            dc.SetPen(wx.Pen("RED", 2))
            dc.DrawLine(concept.pos.x, concept.pos.y, concept.getNext().pos.x, concept.getNext().pos.y)
            paintLinks(concept.getNext())
          if concept.getChild() != None:
            dc.SetPen(wx.Pen("BLUE"))
            dc.DrawLine(concept.pos.x, concept.pos.y, concept.getChild().pos.x, concept.getChild().pos.y)
            paintLinks(concept.getChild())
    paintLinks(self.concept)


    """
    for i in range(len(graphList)-1):
      dc.DrawLine(i, self.size[1] - graphList[i]*self.size[1]/10,i + 1,   self.size[1] - graphList[i+1]*self.size[1]/10)
      #dc.DrawPoint(i, self.size[1] - graphList[i]*self.size[1]/10)
    if not self.isReal:
      dc.SetPen(wx.Pen('Black', 1))
      dc.DrawLine(self.size[0]/2, 0, self.size[0]/2, self.size[1])
    """

    #test for freq marker
    dc.SetPen(wx.Pen('blue', 1))
    #print int(float(self.size[0])/24000 * freq * self.size[0])
    #print self.size[0]

  def OnSize(self, event):
    self.size = event.GetSize()
    self.drawGraph(event)
    self.Refresh()
    event.Skip()


  def OnPaint(self, event = None):
    self.drawGraph(event)


    
