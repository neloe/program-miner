document.getElementById('test').innerHTML='<p>Hello world!</p>'
fetch('./prereqs.json').then(response => response.json())
  .then(data =>  {
    let G = new jsnx.DiGraph();
    G.addNodesFrom(Object.keys(data))
    console.log(Object.keys(data))
  });
