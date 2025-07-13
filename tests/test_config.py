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

import importlib.util
import logging
import os
import sys
from pathlib import Path
import unittest

import tomllib

class TestConfig(unittest.TestCase):

    def bl_info_dict(self):
        init_file = Path(__file__).parent.parent / '__init__.py'
        spec = importlib.util.spec_from_file_location('addon_testing', init_file)
        my_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(my_module)

        bl_info = my_module.bl_info
        logging.debug(bl_info)
        return bl_info

    def get_manifest_info(self):
        toml_file = Path(__file__).parent.parent / 'blender_manifest.toml'
        with open(toml_file, 'rb') as f:
            config = tomllib.load(f)

        logging.debug(config)

        return config

    def test_assert_version(self):
        """bl_info and blender_manifest versions match"""
        bl_info = self.bl_info_dict()
        manifest = self.get_manifest_info()

        bl_info_version = bl_info['version']
        bl_info_str = f'{bl_info_version[0]}.{bl_info_version[1]}.{bl_info_version[2]}'
        self.assertEqual(bl_info_str, manifest['version'])

    def test_assert_name(self):
        """bl_info and blender_manifest names match"""
        bl_info = self.bl_info_dict()
        manifest = self.get_manifest_info()

        bl_info_name = bl_info['name']
        self.assertEqual(bl_info_name, manifest['name'])

    def test_assert_description(self):
        """bl_info and blender_manifest descriptions match"""
        bl_info = self.bl_info_dict()
        manifest = self.get_manifest_info()

        self.assertEqual(bl_info['description'], manifest['tagline'])

    def test_assert_author(self):
        """bl_info and blender_manifest authors match"""
        bl_info = self.bl_info_dict()
        manifest = self.get_manifest_info()

        self.assertEqual(bl_info['author'], manifest['maintainer'])