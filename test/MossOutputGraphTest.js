QUnit.module("Graph Example", {

    //QUnit's version of "setup"
    //Create a dummy graph to use during testing
    before: function() {
        console.log("setup running");
        this.expectedVisible;
        this.edges = new vis.DataSet();
        this.nodes = new vis.DataSet();
        this.network = null;
        this.container = null;
        this.options = null;
        this.slider = null;

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
            {from: 1, to: 2, value: 2},
            {from: 2, to: 3, value: 17},
            {from: 3, to: 4, value: 33},
            {from: 11, to: 12, value: 4},
            {from: 12, to: 13, value: 26},
            {from: 13, to: 14, value: 61},
        ]);

        console.log("Nodes: ", this.nodes);
        console.log("Edges: ", this.edges);

        this.options = {};
        this.container = document.getElementById('mynetwork');
        this.data = {
            nodes: this.nodes,
            edges: this.edges
        };

        this.network = new vis.Network(this.container, this.data, this.options);

        this.slider = document.getElementById("chosenRange");
        this.slider.value = 1;

    }
});

//Test the number of nodes in the graph created in "begin"
QUnit.test("Number of Nodes in Node Dataset", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialNodes;
    }
    console.log("Nodes in graph: ", this.network.body.data.nodes);
    assert.equal(this.network.body.nodeIndices.length, this.expectedVisible, "Expecting 8 nodes");

});

//Test the number of node indices in the graph created in "begin"
QUnit.test("Number of Node Indices in NodeIndex Dataset", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialNodes;
    }
    console.log("NodeIndexes in graph: ", this.network.body.data.nodes);
    assert.equal(this.network.body.nodeIndices.length, this.expectedVisible, "Expecting 8 node indices");

});

//Test the number of edges in the graph created in "begin"
QUnit.test("Number of Edges", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialEdges;
    }
    console.log("Edges in Graph: ", Object.keys(this.network.body.edges));
    assert.equal(Object.keys(this.network.body.data.edges).length, this.NumInitialEdges, "Expecting 6 edges");

});

//Test the number of edge indices in the graph created in "begin"
QUnit.test("Number of Edge Indices in EdgeIndex Dataset", function (assert){

    if (this.expectedVisible === undefined){
        this.expectedVisible = this.NumInitialEdges;
    }
    console.log("Edge Indices in Graph: ", Object.keys(this.network.body.edges));
    assert.equal(this.network.body.edgeIndices.length, this.NumInitialEdges, "Expecting 8 edge indices");

});

QUnit.test("Slider - All Edges Visible", function(assert){
    var oe = new vis.DataSet(this.edges);
    var visible = true;
    for(var i=0; i<oe.length; i++){
        if(oe[i].hidden == true){
            visible = false;
        }
    }

    assert.ok(true, visible, "When slider value is 1, all nodes are visible");
})

QUnit.test("Slider Bar - Single Test", function(assert){
    this.slider.value = 25;
    var e = changeEdges(this.slider.value);

    console.log("ecopy: ", e);

    var testHidden = true;
    for(var i=0; i<e.length; i++){
        if(parseInt(e[i].value) < this.slider.value){
            if(e[i].hidden == false){
                testHidden = false;
            }
        }
        else{
            if(e[i].hidden == true){
                testHidden = false;
            }
        }
    }

    this.slider.value = 1;
    assert.ok(true, testHidden, "Edges with values < 25 should now be marked as hidden");
});

function changeEdges(value){
    var oe = new vis.DataSet(this.edges);
    for (var i = 0; i < oe.length; i++){
        if (parseInt(oe[i].value) < value) {
            oe[i].hidden = true
        }
        else {
            oe[i].hidden = false
        }
    }
    return oe;
}