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

if 'bl_info' in locals():
    import importlib
    import os
    import sys
    import types

    def reload_package(package):
        assert (hasattr(package, '__package__'))
        fn = package.__file__
        fn_dir = os.path.dirname(fn) + os.sep
        module_visit = {fn}
        del fn

        def reload_recursive_ex(module):
            module_iter = (
                module_child
                for module_child in vars(module).values()
                if isinstance(module_child, types.ModuleType)
            )
            for module_child in module_iter:
                fn_child = getattr(module_child, '__file__', None)
                if (fn_child is not None) and fn_child.startswith(fn_dir) and fn_child not in module_visit:
                    # print('Reloading:', fn_child, 'from', module)
                    module_visit.add(fn_child)
                    reload_recursive_ex(module_child)

            importlib.reload(module)

        return reload_recursive_ex(package)

    reload_package(sys.modules[__name__])


bl_info = {
    "name": "Test Your Add-on",
    "author": "Spencer Magnusson",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Nowhere lol",
    "description": "Add-on Template for testing your add-ons",
    "category": "User Interface",
}

def register():
    from . import select_operator, panel
    select_operator.register()
    panel.register()

def unregister():
    from . import select_operator, panel
    panel.unregister()
    select_operator.unregister()