#
# Copyright (c) 2013 Alon Swartz <alon@turnkeylinux.org>
# Copyright (c) 2014 SUSE LLC, Robert Schweikert <rjschwei@suse.com>
#
# This file is part of ec2metadata.
#
# ec2metadata is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ec2metadata is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ec2metadata.  If not, see <http://www.gnu.org/licenses/>.

"""
Utilities to implement convenience functionality. Also allows us to keep
unnecessary state out of the metadata class
"""
import os
import sys

import ec2metadata

def _genXML(metadata, metaopts):
    """Use the option name as a tag name to wrap the data."""

    xml = ''
    for metaopt in metaopts:
        value = metadata.get(metaopt)
        if not value:
            value = "unavailable"
        xml += '<%s>' %metaopt
        xml += str(value)
        xml += '</%s>\n' %metaopt
        
    return xml

def _write(filePath, data):
    """Write the data to the given file"""
    fout = None
    if type(filePath) is str:
        fout = open(filePath, 'w')
    elif type(filePath) is file:
        fout = filePath
    fout.write(data)
    fout.close()

def display(metadata, metaopts, prefix=False):
    """primitive: display metaopts (list) values with optional prefix"""

    writefile(sys.stdout, metadata, metaopts, prefix)

def displayXML(metadata, metaopts):
    """Collect the requested data and display it as XML"""
    data = _genXML(metadata, metaopts)
    print data

def showVersion():
    """Print the version"""
    verPath = os.path.dirname(__file__) + '/VERSION'
    print open(verPath).read()

def writefile(filePath, metadata, metaopts, prefix=False):
    """Collect the requested data and write it to the given file."""

    data = ''
    for metaopt in metaopts:
        value = metadata.get(metaopt)
        if not value:
            value = "unavailable"

        if prefix:
            data += '%s: %s\n' % (metaopt, value)
        else:
            data += value + '\n'

    _write(filePath, data)

def writeXMLfile(filePath, metadata, metaopts):
    """Collect the requested data and write it to the given file as XML"""

    data = _genXML(metadata, metaopts)
    _write(filePath, data)
