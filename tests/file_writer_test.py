# Copyright 2013 Locaweb.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# @author: Willian Molinari (PotHix), Locaweb.

from haproxy_manager.file_writer import FileWriter

import unittest


class FileWriterTest(unittest.TestCase):

    def setUp(self):
        self.writer = FileWriter('tests/output/')

    def test_global_file_writing(self):
        self.writer.global_writer({"name": "machine0001"})

    def test_backend_file_writing(self):
        self.writer.backend_writer({"name": "machine0001"})

    def test_frontend_file_writing(self):
        self.writer.frontend_writer({"name": "machine0001"})
