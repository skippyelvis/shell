from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import pathlib
import shutil
import os

class me2cp:

    def __init__(self, initproj=False):
        configpath = pathlib.Path(".cpyconfig")
        if not configpath.exists() or initproj:
            shutil.copyfile(f"/home/{os.getlogin()}/shell/cpyconfig.default", 
                            ".cpyconfig")
        with open(configpath, "r") as fp:
            self.config = load(fp.read(), Loader=Loader)

    def clear_device(self):
        for f in os.listdir(self.config["devdir"]):
            if f in [".fseventsd", ".Trashes", ".metadata_never_index"]:
                continue
            path = pathlib.Path(self.config["devdir"]) / pathlib.Path(f)
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    def transfer_code(self):
        files = os.listdir()
        tomove = list(set(files) - set(self.config["ignore"]))
        for f in tomove:
            srcpath = pathlib.Path(self.config["workdir"]) / pathlib.Path(f)
            dstpath = pathlib.Path(self.config["devdir"]) / pathlib.Path(f)
            if srcpath.is_dir():
                shutil.copytree(srcpath, dstpath)
            else:
                shutil.copy(srcpath, dstpath)

    def transfer_libs(self):
        devlibdir = pathlib.Path(self.config["devdir"]) / pathlib.Path("libs")
        if not devlibdir.exists():
            devlibdir.mkdir()
        if self.config.get("libs", None) is None:
            return
        for lib in self.config["libs"]:
            libpath = pathlib.Path(self.config["libdir"]) / pathlib.Path(lib)
            if libpath.is_dir():
                shutil.copytree(libpath, devlibdir / pathlib.Path(lib))
            else:
                shutil.copy(libpath, devlibdir / pathlib.Path(lib))

    def __call__(self):
        self.clear_device()
        self.transfer_code()
        self.transfer_libs()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--init", default=False, 
                        help="initialize project directory",
                        action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    obj = me2cp(initproj=args.init)
    if not args.init:
        obj()
