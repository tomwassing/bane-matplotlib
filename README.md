<!-- Add a image to the readme -->
<img src="img/logo.svg" alt="Brane-Matplotlib logo" width="512"/>
<h1>Welcome to the Brane Matplotlib package 👋</h1>

[![example workflow](https://github.com/tomwassing/brane-matplotlib/actions/workflows/test.yml/badge.svg)](https://github.com/tomwassing/brane-matplotlib/actions/workflows/test.yml)

This repository contains a package for BRANE that runs multiple functions from the Matplotlib libary.

## Install

```sh
brane import tomwassing/brane-matplotlib
```

## Requirements
- PyYAML
- Matplotlib
- NumPy


## Usage

|     Action     |                                                                                                     Input (Data)                                                                                                     |    Output (Data)    |                       Description                      |
|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------:|:------------------------------------------------------:|
|    plot_base64 | input (string) <br /> scatter (boolean) <br /> x_label (string) <br /> y_label (string) <br /> title (string) <br /> cmap_input (string) <br /> cmap (string) <br /> edge_color (string)                             |    output (string)  |   Creates a base64 encoding of the  resulting plot     |
|     plot_file  | input (string) <br /> file_path (string) <br />  scatter (boolean) <br />  x_label (string) <br /> y_label (string) <br /> title (string) <br /> cmap_input (string) <br /> cmap (string) <br /> edge_color (string) |     output (string) |    Saves the created  plot to the specified  file_path |

## Run tests

```sh
python3 -m pytest
```

## Authors

👤 **Jurre J. Brandsen, Sander J. Misdorp, Tom J. Wassing**

* Github: [@JurreBrandsen1709](https://github.com/JurreBrandsen1709)
* Github: [@TomWassing](https://github.com/tomwassing)
* Github: [@SanderJan2](https://github.com/SanderJan2)

## Show your support

Give a ⭐️ if this project helped you!
