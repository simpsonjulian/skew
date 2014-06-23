# Copyright (c) 2014 Mitch Garnaat http://garnaat.org/
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import jmespath

import skew.arn.resources


class Table(skew.arn.resources.Resource):

    Config = {
        'service': 'dynamodb',
        'type': 'table',
        'enum_spec': ('ListTables', 'TableNames'),
        'detail_spec': ('DescribeTable', 'table_name', 'Table'),
        'id': 'Table',
        'filter_name': None,
        'name': 'TableName',
        'date': 'CreationDateTime',
        'dimension': 'TableName'
    }

    def __init__(self, endpoint, data):
        super(Table, self).__init__(endpoint, data)
        self._id = data
        detail_op, param_name, detail_path = self.Config['detail_spec']
        params = {param_name: self.id}
        data = endpoint.call(detail_op, **params)
        self.data = jmespath.search(detail_path, data)
