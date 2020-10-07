document.getElementById('test').innerHTML='<p>Hello world!</p>'
let G = new jsnx.DiGraph();
fetch('./prereqs.json').then(response => response.json())
  .then(data =>  {

    G.addNodesFrom(Object.keys(data))
    console.log(Object.keys(data))
    console.log('hello world?')
  });
