let year = '2022-2023'
let program = 'Computer Science'
const programs = {'Computer Science': 'csprereqs_arc.json',
'Data Science and Informatics': 'dsiprereqs_arc.json',
'Digital Media': 'dmprereqs_arc.json',
'Cybersecurity': 'cyberprereqs_arc.json',
'Business Education': 'busedprereqs_arc.json',
'Management Information Systems': 'misprereqs_arc.json',
'Business Technology': 'bustechprereqs_arc.json'}
const years = ['2023-2024', '2022-2023', '2021-2022', '2020-2021']
for (prog in programs)
{
    let b = document.createElement('button')
    b.classList.add('dropdown-item')
    b.setAttribute('type', 'button')
    b.setAttribute('onclick', 'change_program("'+prog+'")')//'_showdeps("'+year + '/'+programs[prog]+'", "'+prog+'")')
    b.innerHTML=prog
    document.getElementById('program-menu').appendChild(b)
}

for (y of years)
{
    let b = document.createElement('button')
    b.classList.add('dropdown-item')
    b.setAttribute('type', 'button')
    b.setAttribute('onclick', 'change_year("'+y+'")')//'_showdeps("'+year + '/'+programs[prog]+'", "'+prog+'")')
    b.innerHTML=y
    document.getElementById('catalog-year').appendChild(b)
}

document.getElementById("yearMenuButton").innerHTML=year
document.getElementById("progMenuButton").innerHTML=program

_showdeps(year + '/'+programs[program], program)

function change_year(y)
{
    year = y
    document.getElementById("yearMenuButton").innerHTML=year
    _showdeps(year + '/'+programs[program], program)
}

function change_program(p)
{
    program = p
    document.getElementById("progMenuButton").innerHTML=program
    console.log(prog + " " + programs[p])
    _showdeps(year + '/'+programs[program], program)
}
