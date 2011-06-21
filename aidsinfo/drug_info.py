#!/usr/bin/env python

"""Python wrapper for the AIDSinfo drug information API."""

from api import API

class DrugInfo(API):
    """Python wrapper for the AIDSinfo drug information API."""

    def __init__(self):
        super(DrugInfo, self).__init__()
        self.base_url = 'http://aidsinfo.nih.gov/DrugsNew/drug.aspx'
        self.output_format = 'xml'
        self.required_params = {'displayxml': 'true'}

    def search(self, name, **kwargs):
        """Search for a specific drug's information."""
        kwargs.update({'name': name})
        self.call_api(**kwargs)
