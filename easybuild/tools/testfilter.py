# #
# Copyright 2016-2016 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
# #
"""
Overrides TestLoader to filter single tests

@author Caroline De Brouwer (Ghent University)
"""
import sys
import unittest
from unittest import suite

class TestLoaderFiltered(unittest.TestLoader):

    def loadTestsFromTestCase(self, testCaseClass, filters):
        """Return a suite of all tests cases contained in testCaseClass."""

        if issubclass(testCaseClass, suite.TestSuite):
            raise TypeError("Test cases should not be derived from "\
                "TestSuite. Maybe you meant to derive from"\
                " TestCase?")
        test_case_names = self.getTestCaseNames(testCaseClass)

        test_cases = []
        for test_case_name in test_case_names:
            for f in filters:
                if f in test_case_name:
                    test_cases.append(testCaseClass(test_case_name))

        loaded_suite = self.suiteClass(test_cases)

        return loaded_suite

def filter_tests():
    fstr = []
    if len(sys.argv) == 1:
        fstr.append('')
    while len(sys.argv) > 1:
        fstr.append(sys.argv.pop())
    return fstr