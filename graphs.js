// for reference: https://bl.ocks.org/emeeks/8d75da95d1e78cd08899
let data = new Object()
chart = {
  const svg = d3.select("#canvas");

  svg.append("style").text(`

.hover path {
  stroke: #ccc;
}

.hover text {
  fill: #ccc;
}

.hover g.primary text {
  fill: black;
  font-weight: bold;
}

.hover g.secondary text {
  fill: #333;
}

.hover path.primary {
  stroke: #333;
  stroke-opacity: 1;
}

`);

fetch('./prereqs.json').then(response => response.json())
  .then(parsed =>  {
    data.nodes = Object.keys(parsed)
    data.links = new Array()
    for (c in parsed)
    {
      for (pr in parsed[c])
      data.links.push({source: parsed[c][pr], target: c})
    }
  });
