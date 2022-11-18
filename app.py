from flask import Flask,request, render_template
from solution import get_pixel_coordinates
app = Flask(__name__)

def validate_input(image_dimensions, corner_points):
    if len(image_dimensions) != 2:
        return False
    elif type(image_dimensions[0]) != int or type(image_dimensions[1]) != int:
        return False
    elif image_dimensions[0] <= 1 or image_dimensions[1] <= 1:
        return False
    elif len(image_dimensions) != 2:
        return False
    
    if len(corner_points) != 4:
        return False
    elif type(corner_points) != list:
        return False
    elif type(corner_points[0]) != tuple or type(corner_points[1]) != tuple or type(corner_points[2]) != tuple or type(corner_points[3]) != tuple:
        return False
    elif len(corner_points[0]) != 2 or len(corner_points[1]) != 2 or len(corner_points[2]) != 2 or len(corner_points[3]) != 2:
        return False
    return True


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        image_dimensions = eval(request.form.get('image_dimensions'))
        corner_points = eval(request.form.get('corner_points'))
        if not validate_input(image_dimensions, corner_points):
            return render_template('index.html', result="Invalid input")
        res = 'Result for input: image_dimensions = {}, corner_points = {} is: {}'.format(image_dimensions, corner_points, get_pixel_coordinates(image_dimensions, corner_points))
        return render_template('index.html', result=res)
    if request.method == 'GET':
        return render_template('index.html')

