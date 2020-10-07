let G = new jsnx.DiGraph();
fetch('./prereqs.json').then(response => response.json())
  .then(data =>  {

    G.addNodesFrom(Object.keys(data))
    for (c in data)
    {
      for (pr in data[c])
        G.addEdge(pr, c)
    }
    document.getElementById('test').innerHTML='<p>'.G.edges().'</p>'
  });
