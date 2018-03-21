QUnit.module("Example", {

    //QUnit's version of "setup"
    //Create a dummy graph to use during testing
    before: function() {
        console.log("setup running");
        this.expectedVisible;
        this.NumInitialNodes = 8;
        this.NumInitialEdges = 6;

        this.nodes = new vis.DataSet([
            {id: 1, label: '1'},
            {id: 2, label: '2'},
            {id: 3, label: '3'},
            {id: 4, label: '4'},
            {id: 11, label: '11'},
            {id: 12, label: '12'},
            {id: 13, label: '13'},
            {id: 14, label: '14'},
        ]);
        this.edges = new vis.DataSet([
            {from: 1, to: 2},
            {from: 2, to: 3},
            {from: 3, to: 4},
            {from: 11, to: 12},
            {from: 12, to: 13},
            {from: 13, to: 14},
        ]);

        this.options = {};
        this.container = document.getElementById('mynetwork');
        this.data = {
            nodes: this.nodes,
            edges: this.edges
        };

        this.network = new vis.Network(this.container, this.data, this.options);
    }
});

//Test the number of nodes in the graph created in "begin"
QUnit.test("Number of Nodes", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialNodes;
    }
    console.log("Nodes in graph: ", this.network.body.data.nodes);
    assert.equal(this.network.body.data.nodes.length, this.NumInitialNodes, "Number of nodes should be 8");
    assert.equal(this.network.body.nodeIndices.length, this.expectedVisible, "Number of nodes should be 8");

});

//Test the number of edges in the graph created in "begin"
QUnit.test("Number of Edges", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialEdges;
    }
    console.log("Edges in graph: ", Object.keys(this.network.body.edges));
    assert.equal(Object.keys(this.network.body.data.edges).length, this.NumInitialEdges, "Number of edges should be 6");
    assert.equal(this.network.body.edgeIndices.length, this.NumInitialEdges, "Number of edges should be 6");

});
