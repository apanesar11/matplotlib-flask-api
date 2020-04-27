import io
from flask import Response, Flask, request, jsonify
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from utils import create_line_graph

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello there'


@app.route('/graph/line', methods=['POST'])
def line_chart():
    try:
        data = request.json
        fig = create_line_graph(data)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    except Exception as err:
        data = {"error": str(err)}
        return jsonify(data)


if __name__ == '__main__':
    app.run()
