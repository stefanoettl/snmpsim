#
# This file is part of snmpsim software.
#
# Copyright (c) 2010-2019, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/snmpsim/license.html
#
from snmpsim.grammar import walk
from snmpsim.record import dump


class WalkRecord(dump.DumpRecord):
    grammar = walk.WalkGrammar()
    ext = 'snmpwalk'
