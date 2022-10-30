# this is a simple tool to copy a local circuitpy project
# to the device. 
# it is helpful because it is much easier to version control
# these projects when the development is not actually happening
# on the board (the board memory is too small to handle a .git/) 

wd=$(pwd) #local dev directory
pd="/media/$USER/CIRCUITPY" # device location
# local directory of circuitpy libraries
libdir="/home/$USER/circuitpy/libs/adafruit-circuitpython-bundle-8.x-mpy-20221029/lib"

# copy the library .mpy files to the device
rm -rf $pd/lib/*
for file in $(cat libs.txt); do
	src=$libdir/$file
	dst=$pd/lib/$file
	cp -r $src $dst
done

# copy all local files/folders not in the .cpignore file to the device
tomove=$(ls | grep -vw -E $(cat .cpignore | tr -s "\n" "|"))
for file in $tomove; do
	src=$wd/$file
	dst=$pd/$file
	cp -r $src $dst
done
