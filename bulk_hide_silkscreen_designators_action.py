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

        dlg = wx.RichMessageDialog(None, "Do you want to Replace Reference by values?","Choose an option",wx.YES | wx.CANCEL_DEFAULT)
        # dlg.ShowModal() # return value ignored as we have "Ok" only anyhow

        if dlg.ShowModal()==wx.ID_YES:
            #To move fab layer to silkscreen and sickscreen layer to fab
            #To show the values instead of component reference
            for selected_footprint in selected_footprints:
                value=selected_footprint.Value()
                reference=selected_footprint.Reference()

                if value.GetLayerName()=="F.Fab":
                    #Setting the layer to F_Fab
                    reference.SetLayer(49)
                    #Setting the layer to F_SilkS
                    value.SetLayer(37)

                elif value.GetLayerName()=="B.Fab":
                    #Setting the layer to B_Fab
                    reference.SetLayer(48)
                    #Setting the layer to B_SilkS
                    value.SetLayer(36)

                elif value.GetLayerName()=="F.Silkscreen":
                    #Setting the layer to F_SilkS
                    reference.SetLayer(37)
                    #Setting the layer to F_Fab
                    value.SetLayer(49)

                elif value.GetLayerName()=="B.Silkscreen":
                    #Setting the layer to B_SilkS
                    value.SetLayer(36)
                    #Setting the layer to B_Fab
                    reference.SetLayer(48)

        for selected_footprint in selected_footprints:
            # Hide reference
            reference = selected_footprint.Reference()
            if reference:
                if reference.IsVisible():
                    # Hide reference if visible earlier
                    reference.SetVisible(False)
                else:
                    # Show reference if not visible earlier
                    reference.SetVisible(True)
        pcbnew.Refresh()