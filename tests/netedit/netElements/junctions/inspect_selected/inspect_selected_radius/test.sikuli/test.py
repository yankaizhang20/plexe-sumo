#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# rebuild network
netedit.rebuildNetwork()

# go to select mode
netedit.selectMode()

# select first edge
netedit.leftClick(match, 325, 250)

# select second edge
netedit.leftClick(match, 10, 220)

# go to inspect mode
netedit.inspectMode()

# inspect central node
netedit.leftClick(match, 325, 220)

# set invalid radius
netedit.modifyAttribute(1, "dummyRadius")

# set invalid radius
netedit.modifyAttribute(1, "-7")

# change radio
netedit.modifyAttribute(1, "2.3")

# rebuild network
netedit.rebuildNetwork()

# Check undo
netedit.undo(match, 1)

# rebuild network
netedit.rebuildNetwork()

# Check redo
netedit.redo(match, 1)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)