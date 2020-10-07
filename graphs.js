document.getElementById('test').innerHTML='<p>Hello world!</p>'
fetch('./prereqs.json').then(response => response.json())
  .then(data => console.log(data));
