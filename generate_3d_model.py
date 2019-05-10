import subprocess
from datetime import datetime
from shutil import copyfile
from typing import TextIO

from builder.pov_builder import PovBuilder
from pov_ray import room
from wardrobe.left_part import assembly as left_part_assembly
from wardrobe.right_part import assembly as right_part_assembly


def write_includes(writer: TextIO):
    writer.write("""
#include "colors.inc"
#include "woods.inc"

""")


def prepare_camera(writer: TextIO):
    writer.write("""
#declare CamLoc= <4,1.8,4>;
#declare CamLook=<0,1.2,0>;

#declare S_angle=(CamLook.y-CamLoc.y)/(CamLoc.y*1000);

#declare Shear= transform {
   matrix <  1,  0,  0,
             0,  1,  -S_angle,
             0,  0,  1,
             0,  0,  0 >
}

//Place the camera
camera {
  location  CamLoc  //Camera location
  angle 70      //Angle of the view--increase to see more, decrease to see less
  transform Shear // comment out to see 'falling buildings'
  look_at   CamLook    //Where camera is pointing
}

""")


def prepare_light(writer: TextIO):
    writer.write("""
//Ambient light to "brighten up" darker pictures
global_settings { ambient_light White }

//Set a background color
background { color White }    

""")
    room.setup_lights(writer)


def prepare_textures(writer: TextIO):
    writer.write("""
#local PaintedMDF = texture{
pigment{ rgbt<1 .95 .85 .35> } // off-white
finish{ brilliance .6 }
}

#local Texture_01 = PaintedMDF

""")


if __name__ == '__main__':
    now = datetime.now()
    timestamp = now.isoformat(timespec='milliseconds')
    pathname_base = f'output/wardrobe_{timestamp}'

    with open(f'{pathname_base}.pov', 'w') as f:
        write_includes(f)
        prepare_camera(f)
        prepare_light(f)
        prepare_textures(f)

        builder = PovBuilder(f)

        left_part_assembly.build(builder)
        right_part_assembly.build(builder)

    subprocess.run(['povray', f'+A', f'+O{pathname_base}.png', f'{pathname_base}.pov'])

    copyfile(f'{pathname_base}.png', 'output/wardrobe_latest.png')
