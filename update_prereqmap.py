import json
from os import path, mkdir
from scraperutils import BASE_URL, getAllClasses, makeSoup, getPrereqs
year = '2020-2021'

classfile = path.join(year, 'allclasses.json')
bscsfile = path.join(year, 'bscsreqs.json')
prereqsfile = path.join(year, 'allprereqs.json')
arcfile = path.join(year, 'csprereqs_arc.json')

urls = {
    'courses': '{}/{}/Undergraduate-Catalog/Courses/'.format(BASE_URL, year),
    'bscs': '{}/{}/Undergraduate-Catalog/School-of-Computer-Science-and-Information-Systems/Computer-Science-and-Information-Systems-44/Computer-Science-Comprehensive-Major-6669-hours-BSNo-Minor-Required'.format(
        BASE_URL, year)
}



##### UPDATE OR READ YEAR CLASS LIST CACHE

if not path.isdir(year):
    mkdir(year)

classinfo = dict()
if not path.exists(classfile):
    print ('Updating class list for ' + year)
    pagesoup = makeSoup(urls['courses'])
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
    print('Updating BS in CS requirements for ' + year)
    soup = makeSoup(urls['bscs'])
    reqlist = [x.text.split()[1] for x in soup.findAll('a', {'class': 'sc-courselink'}) if len(x.text.split()) > 1]
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
    #prereqs = {key: getPrereqs(classinfo[key]['url']) for key in classinfo}
    # this will only get the prereqs for the CS required classes... my bad
    prereqs = {key: getPrereqs(classinfo[key]['url']) for key in reqlist}
    with open(prereqsfile, 'w') as f:
        json.dump(prereqs, f)
else:
    with open(prereqsfile, 'r') as f:
        prereqs = json.load(f)

# get only CS prereqs
cspres = {k: prereqs[k] for k in reqlist if k in prereqs}

reqset = set(reqlist)
reqset.remove('17230')

if not path.exists(arcfile):
    nodes = [{'id': c, 'name': classinfo[c]['name'], 'group': int(c[2])} for c in cspres]
    links = []
    for c in cspres:
        for pr in cspres[c]:
            if pr in reqset and pr[2] != '6':
                links.append({'source': pr, 'target': c, 'value': 1})
    with open(arcfile, 'w') as f:
        json.dump({'nodes': nodes, 'links': links}, f)

#print(prereqs['44517'], '17230' in reqset)
