# Vorticity Gaia API

Vorticity Gaia is a cloud compute service that uses custom accelerator cards to speed up compute seismic imaging projects. This API connects users to this service through well understood seismic operators.

## Getting Started
This guide is for linux and MacOS based machines. For other operating systems, contact Vorticity.

## Prerequisits
* [Python3.8](https://www.python.org/downloads/) or better
* pip
```bash
sudo apt install python3-pip
```
* numpy, grpcio, protobuf
```bash
python3 -m pip install numpy
python3 -m pip install grpcio
python3 -m pip install protobuf
```
* matplotlib (optional)
```bash
python3 -m pip install -U matplotlib
```

## Installation
1. Clone the public git repository on to your working directory
```bash
git clone https://github.com/VorticityXYZ/GaiaAPI /working-directory
```
2. Get a token and certificate file by contacting Vorticity.
3. Copy these files to the working directory.

## Usage
### Examples
1. demo.py - Demonstrates how to run a forward model using the acousitic wave equations.
2. demo2.py - Demostrates how to run a acoustic reverse time migration (RTM) .
3. edemo.py - Demonstrates how to run a forward model using the elastic wave equations.
4. edemo2.py - Demonstrates how to run a elastic reverse time migration (RTM).

### Full Documentation
* [vorticity.cloud](https://www.vorticity.cloud) - WIP

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact Vorticity

* <hello@vorticity.xyz>
* <info@vorticity.xyz>


