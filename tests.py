import sys
import unittest
from io import StringIO
from main import Pagination


class TestPaginationFooter(unittest.TestCase):
    test_data = [
    ]

    def setUp(self):
        self.old_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_pagination_footer(self):
        for current_page, total_pages, boundaries, around, expected_result in self.test_data:
            sys.stdout = my_stdout = StringIO()
            Pagination.create_pagination(current_page, total_pages, boundaries, around)
            sys.stdout = self.old_stdout
            result = my_stdout.getvalue()
            self.assertEqual(result.strip(), expected_result)
