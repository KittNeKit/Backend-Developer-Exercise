import sys
import unittest
from io import StringIO
from main import Pagination


class TestPaginationFooter(unittest.TestCase):
    test_data = [
        (4, 5, 1, 0, "1 ... 4 5"),
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (5, 5, 2, 2, "1 2 3 4 5"),
        (1, 1, 0, 0, "1"),
        (8, 10, 1, 2, "1 ... 6 7 8 9 10"),
        (
            777, 7777, 7, 7,
            "1 2 3 4 5 6 7 ... 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 ... 7771 7772 7773 7774 7775 7776 7777"
        ),
        (333, 3333333, 3, 3, "1 2 3 ... 330 331 332 333 334 335 336 ... 3333331 3333332 3333333"),
        (333, 3333333, 3, 0, "1 2 3 ... 333 ... 3333331 3333332 3333333"),
        (5, 10, 11, 1, "1 2 3 4 5 6 7 8 9 10"),
        (50, 25, 50, 20, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"),
        (1, 10, 6, 1, "1 2 3 4 5 6 7 8 9 10"),
        (1, 25, 15, 1, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"),
        (5, 10, 6, 1, "1 2 3 4 5 6 7 8 9 10"),
        (11, 25, 15, 1, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"),
    ]

    def setUp(self):
        self.old_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_pagination_footer(self):
        for current_page, total_pages, boundaries, around, expected_result in self.test_data:
            with self.subTest(current_page=current_page, total_pages=total_pages,
                              boundaries=boundaries, around=around, expected_result=expected_result):
                sys.stdout = my_stdout = StringIO()
                Pagination.create_pagination(current_page, total_pages, boundaries, around)
                sys.stdout = self.old_stdout
                result = my_stdout.getvalue()
                self.assertEqual(result.strip(), expected_result)
