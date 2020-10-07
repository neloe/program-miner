const someColors = d3.scale.category20b();
function createArcDiagram (data)
{
  let nodes = Object.keys(parsed)
  let links = new Array()
  for (c in parsed)
  {
    for (pr in parsed[c])
    links.push({source: parsed[c][pr], target: c})
  }

  d3.layout.arcDiagram()
  .nodes(nodes)
  .links(links)
  .nodeID(d=>d)

  arcDiagram();

  let canvas = d3.select('svg#canvas')
  .append('g').attr('id', 'argG')
  .attr('transform', 'translate(25, 0)')

  canvas.selectAll('path')
    .data(links)
    .enter()
    .append('path')
    .attr('class', 'arc')
    .style('stroke', d=>)
}
