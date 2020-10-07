let G = new jsnx.DiGraph();
fetch('./prereqs.json').then(response => response.json())
  .then(data =>  {

    G.addNodesFrom(Object.keys(data))
    for (c in data)
    {
      if (data[c].length > 0)
        for (pr in data[c])
          G.addEdge(pr, c)
    }
    console.log(G.edges())
    document.getElementById('test').innerHTML='<p>'+G.edges()+'</p>'
  });
