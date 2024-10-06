import svgwrite
import math
import random
import os
from cairosvg import svg2png

def create_svg_logo(draw_function, size=(300, 300), filename='logo.svg'):
    dwg = svgwrite.Drawing(filename, size=size)
    draw_function(dwg)
    return dwg

def save_svg_and_png(svg_drawing, base_filename):
    # Save SVG
    svg_filename = f"{base_filename}.svg"
    svg_drawing.save()
    print(f"Saved SVG: {svg_filename}")

    # Save PNG
    png_filename = f"{base_filename}.png"
    svg2png(bytestring=svg_drawing.tostring(), write_to=png_filename, output_width=300, output_height=300)
    print(f"Saved PNG: {png_filename}")

def concept_1(dwg):
    # Abstract network of connections
    group = dwg.g(fill='none', stroke='black', stroke_width=2)
    for i in range(20):
        x1, y1 = random.randint(0, 300), random.randint(0, 300)
        x2, y2 = random.randint(0, 300), random.randint(0, 300)
        group.add(dwg.line((x1, y1), (x2, y2)))
    for i in range(10):
        cx, cy = random.randint(0, 300), random.randint(0, 300)
        group.add(dwg.circle(center=(cx, cy), r=5, fill='black'))
    dwg.add(group)

def concept_2(dwg):
    # Fractal tree representing growth and complexity
    def draw_branch(x1, y1, angle, depth):
        if depth > 0:
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
            dwg.add(dwg.line((x1, y1), (x2, y2), stroke='black', stroke_width=depth))
            draw_branch(x2, y2, angle - 20, depth - 1)
            draw_branch(x2, y2, angle + 20, depth - 1)
    
    draw_branch(150, 300, -90, 9)

def concept_3(dwg):
    # Dynamic, interlocking shapes
    shapes = dwg.g(fill='none', stroke='black', stroke_width=2)
    shapes.add(dwg.path(d="M150,50 L250,150 L150,250 L50,150 Z"))
    shapes.add(dwg.circle(center=(150, 150), r=70))
    shapes.add(dwg.rect(insert=(100, 100), size=(100, 100)))
    dwg.add(shapes)

def concept_4(dwg):
    # Abstract representation of AI and human collaboration
    brain = dwg.path(d="M100,150 C100,100 200,100 200,150 C200,200 100,200 100,150", 
                     fill='none', stroke='black', stroke_width=2)
    circuit = dwg.g(fill='none', stroke='black', stroke_width=2)
    for i in range(5):
        circuit.add(dwg.line((50+i*40, 50), (50+i*40, 250)))
    for i in range(5):
        circuit.add(dwg.line((50, 50+i*40), (250, 50+i*40)))
    dwg.add(brain)
    dwg.add(circuit)

# Ensure output directory exists
output_dir = "logo_output"
os.makedirs(output_dir, exist_ok=True)

# Create and save SVG and PNG versions of each concept
concepts = [concept_1, concept_2, concept_3, concept_4]
for i, concept in enumerate(concepts, 1):
    base_filename = os.path.join(output_dir, f'amisana_advanced_logo_concept_{i}')
    svg_drawing = create_svg_logo(concept, filename=f'{base_filename}.svg')
    save_svg_and_png(svg_drawing, base_filename)

print("Advanced SVG and PNG logo concepts have been created and saved.")