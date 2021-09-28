# Vorticity Gaia API

Vorticity Gaia is a cloud compute service that provides lightening fast computing for seismic imaging problems such as FWI, using custom silicon accelerators. These accelerators are built from the ground up to solve scientific computing problems and are typically orders or magnitude faster than typical consumer GPU and CPU based systems. This open source API allows users to connect to this service using well established seismic operators.

## Getting Started
This guide is for linux and MacOS based machines. Windows machines will require a linux bash shell. For troubleshooting contact Vorticity.

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
* [segyio](https://github.com/equinor/segyio) (optional) - Open source segy to numpy file converter.


## Installation
1. Clone the public git repository to your working directory
```bash
git clone https://github.com/VorticityXYZ/GaiaAPI
```
2. Get in touch with Vorticity (<hello@vorticity.xyz>) for a token and encryption file.
3. Copy these two files to your working directory.

## Usage
### Examples
1. [demo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/demo.py) - Demonstrates how to run a forward model using the acousitic wave equations.
2. [demo2.py](https://github.com/vorticityxyz/Gaia-api/blob/main/demo2.py) - Demostrates how to run a acoustic reverse time migration (RTM) .
3. [edemo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/edemo.py) - Demonstrates how to run a forward model using the elastic wave equations.
4. [edemo2.py](https://github.com/vorticityxyz/Gaia-api/blob/main/edemo2.py) - Demonstrates how to run a elastic reverse time migration (RTM).
5. [batch_demo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/batch_demo.py) - Demonstrates how to run acoustic forward models in batch mode.

### Full Documentation
* [gaiaseismic.cloud](https://gaiaseismic.cloud/) - WIP

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact Vorticity

* <hello@vorticity.xyz>
* <info@vorticity.xyz>


