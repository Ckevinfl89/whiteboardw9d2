from whiteboard import solution
from unittest import TestCase, main


class WhiteboardTest(TestCase):

    def test_basic(self):
        self.assertEqual(solution([1, 2, 3, 4, 100]), 3)

    def test_dup_min(self):
        self.assertEqual(solution([1, 1, 5, 5, 10, 8, 7]), 6)

    def test_negs(self):
        self.assertEqual(solution([-10, -4, -2, -4, -2, 0]), -3)

    def test_dup_max(self):
        self.assertEqual(solution([10,10,5,2,3,1,6]), 4)

    def test_dup_max_and_min(self):
        self.assertEqual(solution([10,10,5,5,4,3,2,2,1,1]), 3)

if __name__ == '__main__':
    main()