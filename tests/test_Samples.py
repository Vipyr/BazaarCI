import os
import subprocess as sp
import sys
from unittest import TestCase


class TestSamples(TestCase):
    def test_samples(self):
        samples_dir = os.path.join(
            os.path.dirname(__file__),
            "..",
            "docs",
            "samples",
        )
        for sample_file in os.listdir(samples_dir):
            if sample_file.endswith(".py"):
                with self.subTest(sample_file):
                    cp = sp.run([sys.executable, os.path.join(samples_dir, sample_file)], stdout=sp.PIPE, stderr=sp.STDOUT)
                    self.assertEqual(0, cp.returncode, "Non-zero returncode from sample " + sample_file)
