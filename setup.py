from cx_Freeze import setup, Executable

base = None


executables = [Executable("test.py", base=base)]

packages = ["pygame"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Snake",
    options = options,
    version = "0.1",
    description = 'Simple Snake Game',
    executables = executables
)