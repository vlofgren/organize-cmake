#!/usr/bin/python

import sys
print("# "+" ".join(sys.argv[1:]))

modules = {}
for f in sys.argv[1:]:
    breakdown = f.split('/', 1)
    module= "base"
    if len(breakdown) == 2:
        module = breakdown[0]

    if not module in modules:
        modules[module] = list()

    modules[module].append(f)

for k,m in modules.iteritems():
    sortm = sorted(m)
    print "set(" + k.upper() + "_HEADERS " + " ".join([m for m in sortm if m.endswith("h")]) + ")"
    print "set(" + k.upper() + "_SOURCES " + " ".join([m for m in sortm if not m.endswith("h")]) + ")"
    print ""

print "set(SOURCE_FILES " + " ".join(["${" + m.upper()+"_SOURCES} ${" + m.upper() + "_HEADERS}" for m in modules.keys()]) + ")"
