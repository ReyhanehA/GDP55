# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:59 2013 by generateDS.py version 2.9a.
#

import sys

from mixbox.binding_utils import *

from stix.bindings import register_extension
import stix.bindings.exploit_target as exploit_target_binding

XML_NS = "http://stix.mitre.org/extensions/Vulnerability#CVRF-1"

#
# Data representation classes.
#

@register_extension
class CVRF1_1InstanceType(exploit_target_binding.VulnerabilityType):
    """The CVRF1.1InstanceType provides an extension to the
    exploit_target_binding.VulnerabilityType which imports and leverages the CVRF schema
    for structured characterization of Vulnerabilities. This could
    include characterization of 0-days or other vulnerabilities that
    do not have a CVE or OSVDB ID."""
    subclass = None
    superclass = exploit_target_binding.VulnerabilityType

    xmlns          = XML_NS
    xmlns_prefix   = "cvrfVuln"
    xml_type       = "CVRF1.1InstanceType"

    def __init__(self, Description=None, CVE_ID=None, OSVDB_ID=None, CVSS_Score=None, cvrfdoc=None):
        super(CVRF1_1InstanceType, self).__init__(Description=Description, CVE_ID=CVE_ID, OSVDB_ID=OSVDB_ID, CVSS_Score=CVSS_Score)
        self.cvrfdoc = cvrfdoc
    def factory(*args_, **kwargs_):
        if CVRF1_1InstanceType.subclass:
            return CVRF1_1InstanceType.subclass(*args_, **kwargs_)
        else:
            return CVRF1_1InstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_cvrfdoc(self): return self.cvrfdoc
    def set_cvrfdoc(self, cvrfdoc): self.cvrfdoc = cvrfdoc
    def hasContent_(self):
        if (
            self.cvrfdoc is not None or
            super(CVRF1_1InstanceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CVRF1.1InstanceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CVRF1.1InstanceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='CVRF1.1InstanceType'):
        super(CVRF1_1InstanceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CVRF1.1InstanceType')
        if 'xmlns' not in already_processed:
            already_processed.add('xmlns')
            xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
            lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CVRF1.1InstanceType', fromsubclass_=False, pretty_print=True):
        super(CVRF1_1InstanceType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cvrfdoc is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.cvrfdoc, pretty_print=pretty_print))
            #self.cvrfdoc.export(lwrite, level, nsmap, namespace_, name_='cvrfdoc', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(CVRF1_1InstanceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'cvrfdoc':
            self.set_cvrfdoc(child_)
        super(CVRF1_1InstanceType, self).buildChildren(child_, node, nodeName_, True)
# end class CVRF1_1InstanceType

GDSClassesMapping = {}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CVRF1.1InstanceType'
        rootClass = CVRF1_1InstanceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CVRF1.1InstanceType'
        rootClass = CVRF1_1InstanceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CVRF1.1InstanceType'
        rootClass = CVRF1_1InstanceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="CVRF1.1InstanceType",
        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "CVRF1_1InstanceType"
    ]
