const year = '2021-2022'
const programs = {'Computer Science': 'csprereqs_arc.json',
'Data Science and Informatics': 'dsiprereqs_arc.json',
'Digital Media': 'dmprereqs_arc.json',
'Cybersecurity': 'cyberprereqs_arc.json',
'Business Education': 'busedprereqs_arc.json',
'Management Information Systems': 'misprereqs_arc.json',
'Business Technology': 'bustechprereqs_arc.json'}

for (prog in programs)
{
    let b = document.createElement('button')
    b.classList.add('dropdown-item')
    b.setAttribute('type', 'button')
    b.setAttribute('onclick', '_showdeps("'+year + '/'+programs[prog]+'", "'+prog+'")')
    b.innerHTML=prog
    document.getElementById('program-menu').appendChild(b)
}