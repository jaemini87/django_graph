from django.shortcuts import render

from matplotlib.pyplot import figure, title, bar
from matplotlib.figure import Figure
import matplotlib.path as mpath
import matplotlib.patches as mpatches

import matplotlib.pyplot as plt
import matplotlib
import numpy as np  
import mpld3
from .models import CustomModel







def post_list(request):
    return render(request, 'blog/post_list.html', {})

graph = {'directed': False,
 'graph': {'name': "Zachary's Karate Club"},
'links': [{'source': 0, 'target': 1},
{'source': 0, 'target': 2},
{'source': 0, 'target': 3},
{'source': 0, 'target': 4},
{'source': 0, 'target': 5},
{'source': 0, 'target': 6},
{'source': 0, 'target': 7},
{'source': 0, 'target': 8},
{'source': 0, 'target': 10},
{'source': 0, 'target': 11},
{'source': 0, 'target': 12},
{'source': 0, 'target': 13},
{'source': 0, 'target': 17},
{'source': 0, 'target': 19},
{'source': 0, 'target': 21},
{'source': 0, 'target': 31},
{'source': 1, 'target': 2},
{'source': 1, 'target': 3},
{'source': 1, 'target': 7},
{'source': 1, 'target': 13},
{'source': 1, 'target': 17},
{'source': 1, 'target': 19},
{'source': 1, 'target': 21},
{'source': 1, 'target': 30},
{'source': 2, 'target': 3},
{'source': 2, 'target': 32},
{'source': 2, 'target': 7},
{'source': 2, 'target': 8},
{'source': 2, 'target': 9},
{'source': 2, 'target': 13},
{'source': 2, 'target': 27},
{'source': 2, 'target': 28},
{'source': 3, 'target': 7},
{'source': 3, 'target': 12},
{'source': 3, 'target': 13},
{'source': 4, 'target': 10},
{'source': 4, 'target': 6},
{'source': 5, 'target': 16},
{'source': 5, 'target': 10},
{'source': 5, 'target': 6},
{'source': 6, 'target': 16},
{'source': 8, 'target': 32},
{'source': 8, 'target': 30},
{'source': 8, 'target': 33},
{'source': 9, 'target': 33},
{'source': 13, 'target': 33},
{'source': 14, 'target': 32},
{'source': 14, 'target': 33},
{'source': 15, 'target': 32},
{'source': 15, 'target': 33},
{'source': 18, 'target': 32},
{'source': 18, 'target': 33},
{'source': 19, 'target': 33},
{'source': 20, 'target': 32},
{'source': 20, 'target': 33},
{'source': 22, 'target': 32},
{'source': 22, 'target': 33},
{'source': 23, 'target': 32},
{'source': 23, 'target': 25},
{'source': 23, 'target': 27},
{'source': 23, 'target': 29},
{'source': 23, 'target': 33},
{'source': 24, 'target': 25},
{'source': 24, 'target': 27},
{'source': 24, 'target': 31},
{'source': 25, 'target': 31},
{'source': 26, 'target': 33},
{'source': 26, 'target': 29},
{'source': 27, 'target': 33},
{'source': 28, 'target': 33},
{'source': 28, 'target': 31},
{'source': 29, 'target': 32},
{'source': 29, 'target': 33},
{'source': 30, 'target': 33},
{'source': 30, 'target': 32},
{'source': 31, 'target': 33},
{'source': 31, 'target': 32},
{'source': 32, 'target': 33}],
 'multigraph': False,
'nodes': [{'club': 'Mr. Hi', 'color': 'purple', 'id': 0, 'size': 16},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 1, 'size': 9},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 2, 'size': 10},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 3, 'size': 6},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 4, 'size': 3},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 5, 'size': 4},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 6, 'size': 4},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 7, 'size': 4},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 8, 'size': 5},
{'club': 'Officer', 'color': 'orange', 'id': 9, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 10, 'size': 3},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 11, 'size': 1},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 12, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 13, 'size': 5},
{'club': 'Officer', 'color': 'orange', 'id': 14, 'size': 2},
{'club': 'Officer', 'color': 'orange', 'id': 15, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 16, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 17, 'size': 2},
{'club': 'Officer', 'color': 'orange', 'id': 18, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 19, 'size': 3},
{'club': 'Officer', 'color': 'orange', 'id': 20, 'size': 2},
{'club': 'Mr. Hi', 'color': 'purple', 'id': 21, 'size': 2},
{'club': 'Officer', 'color': 'orange', 'id': 22, 'size': 2},
{'club': 'Officer', 'color': 'orange', 'id': 23, 'size': 5},
{'club': 'Officer', 'color': 'orange', 'id': 24, 'size': 3},
{'club': 'Officer', 'color': 'orange', 'id': 25, 'size': 3},
{'club': 'Officer', 'color': 'orange', 'id': 26, 'size': 2},
{'club': 'Officer', 'color': 'orange', 'id': 27, 'size': 4},
{'club': 'Officer', 'color': 'orange', 'id': 28, 'size': 3},
{'club': 'Officer', 'color': 'orange', 'id': 29, 'size': 4},
{'club': 'Officer', 'color': 'orange', 'id': 30, 'size': 4},
{'club': 'Officer', 'color': 'orange', 'id': 31, 'size': 6},
{'club': 'Officer', 'color': 'orange', 'id': 32, 'size': 12},
{'club': 'Officer', 'color': 'orange', 'id': 33, 'size': 17}]}

