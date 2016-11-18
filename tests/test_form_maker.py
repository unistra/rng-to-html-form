from rng_to_form.rng import RNG
from rng_to_form.form_maker import make_form
from unittest import TestCase, main


class RngTest(TestCase):

    def setUp(self):
        self.file = "./tests/data/test.rng"
        self.rng = RNG(file=self.file, target="ArchiveTransfer")

    def test_generate_form(self):
        generated_form = make_form(self.rng)
        self.assertIsNotNone(generated_form)
        self.assertTrue('''<div class="Comment_N65541"><div style='font-weight:bold;'>Comment_N65541.value</div><input class='selectable' value=" My comment" style='width:87%' name="Comment_N65541" readonly></div></div>''' in generated_form)


if __name__ == '__main__':
    main()
