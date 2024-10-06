import svgwrite
from PIL import Image, ImageDraw
import io
import cairosvg

def create_svg_logo(draw_function, size=(300, 300), filename='logo.svg'):
    dwg = svgwrite.Drawing(filename, size=size)
    draw_function(dwg)
    return dwg.tostring()

def create_png_logo(svg_string, size=(300, 300)):
    png_data = cairosvg.svg2png(bytestring=svg_string, output_width=size[0], output_height=size[1])
    return Image.open(io.BytesIO(png_data))

def concept_1(dwg):
    # Inspired by Apple: Simple, clean lettermark
    circle = dwg.circle(center=(150, 150), r=100, fill='none', stroke='black', stroke_width=10)
    text = dwg.text('A', insert=(150, 180), font_size=150, font_family="Arial", text_anchor="middle", fill='black')
    dwg.add(circle)
    dwg.add(text)

def concept_2(dwg):
    # Inspired by Airbnb: Abstract symbol
    triangle = dwg.polygon(points=[(150, 50), (50, 250), (250, 250)], fill='none', stroke='black', stroke_width=10)
    dwg.add(triangle)

def concept_3(dwg):
    # Inspired by Louis Vuitton: Interlocking letters
    text_a = dwg.text('A', insert=(75, 180), font_size=200, font_family="Arial", text_anchor="middle", fill='black')
    text_s = dwg.text('S', insert=(225, 180), font_size=200, font_family="Arial", text_anchor="middle", fill='black')
    dwg.add(text_a)
    dwg.add(text_s)

def concept_4(dwg):
    # Inspired by OpenAI: Geometric abstraction
    square = dwg.rect(insert=(75, 75), size=(150, 150), fill='none', stroke='black', stroke_width=10)
    line1 = dwg.line(start=(75, 75), end=(225, 225), stroke='black', stroke_width=10)
    line2 = dwg.line(start=(225, 75), end=(75, 225), stroke='black', stroke_width=10)
    dwg.add(square)
    dwg.add(line1)
    dwg.add(line2)

# Create SVG and PNG versions of each concept
concepts = [concept_1, concept_2, concept_3, concept_4]
for i, concept in enumerate(concepts, 1):
    svg_string = create_svg_logo(concept, filename=f'amisana_logo_concept_{i}.svg')
    with open(f'amisana_logo_concept_{i}.svg', 'w') as f:
        f.write(svg_string)
    png_image = create_png_logo(svg_string)
    png_image.save(f'amisana_logo_concept_{i}.png', 'PNG')

print("SVG and PNG logo concepts have been created and saved.")