class NetworkXD3ForceLayout(mpld3.plugins.PluginBase):
    """A NetworkX to D3 Force Layout Plugin"""

    JAVASCRIPT = """
    mpld3.register_plugin("networkxd3forcelayout", NetworkXD3ForceLayoutPlugin);
    NetworkXD3ForceLayoutPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    NetworkXD3ForceLayoutPlugin.prototype.constructor = NetworkXD3ForceLayoutPlugin;
    NetworkXD3ForceLayoutPlugin.prototype.requiredProps = ["graph",
    "ax_id",];
    NetworkXD3ForceLayoutPlugin.prototype.defaultProps = { coordinates: "data",
     gravity: 1,
    charge: -30,
     link_strength: 1,
    friction: 0.9,
     link_distance: 20,
    maximum_stroke_width: 2,
     minimum_stroke_width: 1,
    nominal_stroke_width: 1,
     maximum_radius: 10,
    minimum_radius: 1,
     nominal_radius: 5,
     };
     function NetworkXD3ForceLayoutPlugin(fig, props){
     mpld3.Plugin.call(this, fig, props);
     };
     var color = d3.scale.category20();
     NetworkXD3ForceLayoutPlugin.prototype.zoomScaleProp = function (nominal_prop, minimum_prop, maximum_prop) {
     var zoom = this.ax.zoom;
     scalerFunction = function() {
     var prop = nominal_prop;
     if (nominal_prop*zoom.scale()>maximum_prop) prop = maximum_prop/zoom.scale();
     if (nominal_prop*zoom.scale()<minimum_prop) prop = minimum_prop/zoom.scale();
     return prop
     }
     return scalerFunction;
     }
     NetworkXD3ForceLayoutPlugin.prototype.setupDefaults = function () {
     this.zoomScaleStroke = this.zoomScaleProp(this.props.nominal_stroke_width,
     this.props.minimum_stroke_width,
     this.props.maximum_stroke_width)
     this.zoomScaleRadius = this.zoomScaleProp(this.props.nominal_radius,
     this.props.minimum_radius,
     this.props.maximum_radius)
     }
     NetworkXD3ForceLayoutPlugin.prototype.zoomed = function() {
     this.tick()
     }
     NetworkXD3ForceLayoutPlugin.prototype.draw = function(){
     plugin = this
     brush = this.fig.getBrush();
     DEFAULT_NODE_SIZE = this.props.nominal_radius;
     var height = this.fig.height
     var width = this.fig.width
     var graph = this.props.graph
     var gravity = this.props.gravity.toFixed()
     var charge = this.props.charge.toFixed()
     var link_distance = this.props.link_distance.toFixed()
     var link_strength = this.props.link_strength.toFixed()
     var friction = this.props.friction.toFixed()
     this.ax = mpld3.get_element(this.props.ax_id, this.fig)
     var ax = this.ax;
     this.ax.elements.push(this)
     ax_obj = this.ax;
     var width = d3.max(ax.x.range()) - d3.min(ax.x.range()),
     height = d3.max(ax.y.range()) - d3.min(ax.y.range());
     var color = d3.scale.category20();
     this.xScale = d3.scale.linear().domain([0, 1]).range([0, width]) // ax.x;
     this.yScale = d3.scale.linear().domain([0, 1]).range([height, 0]) // ax.y;
     this.force = d3.layout.force()
     .size([width, height]);
     this.svg = this.ax.axes.append("g");
     for(var i = 0; i < graph.nodes.length; i++){
     var node = graph.nodes[i];
     if (node.hasOwnProperty('x')) {
     node.x = this.ax.x(node.x);
     }
     if (node.hasOwnProperty('y')) {
     node.y = this.ax.y(node.y);
     }
     }
     this.force
     .nodes(graph.nodes)
     .links(graph.links)
     .linkStrength(link_strength)
     .friction(friction)
     .linkDistance(link_distance)
     .charge(charge)
     .gravity(gravity)
     .start();
     this.link = this.svg.selectAll(".link")
     .data(graph.links)
     .enter().append("line")
     .attr("class", "link")
     .attr("stroke", "black")
     .style("stroke-width", function (d) { return Math.sqrt(d.value); });
     this.node = this.svg.selectAll(".node")
     .data(graph.nodes)
     .enter().append("circle")
     .attr("class", "node")
     .attr("r", function(d) {return d.size === undefined ? DEFAULT_NODE_SIZE : d.size ;})
     .style("fill", function (d) { return d.color; });
     this.node.append("title")
     .text(function (d) { return d.name; });
     this.force.on("tick", this.tick.bind(this));
     this.setupDefaults()
     };
     NetworkXD3ForceLayoutPlugin.prototype.tick = function() {
     this.link.attr("x1", function (d) { return this.ax.x(this.xScale.invert(d.source.x)); }.bind(this))
    .attr("y1", function (d) { return this.ax.y(this.yScale.invert(d.source.y)); }.bind(this))
     .attr("x2", function (d) { return this.ax.x(this.xScale.invert(d.target.x)); }.bind(this))
    .attr("y2", function (d) { return this.ax.y(this.yScale.invert(d.target.y)); }.bind(this));
    this.node.attr("transform", function (d) {
    return "translate(" + this.ax.x(this.xScale.invert(d.x)) + "," + this.ax.y(this.yScale.invert(d.y)) + ")";
    }.bind(this)
    );
    }
    """

    def __init__(self, graph, ax,
        gravity=1,
        link_distance=20,
        charge=-30,
        node_size=5,
        link_strength=1,
        friction=0.9):

        self.dict_ = {"type": "networkxd3forcelayout",
            "graph": graph,
            "ax_id": mpld3.utils.get_id(ax),
            "gravity": gravity,
            "charge": charge,
            "friction": friction,
            "link_distance": link_distance,
            "link_strength": link_strength,
            "nominal_radius": node_size}
