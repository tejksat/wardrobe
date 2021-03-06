from builder.primitives import Box, Point


def between(left: Box, right: Box, below: Box, height: float, height_offset: float = 0.0) -> Box:
    # assume that p0 < p1
    p0 = Point(min(left.p1.x, right.p1.x), below.p1.y + height_offset, max(left.p0.z, right.p0.z, below.p0.z))
    p1 = Point(max(right.p0.x, left.p0.x), below.p1.y + height_offset + height, min(left.p1.z, right.p1.z, below.p1.z))
    return Box(p0, p1)


def between_two(left: Box, right: Box, height: float, height_offset: float = 0.0) -> Box:
    # assume that p0 < p1
    p0 = Point(min(left.p1.x, right.p1.x), height_offset, max(left.p0.z, right.p0.z))
    p1 = Point(max(right.p0.x, left.p0.x), height_offset + height, min(left.p1.z, right.p1.z))
    return Box(p0, p1)


def right_from(box: Box, width: float, height: float, height_offset: float = 0.0) -> Box:
    # assume that p0 < p1
    p0 = Point(box.p1.x, height_offset, box.p0.z)
    p1 = Point(box.p1.x + width, height_offset + height, box.p1.z)
    return Box(p0, p1)
