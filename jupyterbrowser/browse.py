"""a Jupyter Notebook GUI for quickly finding notebooks in your tree"""

import os
import datetime

from IPython.display import display, HTML
from ipywidgets import interact

try:
    # python3
    from urllib.request import pathname2url
except:
    # python2
    from urllib import pathname2url


def age(dt):
    """convert a datetime to a user-friendly age string"""
    delta = datetime.datetime.now() - dt
    if delta.total_seconds() < 60.:
        return '%.0f seconds' % delta.total_seconds()
    elif delta.total_seconds() < 60.*60.:
        return '%.0f minutes' % (delta.total_seconds()/60.)
    elif delta.total_seconds() < 60.*60.*24.0:
        return '%.0f hours' % (delta.total_seconds()/(60.*60.))
    elif delta.days < 365:
        return '%d days' % delta.days
    else:
        return '%d years' % (delta.days/365.)


def indexnotebooks():
    """walk tree from current working dir return a list of notebooks with properties"""
    notebooks = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for f in filenames:
            name,ext = os.path.splitext(f)
            if ext == '.ipynb':
                if not name.endswith('-checkpoint'):
                    path = os.path.join(dirpath,f)
                    notebooks.append({'name':name,
                                      'dirpath':dirpath,
                                      'path':path,
                                      'link':path2link(path),
                                      'ctime':datetime.datetime.fromtimestamp(os.path.getctime(path)),
                                      'mtime':datetime.datetime.fromtimestamp(os.path.getmtime(path)),
                                      'atime':datetime.datetime.fromtimestamp(os.path.getatime(path)),
                                      })
    return notebooks



def path2link(path):
    """generate html link from file system oath"""
    return '<a href="%s" target="_blank">%s</a>' % (pathname2url(path),path)


def renderHTML(maxrows,sortby,search,descend):
    """generate HTML table with sorted filtered results"""
    data_sorted = sorted(indexnotebooks(), key=lambda item: item[sortby])
    if len(search)>0:
        data_sorted = list(filter(lambda x:x['path'].lower().find(search.lower())>-1,data_sorted))
    nitems = len(data_sorted)
    if descend:
        data_sorted = reversed(data_sorted)
    s = '<table>'
    s += '<tr><th>%d items match, showing %d</th></tr>\n' % (nitems,int(maxrows))
    s += '<tr><th>Folder</th><th>File Name</th><th>Modified</th></tr>\n'
    for i,n in enumerate(data_sorted):
        s += '<tr><td>%s</td><td>%s</td><td>%s ago</td></tr>\n' % (n['dirpath'],n['link'],age(n['mtime']))
        if i > int(maxrows):
            break
    s += '</table>'
    return s


def render(maxrows,sortby,search,descend):
    """interact callback for rendering the cell"""
    display(HTML(renderHTML(maxrows,sortby,search,descend)))


def ui():
    """call this in a notebook cell to display the browser"""
    interact(
        render,
        maxrows=['20','30','50'],
        sortby=['mtime','ctime','dirpath'],
        search='',
        descend=True)


# for testing...
if __name__ == '__main__':
    print(renderHTML(maxrows=10,sortby='mtime',search='',descend=True))