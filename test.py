#!/usr/bin/env python

"""Unit tests for the AIDSinfo drug information API."""

import unittest

from mock import Mock

from aidsinfo.api import api
from aidsinfo import DrugInfo


class TestDrugInfoSearchMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_url_called_for_abacavir(self):
        info = DrugInfo()
        info.search('abacavir')
        expected_url = ('http://aidsinfo.nih.gov/DrugsNew/drug.aspx?'
                        'displayxml=true&name=abacavir')
        api.urlopen.assert_called_with(expected_url)

    def test_url_called_for_combivir(self):
        info = DrugInfo()
        info.search('combivir')
        expected_url = ('http://aidsinfo.nih.gov/DrugsNew/drug.aspx?'
                        'displayxml=true&name=combivir')
        api.urlopen.assert_called_with(expected_url)

    def test_xml_data_is_output(self):
        info = DrugInfo()
        info.search('combivir', output_format=None)
        self.assertFalse(api.xml2dict.called)


if __name__ == '__main__':
    unittest.main()
