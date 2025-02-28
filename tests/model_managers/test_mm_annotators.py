import glob
import pathlib

import pytest
from PIL import Image

from hordelib.settings import UserSettings


class TestHordePreloadAnnotators:
    def test_preload_annotators(self):
        import hordelib

        hordelib.initialise(setup_logging=True)

        from hordelib.shared_model_manager import SharedModelManager

        SharedModelManager.preloadAnnotators()

    def test_check_sha_annotators(self):
        from hordelib.model_manager.base import BaseModelManager

        annotatorCacheDir = (
            pathlib.Path(UserSettings.get_model_directory()).joinpath("controlnet").joinpath("annotator")
        )
        annotators = glob.glob("*.pt*", root_dir=annotatorCacheDir)
        for annotator in annotators:
            hash = BaseModelManager.get_file_sha256_hash(annotatorCacheDir.joinpath(annotator))
            print(f"{annotator}: {hash}")  # XXX # TODO Validate hashes
