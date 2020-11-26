import fileinput
import os
import sys,argparse

import numpy
import pandas

p = argparse.ArgumentParser()
def folder(v):
    if not os.path.isdir(v):
        v = "packages/%s"%v
    vFolder = v.replace("_","-")
    assert os.path.isdir(vFolder),"You must pass an existing folder name not '%s'"%(vFolder,)
    return vFolder
p.add_argument("targetFolder",type=folder)
args = p.parse_args()
oldDir = os.getcwd()
os.chdir(args.targetFolder)
package_name = os.path.basename(args.targetFolder)
with open(os.path.join("index.html"),"wb") as f:
    f.write('<h1>Links for {0}</h1>\n'.format(package_name))
    for fname in os.listdir("."):
        if fname.endswith(".gz") or fname.endswith(".whl"):
            f.write("<a href=\"{0}\">{0}</a>\n".format(fname))

pkg_entry = "<a href=\"{0}/\">{0}</a>".format(package_name)
print("CHECK:",pkg_entry)
os.chdir(oldDir)
if not os.path.exists("index.html") or pkg_entry not in open("index.html","rb").read():
    print("ADD:",package_name)
    if os.path.exists('index.html'):
        entries = numpy.genfromtxt("index.html",dtype="S132",delimiter="\n")

        ix = numpy.searchsorted(entries, pkg_entry)
        entries = numpy.insert(entries, ix, pkg_entry)
    else:
        entries = [pkg_entry]
    print("Entries:",entries)
    import pdb;pdb.set_trace()
    s= "\n".join(entries)
    with open("index.html","wb") as f:
        f.writelines("\n".join(entries))
print("DEPLOYED")




