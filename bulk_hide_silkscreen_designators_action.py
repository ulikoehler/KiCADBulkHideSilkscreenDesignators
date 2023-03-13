#!/usr/bin/env python
import pcbnew
import os.path
import wx

class BulkHideSilkscreenDesignators(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Bulk hide silkscreen designators"
        self.category = "Silkscreen"
        self.description = "Hide all silkscreen reference designators for selected footprints"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        # Filter just selected footprints
        selected_footprints: list[pcbnew.FOOTPRINT] = [
            footprint for footprint in pcbnew.GetCurrentSelection()
            if type(footprint).__name__ == 'FOOTPRINT'
        ]
        
        if len(selected_footprints) == 0:
            # Show info dialog
            dlg = wx.MessageDialog(None, "Please select one or multiple footprints!\n...or use Ctrl+A to select everything.", "No footprints selected", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        for selected_footprint in selected_footprints:
            # Hide reference
            reference = selected_footprint.Reference()
            if reference:
                reference.SetVisible(False)
        pcbnew.Refresh()