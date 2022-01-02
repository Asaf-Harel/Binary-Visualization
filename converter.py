from PIL import Image, ImageDraw

from scurve import progress
from scurve.hilbert import Hilbert
from scurve.color import ColorClass


def convert_to_image(size, data, name):
    prog = progress.Progress(None)

    prog.set_target((size ** 2) * 4)
    csource = ColorClass(data)
    map = Hilbert.fromSize(2, size ** 2)
    c = Image.new("RGB", (size, size * 4))
    cd = ImageDraw.Draw(c)
    step = len(csource) / float(len(map) * 4)

    sofar = 0
    for quad in range(4):
        for i, p in enumerate(map):
            off = (i + (quad * size ** 2))
            color = csource.point(
                int(off * step)
            )
            x, y = tuple(p)
            cd.point(
                (x, y + (size * quad)),
                fill=tuple(color)
            )
            if not sofar % 100:
                prog.tick(sofar)
            sofar += 1
    c.save(name)

    print('\n')