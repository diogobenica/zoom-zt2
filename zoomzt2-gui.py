#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0 on Sun Sep 15 09:53:08 2019
#

import wx
import zoomzt2
import os

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class _479389042__675845753_MyFrame(wx.Frame):
    effect = None
    effects = []
    files = []
    pedal = None

    def __init__(self, *args, **kwds):
        # begin wxGlade: _479389042__675845753_MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.button_6 = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "Select Effect")
        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "<No Effect Selected>", style=wx.TE_MULTILINE)
        self.notebook_1_tab2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_box_1 = wx.ListBox(self.notebook_1_tab2, wx.ID_ANY, choices=["<Connect to list effects>"], style=wx.LB_HSCROLL | wx.LB_SINGLE)
        self.notebook_1_tab3 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_box_2 = wx.ListBox(self.notebook_1_tab3, wx.ID_ANY, choices=["<Connect to list files>"])
        self.button_1 = wx.Button(self, wx.ID_ANY, "Disconnect")
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "Connect")
        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, "Install")
        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, "Remove")
        self.button_5 = wx.Button(self.panel_1, wx.ID_ANY, "Download")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.butSelect, self.button_6)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.PageChange, self.notebook_1)
        self.Bind(wx.EVT_BUTTON, self.butQuit, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.butConnect, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.butInstall, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.butRemove, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.butDownload, self.button_5)
        # end wxGlade

        self.pedal = zoomzt2.zoomzt2()
        if self.ConnectPedal():
            self.UpdateButtons()

    def __set_properties(self):
        # begin wxGlade: _479389042__675845753_MyFrame.__set_properties
        self.SetTitle("ZoomZT2-GUI")
        self.text_ctrl_1.SetMinSize((-1, 300))
        self.list_box_1.SetMinSize((398, 300))
        self.list_box_2.SetMinSize((398, 300))

        # Enable file downloads (or not)
        #self.notebook_1_tab3.Hide()

        self.button_3.Disable()
        self.button_3.Hide()
        self.button_4.Hide()
        self.button_5.Hide()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: _479389042__675845753_MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_4.Add(self.button_6, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Info", style=wx.ALIGN_CENTER)
        label_2.SetMinSize((398, -1))
        sizer_4.Add(label_2, 0, wx.ALL, 0)
        sizer_4.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_4)
        sizer_5.Add(self.list_box_1, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        self.notebook_1_tab2.SetSizer(sizer_5)
        sizer_6.Add(self.list_box_2, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.notebook_1_tab3.SetSizer(sizer_6)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "New")
        self.notebook_1.AddPage(self.notebook_1_tab2, "Effects")
        self.notebook_1.AddPage(self.notebook_1_tab3, "Files")
        sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_1, 1, 0, 0)
        sizer_1.Add(self.button_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.button_3, 1, wx.EXPAND, 0)
        sizer_1.Add(self.button_4, 1, wx.EXPAND, 0)
        sizer_1.Add(self.button_5, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_1)
        sizer_3.Add(self.panel_1, 1, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def butSelect(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        dlg = wx.FileDialog(self, "Select Effect", wildcard="*.ZD2",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_CANCEL:
            event.Skip()
            return
        self.effect = dlg.GetPath()
        dlg.Destroy()

        binfile = open(self.effect, "rb")
        if binfile:
            bindata = binfile.read()
            binfile.close()

            config = zoomzt2.ZD2.parse(bindata)
            head, tail = os.path.split(self.effect)
            self.text_ctrl_1.SetValue(tail + " = " + config['name'])
            self.text_ctrl_1.AppendText("\nVer  : " + config['version'])
            self.text_ctrl_1.AppendText("\nGroup: " + str(config['group']) + " (" \
                    + config['groupname'] + ")")
            self.text_ctrl_1.AppendText("\nID   : " + hex(config['id']))

            self.button_6.SetLabel(tail)
            self.button_3.Enable()

        event.Skip()

    def PageChange(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        self.UpdateButtons()
        event.Skip()

    def butQuit(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        if self.pedal.is_connected():
            self.DisconnectPedal()
        event.Skip()

    def butConnect(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        self.ConnectPedal()
        event.Skip()

    def butInstall(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        if self.effect == None:
            event.Skip()
            return

        self.pedal.file_check("FLST_SEQ.ZT2")
        data = self.pedal.file_download("FLST_SEQ.ZT2")

        binfile = open(self.effect, "rb")
        if binfile:
            bindata = binfile.read()
            binfile.close()

            binconfig = zoomzt2.ZD2.parse(bindata)

            self.pedal.file_check(self.effect)
            self.pedal.file_upload(self.effect, bindata)
            self.pedal.file_close()

            data = self.pedal.add_effect_from_filename(data, self.effect)

            self.pedal.file_check("FLST_SEQ.ZT2")
            self.pedal.file_upload("FLST_SEQ.ZT2", data)
            self.pedal.file_close()

            self.text_ctrl_1.AppendText("\n\nEffect installed!")
            self.button_3.Disable()

        event.Skip()

    def butRemove(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        name = self.list_box_1.GetString(self.list_box_1.GetSelection())
        if name :
            self.pedal.file_check(name)
            self.pedal.file_delete(name)

            self.pedal.file_check("FLST_SEQ.ZT2")
            data = self.pedal.file_download("FLST_SEQ.ZT2")

            data = self.pedal.remove_effect(data, name)

            self.pedal.file_check("FLST_SEQ.ZT2")
            self.pedal.file_upload("FLST_SEQ.ZT2", data)
            self.pedal.file_close()

            self.ReadEffects()
            self.ReadFiles()

        event.Skip()

    def butDownload(self, event):  # wxGlade: _479389042__675845753_MyFrame.<event_handler>
        name = self.list_box_2.GetString(self.list_box_2.GetSelection())
        if name :
            self.pedal.file_check(name)
            data = self.pedal.file_download(name)
            self.pedal.file_close()

            if data:
                outfile = open(name, "wb")
                if not outfile:
                    sys.exit("Unable to open FILE for writing")
                outfile.write(data)
                outfile.close()

        event.Skip()

    def UpdateButtons(self):
        self.button_3.Hide()
        self.button_4.Hide()
        self.button_5.Hide()

        if self.pedal.is_connected():
            self.button_2.Hide()
        else:
            self.button_2.Show()
            self.Layout()
            return

        page = self.notebook_1.GetSelection()
        if page == 0:
            self.button_3.Show()
        if page == 1:
            self.button_4.Show()
        if page == 2:
            self.button_5.Show()
        self.Layout()

    def ConnectPedal(self):
        if self.pedal.connect():
            self.ReadEffects()
            self.ReadFiles()
            self.UpdateButtons()
            return True
        return False

    def DisconnectPedal(self):
        self.pedal.disconnect()
        self.UpdateButtons()

    def ReadEffects(self):
        self.pedal.file_check("FLST_SEQ.ZT2")
        data = self.pedal.file_download("FLST_SEQ.ZT2")
        self.pedal.file_close()

        if not data:
            return False

        config = zoomzt2.ZT2.parse(data)
        self.effects.clear()
        for group in config[1]:
            for effect in dict(group)["effects"]:
                if effect['installed']:
                    self.effects.append(dict(effect)["effect"])

        self.list_box_1.Set(self.effects)

    def ReadFiles(self):
        name = self.pedal.file_wild(True)
        if name:
            self.files.clear()
        while name:
            self.files.append(name)
            name = self.pedal.file_wild(False)
        self.pedal.file_close()

        self.list_box_2.Set(self.files)

# end of class _479389042__675845753_MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = _479389042__675845753_MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    App = MyApp(0)
    App.MainLoop()