class LinkedDragPlugin(mpld3.plugins.PluginBase):
    JAVASCRIPT = r"""
    mpld3.register_plugin("drag", DragPlugin);
    DragPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    DragPlugin.prototype.constructor = DragPlugin;
    DragPlugin.prototype.requiredProps = ["idpts", "idline", "idpatch"];
    DragPlugin.prototype.defaultProps = {}
    function DragPlugin(fig, props){
    mpld3.Plugin.call(this, fig, props);
    };

    DragPlugin.prototype.draw = function(){
    var patchobj = mpld3.get_element(this.props.idpatch, this.fig);
    var ptsobj = mpld3.get_element(this.props.idpts, this.fig);
    var lineobj = mpld3.get_element(this.props.idline, this.fig);

    var drag = d3.behavior.drag()
    .origin(function(d) { return {x:ptsobj.ax.x(d[0]),
    y:ptsobj.ax.y(d[1])}; })
    .on("dragstart", dragstarted)
    .on("drag", dragged)
    .on("dragend", dragended);

    lineobj.path.attr("d", lineobj.datafunc(ptsobj.offsets));
    patchobj.path.attr("d", patchobj.datafunc(ptsobj.offsets,
    patchobj.pathcodes));
    lineobj.data = ptsobj.offsets;
    patchobj.data = ptsobj.offsets;

    ptsobj.elements()
     .data(ptsobj.offsets)
    .style("cursor", "default")
     .call(drag);

     function dragstarted(d) {
     d3.event.sourceEvent.stopPropagation();
     d3.select(this).classed("dragging", true);
     }

     function dragged(d, i) {
     d[0] = ptsobj.ax.x.invert(d3.event.x);
     d[1] = ptsobj.ax.y.invert(d3.event.y);
     d3.select(this)
     .attr("transform", "translate(" + [d3.event.x,d3.event.y] + ")");
     lineobj.path.attr("d", lineobj.datafunc(ptsobj.offsets));
     patchobj.path.attr("d", patchobj.datafunc(ptsobj.offsets,
     patchobj.pathcodes));
     }

     function dragended(d, i) {
     d3.select(this).classed("dragging", false);
     }
     }

     mpld3.register_plugin("drag", DragPlugin);
     """

    def __init__(self, points, line, patch):
        if isinstance(points, matplotlib.lines.Line2D):
            suffix = "pts"
        else:
            suffix = None

        self.dict_ = {"type": "drag",
        "idpts": mpld3.utils.get_id(points, suffix),
        "idline": mpld3.utils.get_id(line),
        "idpatch": mpld3.utils.get_id(patch)}

