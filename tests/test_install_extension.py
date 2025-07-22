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

from pathlib import Path
import sys
import unittest

class TestExtension(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Install extension via repository"""
        repo = str(Path(__file__).parent.parent.parent)

        import bpy
        bpy.ops.wm.read_factory_settings(use_factory_startup_app_template_only=True)

        repo_module = 'test_repo'
        new_repo = bpy.context.preferences.extensions.repos.new(
            name='Test Repo',
            module=repo_module,
            custom_directory=repo,
            source='USER'
        )
        cls.module_path = 'bl_ext.' + repo_module + '.addon_testing'
        bpy.ops.preferences.addon_enable(module=cls.module_path)

    def test_addon_panel_exists(self):
        """Check if add-on panel exists"""
        import bpy
        self.assertTrue(hasattr(bpy.types, 'OBJECT_PT_test'))

    def test_addon_operator(self):
        """Check for and run add-on operator"""
        import bpy
        
        bpy.ops.object.test(action='DESELECT')
        assert bpy.context.selected_objects == []

        bpy.ops.object.test(action='SELECT')
        assert all(obj.name in {'Cube', 'Camera', 'Light'} for obj in bpy.context.selected_objects)

        bpy.ops.object.test(objects_to_select=[
            {'name': 'Cube', 'select': True},
            {'name': 'Camera', 'select': False}
        ])
        assert bpy.data.objects['Cube'].select_get()
        assert not bpy.data.objects['Camera'].select_get()

    @classmethod
    def tearDownClass(cls):
        """Disable add-on"""
        import bpy
        bpy.ops.preferences.addon_disable(module=cls.module_path)

        