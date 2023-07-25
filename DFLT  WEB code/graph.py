from bokeh.plotting import figure, show
from bokeh.models import HoverTool, CustomJS, ColumnDataSource
from PIL import Image
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return "data:image/png;base64," + base64.b64encode(image_file.read()).decode('utf-8')

def generate_plot(radii, percentages, images):
    x = [i for i in range(1, len(radii) + 1)]
    y = radii

    source = ColumnDataSource(data=dict(
        x=x,
        y=y,
        images=images,
        percentages=percentages
    ))

    p = figure(title="hirox result", plot_width=600, plot_height=400)
    p.circle('x', 'y', size=10, color="green", source=source)

    hover = HoverTool(tooltips="""
        <div>
            <div>
                <img
                    src="@images" height="200" alt="@percentages" width="200"
                    style="float: left; margin: 0px 15px 15px 0px;"
                ></img>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@percentages</span>
            </div>
        </div>
    """)

    p.add_tools(hover)

    tap_js = CustomJS(args=dict(source=source), code="""
        var images = source.data['images'];
        var index = source.selected.indices[0];
        var dataURL = images[index];
        var link = document.createElement('a');
        link.href = dataURL;
        link.download = 'image.png';
        link.target = '_blank';
        link.click();
    """)

    p.js_on_event('tap', tap_js)

    show(p)

radii = [3, 5, 8]
percentages = [20, 30, 25]
images = [
    'DFLT  WEB code/templates/image1.jpg',
    'DFLT  WEB code/temp/ates/image2.jpg',
    'DFLT  WEB code/templates/image3.jpg'
]


