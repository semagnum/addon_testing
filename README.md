# Test Your Add-on

This is a template Blender add-on to showcase how simple unit testing can be!

The unit tests cover:

- installing and uninstalling the add-on, both as an add-on and an add-on extension
- running operators, including passing arguments for properties
- checking the add-on version between `bl_info` and `blender_manifest.toml` match

## Testing with bpy in virtual environment

Blender as a Python module is available [on pypi](https://pypi.org/project/bpy/) as `bpy`.
You can also build it yourself manually; see [docs](https://developer.blender.org/docs/handbook/building_blender/python_module/).
It runs Blender headlessly within a Python environment.

This allows your tests to run within a Blender environment of any supported version, ideal for CI/CD and pipelines.

## Testing with Blender executable

For those uncomfortable or otherwise unable to setup an environment with Blender as a Python module,
developers can also run the unit tests directly with the Blender executable:

```
path/to/blender.exe --background --factory-startup --python tests/__init__.py
```

This will run all the unit tests within the Blender executable.