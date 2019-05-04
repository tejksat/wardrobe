###Textures
PaintedMDF from DMFWood6 is rich polished wood with reflection

Example:
```
#include "textures.inc"

box { <1.4, 0.0, 0.0>, <1.375, 2.4, 0.6> texture{DMFWood6} }
```

This is nice painted matt texture taken from [Texture for wall paints needed](http://news.povray.org/povray.general/thread/%3C40adf648@news.povray.org%3E/?ttop=287109&toff=2050) thread:

```
#local PaintedMDF = texture{
pigment{ rgb<1 .95 .85> } // off-white
finish{ brilliance .6 }
}
```


###Lights

####Bulb
```
#include "textures.inc"


#declare Lightbulb = union {
  merge {
    sphere { <0,0,0>,1 }
    cylinder {
      <0,0,1>, <0,0,0>, 1
      scale <0.35, 0.35, 1.0>
      translate  0.5*z
    }
    texture {
      pigment {color rgb <1, 1, 1>}
      finish {ambient .8 diffuse .6}
    }
  }
  cylinder {
    <0,0,1>, <0,0,0>, 1
    scale <0.4, 0.4, 0.5>
    texture { Brass_Texture }
    translate  1.5*z
  }
  rotate -90*x
  scale .05
}
  
...
  
light_source {
  <1.3,2.4,0.8>
  color Gray50

  looks_like { Lightbulb }
}

  
```