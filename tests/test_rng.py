from rng_to_form.rng import RNG
from unittest import TestCase, main


class RngTest(TestCase):

    def setUp(self):
        self.file = "./tests/data/test.rng"

    def test_create_rng_obj(self):
        rng = RNG(file=self.file, target="ArchiveTransfer")
        self.assertIsNotNone(rng)


if __name__ == '__main__':
    main()
