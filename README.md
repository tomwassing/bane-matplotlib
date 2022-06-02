<!-- Add a image to the readme -->
<img src="logo.svg" alt="Brane-Matplotlib logo" width="512"/>
<h1>Welcome to Brane Matplotlib 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> This repository contains a package for BRANE that runs multiple functions from the Matplotlib libary.

## Install

```sh
brane import tomwassing/brane-matplotlib
```

## Requirements
- Yaml
- JSON
- Matplotlib
- Numpy


## Usage

|     Action     |                                                                                                     Input (Data)                                                                                                     |    Output (Data)    |                       Description                      |
|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------:|:------------------------------------------------------:|
|    plot_base64 | input (string) <br /> scatter (boolean) <br /> x_label (string) <br /> y_label (string) <br /> title (string) <br /> cmap_input (string) <br /> cmap (string) <br /> edge_color (string)                             |    output (string)  |   Creates a base64 encoding of the  resulting plot     |
|     plot_file  | input (string) <br /> file_path (string) <br />  scatter (boolean) <br />  x_label (string) <br /> y_label (string) <br /> title (string) <br /> cmap_input (string) <br /> cmap (string) <br /> edge_color (string) |     output (string) |    Saves the created  plot to the specified  file_path |

## Run tests

```sh
python3 -m pytest
```

## Author

👤 **Jurre J. Brandsen, Sander J. Misdorp, Tom J. Wassing**

* Github: [@JurreBrandsen1709](https://github.com/JurreBrandsen1709)
* Github: [@TomWassing](https://github.com/tomwassing)
* Github: [@SanderJan2](https://github.com/SanderJan2)

## Show your support

Give a ⭐️ if this project helped you!
