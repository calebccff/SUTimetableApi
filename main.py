from flask_cors import CORS
from flask import Flask, request, abort
import requests, re, csv
from ics import Calendar

groups = {'t': 'turing', 'l': 'lovelace', 'b': 'babbage'}
modules = dict((row[0], row[1]) for row in csv.reader(open("modules.csv", "r")))

app = Flask(__name__)
CORS(app)

def eventIsDifferentSubHouse(name, g, p):
    ret = None
    if groups[g]+' a ' in name or groups[g]+' group a' in name:
        ret = 'a'
    elif groups[g]+' b ' in name or groups[g]+' group b' in name:
        ret = 'b'
        #print(name, p, g, ret==p)
    else:
        return False
    return not ret==p

@app.route('/api/<string:stu_hash>', methods=['GET'])
def index(stu_hash):
    print(request.url)
    g = request.args.get('group')
    hide_optional = request.args.get('hide_optional')
    hide_optional = hide_optional if not hide_optional == None else "f"
    
    if g == None or not len(g.split(":")) == 2:
        return "Your query string wasn't in the correct format"
    p = g.split(":")[1].lower()
    g = g.split(":")[0].lower()
    if not g in groups.keys() or not p in ['a', 'b']:
        return "Your query string wasn't in the correct format"

    timetable = requests.get("https://science.swansea.ac.uk/intranet/attendance/timetable/student_calendar/{0}/timetable.ics".format(stu_hash))
    if "page not found" in timetable.text.lower():
        return "The hash you provided was invalid"

    c = Calendar(timetable.text)
    toRemove = []

    for ev in c.events:
        name = ev.name.lower()
        removeGroups = list(groups.values())
        del removeGroups[removeGroups.index(groups[g])]
        pattern = re.compile("^((?!{}|{}).)+$".format(removeGroups[0], removeGroups[1]))
        if pattern.match(name): #This means the event name contains either the name of this users house, or no houses
            if re.compile("^.*{}.*$".format(groups[g])).match(name):
                if eventIsDifferentSubHouse(name, g, p):
                    toRemove.append(ev)
            elif "b groups" in name and p == "a" or "a groups" in name and p == "b": #They actually split in half too....
                toRemove.append(ev)
        else:
            toRemove.append(ev)
        
        if "t" in hide_optional.lower() and "Optional Help Session".lower() in ev.name.lower():
            toRemove.append(ev)
    for e in toRemove:
        c.events.remove(e)
    
    if request.args.get('codes_not_names') == None or not (request.args.get('codes_not_names') == "1" or "t" in request.args.get('codes_not_names')):
        for ev in c.events:
            for mod in modules.keys():
                if ":"+mod+" - " in ev.name:
                    ev.name = ev.name.replace(":"+mod+" - ", ": "+modules[mod]+" ")
                elif ":"+mod in ev.name:
                    ev.name = ev.name.replace(":"+mod, ": "+modules[mod]+" ")
                elif mod in ev.name:
                    ev.name = ev.name.replace(mod+":", modules[mod]+": ", 1)
                
    return str(c)


if __name__ == "__main__":
    app.run(debug=False, host = '127.0.0.1', port=8001)