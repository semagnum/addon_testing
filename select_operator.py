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


class TestOperator(bpy.types.Operator):
    """Test operator that deselects all objects"""
    bl_idname = 'object.test'
    bl_label = 'Simple Object Operator'

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        return bpy.ops.object.select_all(action='DESELECT')


def menu_func(self, context):
    self.layout.operator(TestOperator.bl_idname, text=TestOperator.bl_label)


def register():
    bpy.utils.register_class(TestOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(TestOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
