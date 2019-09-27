from flask_cors import CORS
from flask import Flask, request, abort
import requests
from ics import Calendar

groups = {'t': 'turing', 'l': 'lovelace', 'b': 'babbage'}

app = Flask(__name__)
CORS(app)

def isMember(ev, g, p):
    if groups[g] in ev.name.lower() or groups[g]+' group '+p in ev.name.lower() or groups[g]+' '+p+' group' in ev.name.lower():
        return True
    return False

@app.route('/api/<string:stu_hash>', methods=['GET'])
def index(stu_hash):
    g = request.args.get('group')
    
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
        if any([x in ev.name.lower() for x in groups.values()]):
            if not isMember(ev, g, p):
                toRemove.append(ev)
    for e in toRemove:
        c.events.remove(e)
    return str(c)



if __name__ == "__main__":
    app.run(debug=False, host = '127.0.0.1', port=8001)