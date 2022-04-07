import networkx as nx
from pathlib import Path
import json

# tiedostopohja, johon verkkodata tungetaan
html_template = '''
<!doctype html>
<html>

<head>
<title>Graph visualization</title>
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.20.0/cytoscape.min.js"></script>
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
        'target-arrow-shape': '[TARGET-ARROW-SHAPE]',
        'width': 4,
        'line-color': '#ddd'
      })
    .selector('edge[[WEIGHT]]')
      .style({
        'label': 'data([WEIGHT])'
      })
    .selector('.highlighted')
      .style({
        'background-color': '#61bffc',
        'line-color': '#61bffc',
        'transition-property': 'background-color, line-color',
        'transition-duration': '0.5s'
      }),
  elements: [ELEMENTS],
  data: [DATA],
  layout: {
    name: '[LAYOUT]',
    directed: [DIRECTED],
    padding: 10
  }
});

// animointiin
var i = 0;
var highlightNext = function() {
    if (i < cy.data('highlight').length) {
        myid = cy.data('highlight')[i];
        ele = cy.getElementById(myid);
        ele.addClass('highlighted');
        i += 1;
        setTimeout(highlightNext, [FREQUENCY]);
    }
}

[ANIMATE]

</script>
</body>

</html>
''' 

# apufunktio
def fix_highlight_edges(highlight_data, directed):

    # tyhjälle ei tehdä mitään
    if not highlight_data or 'highlight' not in highlight_data:
        return {}

    highlight_edges = []

    for i, e in enumerate(highlight_data['highlight']):
        e = (e[0],e[1]) if directed else sorted((e[0],e[1]))
        highlight_edges.append('{},{}'.format(e[0],e[1]))

    return {'highlight': highlight_edges}


'''
create_html

ei palauta mitään

tunkee verkkodatan G html-pohjaan

ulostaa html-tiedoston (mahdollisesti animoidun)

offset = kauanko odotetaan ennen animoinnin aloitusta

frequency = kahden animaatioaskeleen välinen aika
'''
def create_html(G, outpath, weight='weight', animate=False, offset=5000, frequency=2000):

    # onko suunnattu vai ei
    directed = isinstance(G, nx.DiGraph)

    # luetaan verkko cytoscape-muodossa
    cyto_dict_all = nx.readwrite.json_graph.cytoscape_data(G)

    # noodit ja linkit
    cyto_dict_elements = cyto_dict_all['elements']

    # verkkoattribuutit (highlight-järjestys)
    cyto_dict_data = dict(cyto_dict_all['data'])

    # vähän joutuu vääntääN jotta tulee kaikki oikein
    cyto_dict_data = fix_highlight_edges(cyto_dict_data, directed)

    # väännetään verkkodata cytoscape.js:n ymmärtämään muotoon
    # cytoscape (vanha) on eri asia kuin cytoscape.js
    for node in cyto_dict_elements['nodes']:
        del node['data']['name'], node['data']['value']
    for edge in cyto_dict_elements['edges']:
        edge['data']['id'] = '{},{}'.format(edge['data']['source'],edge['data']['target'])
        if weight in edge['data']:
            edge['data'][weight] = str(edge['data'][weight])

    # muokataan pohjaa ja kirjoitetaan tiedosto
    html_output = html_template.replace('[ELEMENTS]', f'{json.dumps(cyto_dict_elements)}')
    html_output = html_output.replace('[DATA]', f'{json.dumps(cyto_dict_data)}' if animate else '{}')

    html_output = html_output.replace('[DIRECTED]', 'true' if directed else 'false')
    html_output = html_output.replace('[TARGET-ARROW-SHAPE]', 'triangle' if directed else 'none')
    html_output = html_output.replace('[LAYOUT]', 'circle' if directed else 'cose')
    html_output = html_output.replace('[WEIGHT]', weight)
    html_output = html_output.replace('[FREQUENCY]', str(frequency))
    html_output = html_output.replace('[ANIMATE]', f'setTimeout(highlightNext, {offset});' if animate else '')
    with open(Path(outpath), 'w') as handle:
        handle.write(html_output)
