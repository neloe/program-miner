import json
from os import path, mkdir
from scraperutils import BASE_URL, getAllClasses, makeSoup, getPrereqs
from toposort import toposort
from collections import defaultdict

year = '2022-2023'
programs = ['cs', 'dsi', 'dm', 'cyber', 'bused', 'mis', 'bustech']
program = 'cs'

classfile = path.join(year, 'allclasses.json')
prereqsfile = path.join(year, 'allprereqs.json')
bscsfile = path.join(year, '{}reqs.json'.format(program))
arcfile = path.join(year, '{}prereqs_arc.json'.format(program))

CATPATH = 'Undergraduate-Catalog/School-of-Computer-Science-and-Information-Systems/Computer-Science-and-Information-Systems-44'

urls = {
    'courses': '{}/en/{}/Undergraduate-Catalog/Courses/'.format(BASE_URL, year),
    'cs': '{}/{}/{}/Computer-Science-Comprehensive-Major-6669-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'dsi': '{}/{}/{}/Data-Sciences-and-Informatics-Comprehensive-MajorComputer-Science-Emphasis-73-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'dm': '{}/{}/{}/Digital-Media-Comprehensive-Major-66-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'cyber': '{}/{}/{}/Cybersecurity-Comprehensive-Major-6062-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'bused': '{}/{}/{}/Business-Education-Major-42-hours-BSEd-Secondary-ProgramNo-Minor-Required-Certifies-Grades-912'.format(
        BASE_URL, year, CATPATH),
    'bused-second': '{}/{}/Undergraduate-Catalog/School-of-Education/Professional-Education-Unit/Education-Educational-Leadership-61/Education-BS-Secondary-Program-Certifies-Grades-912'.format(
        BASE_URL, year),
    'mis': '{}/{}/{}/Management-Information-Systems-Comprehensive-Major-75-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'mis-second': '{}/{}/Undergraduate-Catalog/Melvin-D-and-Valorie-G-Booth-School-of-Business/Common-Professional-Component-Requirements-for-Accredited-Business-Programs'.format(
        BASE_URL, year),
    'bustech': '{}/{}/{}/Business-Technology-Comprehensive-Major-72-hours-BSNo-Minor-Required'.format(
        BASE_URL, year, CATPATH),
    'bustech-second': '{}/{}/Undergraduate-Catalog/Melvin-D-and-Valorie-G-Booth-School-of-Business/Common-Professional-Component-Requirements-for-Accredited-Business-Programs'.format(
        BASE_URL, year),
}



##### UPDATE OR READ YEAR CLASS LIST CACHE

if not path.isdir(year):
    mkdir(year)

classinfo = dict()
if not path.exists(classfile):
    print ('Updating class list for ' + year)
    pagesoup = makeSoup(urls['courses'].lower())
    unitlist = pagesoup.find('ul', {'class': 'sc-child-item-links'})
    for u in unitlist.find_all('a'):
        classinfo.update(getAllClasses(BASE_URL+u['href']))
    with open(classfile, 'w') as f:
        json.dump(classinfo, f)
else:
    with open(classfile, 'r') as f:
        classinfo = json.load(f)

##### UPDATE OR READ YEAR CLASS LIST CACHE
reqlist = []
if not path.exists(bscsfile):
    print('Updating '+program+' requirements for ' + year)
    soup = makeSoup(urls[program])
    reqlist = [x.text.split()[1] for x in soup.findAll('a', {'class': 'sc-courselink'}) if len(x.text.split()) > 1]
    if program+'-second' in urls:
        soup = makeSoup(urls[program+'-second'])
        reqlist.extend([x.text.split()[1] for x in soup.findAll('a', {'class': 'sc-courselink'}) if len(x.text.split()) > 1])
    with open(bscsfile, 'w') as f:
        json.dump(reqlist, f)
else:
    with open(bscsfile, 'r') as f:
        reqlist=json.load(f)

##### UPDATE OR READ PREREQ CACHE
prereqs = dict()
if not path.exists(prereqsfile):
    print('Updating list of prereqs for ' + year)
    #oops
    prereqs = {key: getPrereqs(classinfo[key]['url']) for key in classinfo}
    # this will only get the prereqs for the CS required classes... my bad
    #prereqs = {key: getPrereqs(classinfo[key]['url']) for key in reqlist}
    with open(prereqsfile, 'w') as f:
        json.dump(prereqs, f)
else:
    with open(prereqsfile, 'r') as f:
        prereqs = json.load(f)

# get only CS prereqs
cspres = {k: prereqs[k] for k in reqlist if k in prereqs}

reqset = set(reqlist)
if '17230' in reqset:
    reqset.remove('17230')

interesting_courses = {c: prereqs[c] for c in reqset}
graph = defaultdict(list)
for c in interesting_courses:
    for pr in interesting_courses[c]:
        graph[pr].append(c)

l = toposort(graph, interesting_courses.keys())

# TODO: toposort to determine better ordering of classes?
if not path.exists(arcfile):
    nodes = [{'id': c, 'name': classinfo[c]['name'], 'group': int(c[2])} for c in l]
    links = []
    for c in cspres:
        for pr in cspres[c]:
            if pr in reqset and pr[2] != '6':
                links.append({'source': pr, 'target': c, 'value': 1})
    with open(arcfile, 'w') as f:
        json.dump({'nodes': nodes, 'links': links}, f)

#print(prereqs['44517'], '17230' in reqset)
