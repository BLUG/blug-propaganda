import cairo
import rsvg
import sys

img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1920,1080)

ctx = cairo.Context(img)

## handle = rsvg.Handle(<svg filename>)
# or, for in memory SVG data:
handle= rsvg.Handle(sys.argv[1])

handle.render_cairo(ctx)

img.write_to_png(sys.argv[2])
