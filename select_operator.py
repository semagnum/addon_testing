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


class Item(bpy.types.PropertyGroup):
    select: bpy.props.BoolProperty()


class TestOperator(bpy.types.Operator):
    """Test operator that deselects all objects"""
    bl_idname = 'object.test'
    bl_label = 'Simple Object Operator'
    bl_options = {'REGISTER', 'UNDO'}

    action: bpy.props.EnumProperty(
        name='Action',
        items=[
            ('DESELECT', 'Deselect', 'Deselect all objects'),
            ('SELECT', 'Select', 'Select all objects')
        ],
        default='DESELECT'
    )

    objects_to_select: bpy.props.CollectionProperty(
        type=Item
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if self.objects_to_select:
            for item in self.objects_to_select:
                name, select = item.name, item.select
                if name not in bpy.data.objects:
                    self.report({'ERROR'}, f'Object {name} not found, skipping')
                
                bpy.data.objects[name].select_set(select)
            context.view_layer.objects.active = context.selected_objects[0]
            return {'FINISHED'}

        return bpy.ops.object.select_all(action=self.action)


def menu_func(self, context):
    self.layout.operator(TestOperator.bl_idname, text=TestOperator.bl_label)


def register():
    bpy.utils.register_class(Item)
    bpy.utils.register_class(TestOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(TestOperator)
    bpy.utils.unregister_class(Item)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
