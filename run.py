#!/usr/bin/env python3

import os
import sys
import yaml
import io
import json
import matplotlib.pyplot as plt
import numpy as np


def read_np_array(key):
    os_data = os.environ.get(key)
    if os_data is None:
        return None

    return np.array(json.loads(os_data))


def main(command):
    # reading input data
    data = read_np_array("INPUT")
    cmap_data = read_np_array("CMAP_INPUT")

    cmap_name = os.environ.get("CMAP")
    edge_color = os.environ.get("EDGE_COLOR")

    if os.environ.get("SCATTER", False):
        plt.scatter(data[:, 0], data[:, 1], c=cmap_data,
                    cmap=cmap_name, edgecolor=edge_color)
    else:
        plt.plot(data)

    # setting labels and title
    plt.xlabel(os.environ.get("X_LABEL", ""))
    plt.ylabel(os.environ.get("Y_LABEL", ""))
    plt.title(os.environ.get("TITLE", ""))

    if command == "plot_base64":
        temp_file = io.BytesIO()
        plt.savefig(temp_file)
        output = temp_file.getvalue()

        # write image encoded to stdout
        print(yaml.dump({"output": output}))
    elif command == "plot_file":
        file_path = os.environ.get("FILE_PATH", "/data/output.png")
        plt.savefig(file_path)
        print(yaml.dump({"output": file_path}))
    elif command == "plot_show":
        plt.show()
        print(yaml.dump({"output": "show"}))
    else:
        print("Unknown command")


if __name__ == "__main__":
    main(sys.argv[1])
