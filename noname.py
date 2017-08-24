# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 404,219 ), style = wx.DEFAULT_DIALOG_STYLE )
		
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
        m_comboBox1Choices = [u'1', u'2', u'3', '4']
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        self.m_comboBox1.SetSelection(3)
        bSizer1.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
        self.SetSizer( bSizer1 )
        self.Layout()
		
        self.Centre( wx.BOTH )
        self.initialWindow()
	    
	    
    def __del__( self ):
        pass
	
    def initialWindow(self):
        flag = 0
        
        antNum = self.m_comboBox1.GetCurrentSelection()+1
        n = 1
        while (n <= antNum):
            if (flag == 0) and (n == 2): 
                n == 2
                flag = 1
                print "re-Run"
                continue
            
            print n
            n += 1
        
        
        
class App(wx.App):
    def OnInit(self):
        try:
            self.main = MyDialog1(None)
            self.main.Show(True)
            self.SetTopWindow(self.main)
        except Exception,e:
            print e
        return True

def main():
    application = App(0)
    application.MainLoop()

if __name__ == '__main__':
   main()