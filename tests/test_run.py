
import os
import numpy as np
import json
from os import path

from run import main


def test_random_nparray():
    test_data = np.random.rand(25, 25)
    os.environ["INPUT"] = json.dumps(test_data.tolist())
    os.environ["FILE_PATH"] = "./output.png"

    main("plot_file")

    assert path.exists("./output.png")
