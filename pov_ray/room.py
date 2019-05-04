from typing import TextIO


def setup_lights(writer: TextIO):
    _place_light(writer, 1.3, 2.4, 0.8)
    _place_light(writer, 1.3, 2.4, 1.5)
    _place_light(writer, 1.3, 2.4, 2.2)


def _place_light(writer: TextIO, x, y, z):
    writer.write(f"""
light_source {{
  <{x},{y},{z}>
  color Gray50
}}

// looks_like {{ Lightbulb }}
""")
