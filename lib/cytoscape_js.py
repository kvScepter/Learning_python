import networkx as nx
from pathlib import Path
import json

# tiedostopohja
html_template = '''<!doctype html>
<html>

<head>
<style>
body { 
  font: 14px helvetica neue, helvetica, arial, sans-serif;
}
#cy {
  height: 100%;
  width: 100%;
  position: absolute;
  left: 0;
  top: 0;
}
</style>
<meta charset="utf-8" />
<meta name="viewport" content="user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, minimal-ui"/>
<title>Bruteforce-color test</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.18.1/cytoscape.min.js"></script>
</head>
<body>
<div id="cy"></div>
<script>
var cy = cytoscape({
  container: document.getElementById('cy'),

  boxSelectionEnabled: false,
  autounselectify: true,

  style: cytoscape.stylesheet()
    .selector('node')
      .style({
        'content': 'data(id)',
        'label': 'data(id)',
          "text-halign": "center",
          "text-valign": "center",
          width: "30px",
          height: "30px",
          color: "blue"
      })
    .selector('edge')
      .style({
        'curve-style': 'bezier',
        'width': 4,
        // 'label': 'data(weight)',
        'line-color': '#ddd'
      })
    .selector('.highlighted')
      .style({
        'background-color': '#61bffc',
        'line-color': '#61bffc',
        'transition-property': 'background-color, line-color',
        'transition-duration': '0.5s'
      }),
  elements: [ELEMENTS],
  layout: {
    name: 'cose',
    directed: false,
    padding: 10
  }
});
for (node of cy.elements().nodes()) {
    node.style('color', node.data().color)
}
</script>
</body>
</html>
''' 

# värikartta
colormap = [
    "FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", "00FFFF", "000000",
    "800000", "008000", "000080", "808000", "800080", "008080", "808080",
    "C00000", "00C000", "0000C0", "C0C000", "C000C0", "00C0C0", "C0C0C0",
    "400000", "004000", "000040", "404000", "400040", "004040", "404040",
    "200000", "002000", "000020", "202000", "200020", "002020", "202020",
    "600000", "006000", "000060", "606000", "600060", "006060", "606060",
    "A00000", "00A000", "0000A0", "A0A000", "A000A0", "00A0A0", "A0A0A0",
    "E00000", "00E000", "0000E0", "E0E000", "E000E0", "00E0E0", "E0E0E0"
]

def create_html(G, outpath):

    colors = G.graph['colors']
    for node in G.nodes():
        G.nodes[node]['color'] = f'#{colormap[colors[node]]}'


    # ensin saatetaan verkkodata cytoscape.js-muotoon
    cyto_dict = nx.readwrite.json_graph.cytoscape_data(G)['elements']
    for node in cyto_dict['nodes']:
        del node['data']['name'], node['data']['value']
    for edge in cyto_dict['edges']:
        edge['data']['id'] = f"{edge['data']['source']}, {edge['data']['target']}"

    html_output = html_template.replace('[ELEMENTS]', f'{json.dumps(cyto_dict)}')
    with open(outpath, 'w') as handle:
        handle.write(html_output)
