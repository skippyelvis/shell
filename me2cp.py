import subprocess
import os
import argparse

template = '''wd={}
pd={}
libdir={}

# copy the library .mpy files to the device
rm -rf $pd/lib/*
for file in $(cat libs.txt); do
	src=$libdir/$file
	dst=$pd/lib/$file
	cp -r $src $dst
done

# copy all local files/folders not in the .cpignore file to the device
if [ -e ".cpignore" ]; then
	tomove=$(ls | grep -vw -E $(cat .cpignore | tr -s "\n" "|"))
else
	tomove=$(ls)
fi
for file in $tomove; do
	src=$wd/$file
	dst=$pd/$file
	if [ -e "$dst" ]; then
		rm -rf $dst
	fi
	cp -r $src $dst
done'''

def me2cp(wd, pd, libdir):
    print("starting me2cp")
    global template
    script = template.format(wd, pd, libdir)
    out = subprocess.run(script, shell=True, capture_output=True)
    print("stderr:")
    print(out.stderr.decode())
    print("stdout:")
    print(out.stdout.decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--wd", default=os.getcwd())
    parser.add_argument("--pd", default=f"/media/{os.getlogin()}/CIRCUITPY")
    parser.add_argument("--libdir", default=f"/home/{os.getlogin()}/circuitpy/libs/adafruit-circuitpython-bundle-8.x-mpy-20221029/lib")
    args = parser.parse_args()
    me2cp(args.wd, args.pd, args.libdir)
