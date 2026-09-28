import unittest

from video_class import Video
class video_test(unittest.TestCase):

    def setUp(self):
        self.video = Video("legend of avater", 10)


    def test_advance_moves_forward(self):
        self.video.advance(4)
        self.assertEqual(self.video.time_remaining(), 6)

    def test_advance_does_not_exceed_duration(self):
        self.video.advance(15)
        self.assertEqual(self.video.time_remaining(), 0)
        self.assertTrue(self.video.is_finished())

    def test_is_finished_false_initially(self):
        self.assertFalse(self.video.is_finished())

    def test_is_finished_true_at_end(self):
        self.video.advance(10)
        self.assertTrue(self.video.is_finished())

    def test_restart_resets_position(self):
        self.video.advance(7)
        self.video.restart()
        self.assertEqual(self.video.time_remaining(), 10)
        self.assertFalse(self.video.is_finished())

    def test_time_remaining_updates_correctly(self):
        self.video.advance(3)
        self.assertEqual(self.video.time_remaining(), 7)
        self.video.advance(3)
        self.assertEqual(self.video.time_remaining(), 4)


if __name__ == "__main__":
    unittest.main()