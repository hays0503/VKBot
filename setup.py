from cx_Freeze import setup, Executable

base = None

executables = [Executable("download.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<VK bot by hays0503>",
    options = options,
    version = "<3.0>",
    description = '<download image and post there in vk>',
    executables = executables, requires=['requests', 'vk']
)