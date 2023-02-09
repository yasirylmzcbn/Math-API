import flask
from flask import request
import json
import sys
import werkzeug
import statistics
from math import *

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {'success': True, 'message': 'This is the home page'}

@app.route('/area/square', methods=['GET'])
def aSq():
    try:
        s = float(request.args['s'])
        a = s*s
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 's' : s}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/rectangle', methods=['GET'])
def aRect():
    try:
        l = float(request.args['l'])
        w = float(request.args['w'])
        a = l*w
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 'l' : l, 'w' : w}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/triangle', methods=['GET'])
def aTri():
    try:
        b = float(request.args['b'])
        h = float(request.args['h'])
        a = (b*h)/2
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 'b' : b, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/heron', methods=['GET'])
def aTriH():
    try:
        a = float(request.args['a'])
        b = float(request.args['b'])
        c = float(request.args['c'])
        s = a + b + c
        s /= 2
        ar = sqrt(s*(s-a)*(s-b)*(s-c))
    except:
        return 'Bad or missing variable', 400
    js = {'area' : ar, 's' : s, 'a' : a, 'b' : b, 'c' : c}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/parallelogram', methods=['GET'])
def aPar():
    try:
        b = float(request.args['b'])
        h = float(request.args['h'])
        a = b*h
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 'b' : b, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/circle', methods=['GET'])
def aCirc():
    try:
        r = float(request.args['r'])
        a = pi*r*r
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 'r' : r}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/area/trapezoid', methods=['GET'])
def aTrap():
    try:
        b1 = float(request.args['b1'])
        b2 = float(request.args['b2'])
        h = float(request.args['h'])
        a = (b1+b2)/2 * h
    except:
        return 'Bad or missing variable', 400
    js = {'a' : a, 'b1' : b1, 'b2' : b2, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/surface/cube', methods=['GET'])
def saCube():
    try:
        s = float(request.args['s'])
        sa = 6*s*s
    except:
        return 'Bad or missing variable', 400
    js = {'sa' : sa, 's' : s}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/surface/sphere', methods=['GET'])
def saSph():
    try:
        r = float(request.args['r'])
        sa = 4*r*r
    except:
        return 'Bad or missing variable', 400
    js = {'sa' : sa, 'r' : r}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/surface/cylinder', methods=['GET'])
def saCyl():
    try:
        r = float(request.args['r'])
        h = float(request.args['h'])
        sa = 2 * pi * r * h
    except:
        return 'Bad or missing variable', 400
    js = {'sa' : sa, 'r' : r, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

app.route('/perimeter/square', methods=['GET'])
def pSqr():
    try:
        s = float(request.args['s'])
        sa = 4*s
    except:
        return 'Bad or missing variable', 400
    js = {'p' : sa, 's' : s}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/perimeter/rectangle', methods=['GET'])
def pRect():
    try:
        l = float(request.args['l'])
        w = float(request.args['w'])
        sa = 2 * (l+w)
    except:
        return 'Bad or missing variable', 400
    js = {'p' : sa, 'l' : l, 'w' : w}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/perimeter/triangle', methods=['GET'])
def pTri():
    try:
        s1 = float(request.args['s1'])
        s2 = float(request.args['s2'])
        s3 = float(request.args['s3'])
        p = s1 + s2 + s3
    except:
        return 'Bad or missing variable', 400
    js = {'p' : p, 's1' : s1, 's2' : s2, 's3' : s3}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/perimeter/circle', methods=['GET'])
def pCirc():
    try:
        d = float(request.args['d'])
        p = pi*d
    except:
        return 'Bad or missing variable', 400
    js = {'p' : p, 'd' : d}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/volume/cube', methods=['GET'])
def vCub():
    try:
        s = float(request.args['s'])
        v = s*s*s
    except:
        return 'Bad or missing variable', 400
    js = {'v' : v, 's' : s}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/volume/prism', methods=['GET'])
def vPrs():
    try:
        l = float(request.args['l'])
        w = float(request.args['w'])
        h = float(request.args['h'])
        v = l*w*h
    except:
        return 'Bad or missing variable', 400
    js = {'v' : v, 'l' : l, 'w' : w, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/volume/pyramid', methods=['GET'])
def vPyr():
    try:
        b = float(request.args['b'])
        h = float(request.args['h'])
        v = (b*b*h)/3
    except:
        return 'Bad or missing variable', 400
    js = {'v' : v, 'b' : b, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/volume/cylinder', methods=['GET'])
def vCyl():
    try:
        r = float(request.args['r'])
        h = float(request.args['h'])
        v = pi * r * r * h
    except:
        return 'Bad or missing variable', 400
    js = {'v' : v, 'r' : r, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/volume/cone', methods=['GET'])
def vCon():
    try:
        r = float(request.args['r'])
        h = float(request.args['h'])
        v = (pi * r * r * h)/3
    except:
        return 'Bad or missing variable', 400
    js = {'v' : v, 'r' : r, 'h' : h}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/distance', methods=['GET'])
def dist():
    try:
        x1 = float(request.args['x1'])
        y1 = float(request.args['y1'])
        x2 = float(request.args['x2'])
        y2 = float(request.args['y2'])
        distance = sqrt((x2-x1)**2 + (y2  - y1)**2)
    except:
        return 'Bad or missing variable', 400
    js = {'distance' : distance, 'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
    return json.dumps(js), 200, {'Content-Type' : 'application/json'}
    
@app.route('/slope', methods=['GET'])
def slope():
    try:
        x1 = float(request.args['x1'])
        y1 = float(request.args['y1'])
        x2 = float(request.args['x2'])
        y2 = float(request.args['y2'])
        slope = (y2 - y1) / (x2 - x1)
    except:
        return 'Bad or missing variable', 400
    js = {'slope' : slope, 'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
    return json.dumps(js), 200, {'Content-Type' : 'application/json'}

@app.route('/pythag', methods=['GET'])
def pythag():
    at = False
    bt = False
    ct = False
    try:
        try:
            a = float(request.args['a'])
            at = True
            b = float(request.args['b'])
            bt = True
        except:
            c = float(request.args['c'])
            ct = True
        try:
            a = float(request.args['a'])
            at = True
        except:
            b = float(request.args['b'])
            bt = True
    except:
        return 'Bad or missing variable', 400
    if at and bt:
        c = sqrt(a**2 + b**2)
    elif at and ct:
        b = sqrt(c**2 - a**2)
    else:
        a = sqrt(c**2 - b**2)
    js = {'a' : a, 'b' : b, 'c' : c}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/mean', methods=['GET'])
def mean():
    try:
        lst = request.args['nums']
        lst = lst.split(",")
        mean = 0
        for i in lst:
            mean += float(i)
        mean /= len(lst)
    except:
        return 'Bad or missing variable', 400
    js = {'mean' : mean, 'list' : lst}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/median', methods=['GET'])
def median():
    try:
        lst = request.args['nums']
        lst = lst.split(",")
        for i in range(0,len(lst)):
            lst[i] = float(lst[i])
        median = str(statistics.median(lst))
    except:
        return 'Bad or missing variable', 400
    js = {'median' : median, 'list' : lst}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.route('/mode', methods=['GET'])
def mode():
    try:
        lst = request.args['nums']
        lst = lst.split(",")
        for i in lst:
            i = float(i)
        median = str(statistics.mode(lst))
    except:
        return 'Bad or missing variable', 400
    js = {'mode' : median, 'list' : lst}
    return json.dumps(js), 200, {'Content-Type': 'application/json'}

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404

app.run(host='127.0.0.1', port=3001)
