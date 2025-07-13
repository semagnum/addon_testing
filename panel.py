# Unit testing template for Blender add-ons
# Copyright (C) 2025 Spencer Magnusson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bpy


class AddonTestPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = 'Test Panel'
    bl_idname = 'OBJECT_PT_test'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text='Hello world!', icon='WORLD_DATA')

        row = layout.row()
        row.label(text='Active object is: ' + obj.name)
        row = layout.row()
        row.prop(obj, 'name')

        row = layout.row()
        row.operator('mesh.primitive_cube_add')
        row.operator('object.test')


def register():
    bpy.utils.register_class(AddonTestPanel)


def unregister():
    bpy.utils.unregister_class(AddonTestPanel)