def view_chart(request, instance_id=1):
    matplotlib.use('Agg')
    Fig = Figure(figsize=(12,18))
    Fig1 = Fig.add_subplot(311)
    Fig2 = Fig.add_subplot(312)
    Fig3 = Fig.add_subplot(313)
    #Fig1,ax = Fig.add_subplot(subplot_kw=dict(axisbg='#EEEEEE'))
    N = 100

    scatter = Fig1.scatter(np.random.normal(size=N),
    np.random.normal(size=N),
    c=np.random.random(size=N),
    s=1000 * np.random.random(size=N),
    alpha=0.3,
    cmap=plt.cm.jet)
    Fig1.grid(color='white', linestyle='solid')

    #Fig1.set_title("Scatter Plot (with tooltips!)", size=20)
    Fig1.set_title("Jaemin Cho Graph Test", size=40)

    labels = ['point {0}'.format(i + 1) for i in range(N)]
    Path = mpath.Path
    path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
    Fig3.add_patch(patch)

    # plot control points and connecting lines
    x, y = zip(*path.vertices[:-1])
    points = Fig3.plot(x, y, 'go', ms=10)
    line = Fig3.plot(x, y, '-k')

    #Fig3.grid(True, color='gray', alpha=0.5)
    Fig3.axis('equal')
    Fig3.set_title("Drag Points to Change Path", fontsize=40)

    mpld3.plugins.connect(Fig, LinkedDragPlugin(points[0], line[0], patch))
    mpld3.plugins.connect(Fig, NetworkXD3ForceLayout(graph,
        Fig2,
        gravity=.5,
        link_distance=20,
        charge=-600,
        friction=1
        )
    )


    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(Fig, tooltip)
    fig_html = mpld3.fig_to_html(Fig)
    return render(request,'blog/post_list.html',
    {'figure': fig_html,})

    #mpld3.show()



def view_charts(request, instance_id=1):
    matplotlib.use('Agg')
    #mpl_figure = figure(1, figsize=(6, 6))
    Fig = Figure(figsize=(6,6))
    Fig1 = Fig.add_subplot(211)
    Fig2 = Fig.add_subplot(212)
    xvalues = range(5)# the x locations for the groups
    try:    
        model_object = CustomModel.objects.get(pk=instance_id)
        yvalues = model_object.get_data()
    except CustomModel.DoesNotExist:
        yvalues = np.random.random_sample(5)
    width = 0.5# the width of the bars
    #title(_(u'Custom Bar Chart'))
    Fig1.bar(xvalues, yvalues, width)
    Fig2.bar(xvalues, yvalues, width)
    Fig2.get_xaxis().set_visible(False)
    Fig2.get_yaxis().set_visible(False)
    fig_html = mpld3.fig_to_html(Fig)
    return render(request,'blog/post_list.html',
        {'figure': fig_html,})

# Create your views here.
