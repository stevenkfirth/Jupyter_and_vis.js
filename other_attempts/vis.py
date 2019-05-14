
from IPython.display import Javascript
from uuid import uuid4
import json

def network(nodes=None,edges=None,height=300):

    id1=uuid4()

    data="""

    require.config(
            {paths:
                {vis: '//cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min'}
            });

    require(['vis'],function(vis){
        // create an array with nodes
            var nodes = new vis.DataSet(%(nodes)s);

            // create an array with edges
            var edges = new vis.DataSet(%(edges)s);

            // create a network
            var container = document.getElementById('%(id1)s');

            // provide the data in the vis format
            var data = {
                nodes: nodes,
                edges: edges
            };
            var options = {
                width:'100%%',
                height:%(height)s,
                nodes:{shape:'circle',size:14},
                edges:{arrows:'to',font:{size:10}}
            };

            // initialize your network!
            var network = new vis.Network(container, data, options);
        });

    element.append('<div id="%(id1)s"> </div>');
    """ % {'id1':id1,'nodes':json.dumps(nodes),'edges':json.dumps(edges),
           'height':height}

    js=Javascript(data=data,
                  css='https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css')

    return js



def network_test():

    id1=uuid4()

    data="""

    require.config(
            {paths:
                {vis: '//cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min'}
            });

    require(['vis'],function(vis){
        // create an array with nodes
            var nodes = new vis.DataSet([
                {id: 1, label: 'Node 1', title:'test'},
                {id: 2, label: 'Node 2', title:'test'},
                {id: 3, label: 'Node 3', title:'test'},
                {id: 4, label: 'Node 4', title:'test'},
                {id: 5, label: 'Node 5', title:'test'}
            ]);

            // create an array with edges
            var edges = new vis.DataSet([
                {from: 1, to: 3},
                {from: 1, to: 2},
                {from: 2, to: 4},
                {from: 2, to: 5}
            ]);

            // create a network
            var container = document.getElementById('%(id1)s');

            // provide the data in the vis format
            var data = {
                nodes: nodes,
                edges: edges
            };
            var options = {};

            // initialize your network!
            var network = new vis.Network(container, data, options);
        });

    element.append('<div id="%(id1)s"> </div>');
    """ % {'id1':id1}

    js=Javascript(data=data,
                  css='https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css')

    return js

    

