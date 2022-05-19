# Utility script to convert png source to python array

from PIL import Image

# Layout of the icons inside the PNG

ICONS_MATRIX_SIZE = (10, 10)
ICONS_SIZE = (8, 8)
PIXEL_SIZE = (4, 4)
OFFSETS = (5, 24)
CELL_SIZE = (52, 48) 

def get_cell_base(x):
    return (OFFSETS[0] + x[0]*CELL_SIZE[0], OFFSETS[1] + x[1]*CELL_SIZE[1])



def sample(pixels):
    (r,g,b) = (sorted(p[k] for p in pixels) for k in (0,1,2))
    return tuple(c[len(c) // 2] for c in (r,g,b))

def cell(img, pos):
    (bx, by) = get_cell_base(pos)
    return [[
            sample([img.getpixel((bx+x*PIXEL_SIZE[0]+dx,by+y*PIXEL_SIZE[1]+dy)) 
                 for dx in range(PIXEL_SIZE[0]) 
                 for dy in range(PIXEL_SIZE[1])])
            for x in range(ICONS_SIZE[0])]
        for y in range(ICONS_SIZE[1])
        ]

if __name__ == '__main__':
    img = Image.open("pixelart.png")
    icons = [cell(img, (x,y)) for x in range(ICONS_MATRIX_SIZE[0]) for y in range(ICONS_MATRIX_SIZE[1])]
    print(f"icons = {icons}")
