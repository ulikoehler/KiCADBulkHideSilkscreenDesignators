# "Bulk hide Silkscreen Designators" KiCAD plugin

"Bulk hide Silkscreen Designators" is a plugin for KiCAD that allows you to hide all the silkscreen designators on a PCB.
It works on all selected footprints. If you select everything using Ctrl+A, it will hide all reference designators.

Only the reference designators on the `F.Silkscreen` and `B.Silkscreen` layer are hidden. `F.Fab` and `B.Fab` are not affected.

## Motivation

If you design PCBs with lots of fotprints close together, the reference designators will overlap.
Since using the EDA data for assembly & maintenance is preferred anyway, the silkscreen designators serve little purpose in practice.

Without using this plugin, you will have to manually hide the reference designators on each footprint.

## Usage

1. Select the footprints you want to hide the reference designators on. Most often you want to just select everything using Ctrl+A.
2. Click on the logo in the toolbar:

![icon.png]

3. Drink a coffee! You MUST drink a coffee after using this plugin. Else, all the time saved will go to waste.

### Before "Bulk hide Silkscreen Designators"

![before.png]

### After "Bulk hide Silkscreen Designators"

![after.png]