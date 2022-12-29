# me2cp
`me2cp` helps you write circuitpython projects locally and distribute them to devices easily

# usage
`me2cp` is a helper to copy your project code and `.mpy` files from your local computer to your circuitpython device.

It is most helpful for larger projects with multiple devices which share code.

It relies on a project configuration file, `proj.yaml`.

This file allows you to define

    - the path of the device to copy to
    - external/shared code folders to copy 
    - files from local project directory to ignore when copying
    - local directory containing circuitpython `.mpy` files
    - `.mpy` libraries/modules to upload to devices `lib/`

Check out the `cpyconfig.default` file for an example

To use, run `python3 /path/to/me2cp.py` in your local circuitpython project directory.
