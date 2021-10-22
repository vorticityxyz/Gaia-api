# Vorticity Gaia API

Vorticity Gaia is a cloud compute service that provides lightning fast computing for seismic imaging problems such as FWI, RTM etc. using custom silicon accelerators on the cloud. These accelerators are built from the ground up to solve scientific computing problems and can be a few orders or magnitude faster than typical consumer GPU and CPU based system. This open source API allows users to connect to this service using well established seismic operators.

NOTE: For full functionality, contact Vorticity to set up your account. 

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

```bash
python3 -m pip install segyio
```

## Installation

1. Clone the public git repository to your working directory.

```bash
git clone https://github.com/VorticityXYZ/GaiaAPI
```

2. Contact Vorticity (<hello@vorticity.xyz>) to setup your account and receive the required authetication and encryption files.

3. Copy these files to your working directory.

## Usage

### Documentation

* [gaiaseismic.cloud](https://gaiaseismic.cloud/) - WIP

### Examples

We provide serveral examples here to get you started. If you have any questions, please feel free to contact us.

#### Forward examples

1. [demo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/demo.py) - Demonstrates how to run a forward model using the acousitic wave equations.
2. [mdemo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/mdemo.py) - Demonstrates how to run a large (1 billion grid points +) forward model using the acousitic wave equations. Will require special access.

3. [edemo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/edemo.py) - Demonstrates how to run a forward model using the elastic wave equations.

#### RTM examples

1. [demo2.py](https://github.com/vorticityxyz/Gaia-api/blob/main/demo2.py) - Demostrates how to run a acoustic reverse time migration (RTM) .

2. [edemo2.py](https://github.com/vorticityxyz/Gaia-api/blob/main/edemo2.py) - Demonstrates how to run a elastic reverse time migration (RTM).

#### Remote/batch operators

1. [remote_demo.py](https://github.com/vorticityxyz/Gaia-api/blob/main/remote_demo.py) - Demonstrates several operators useful in gathering shots from a large survey.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact Vorticity

* <hello@vorticity.xyz>
* <info@vorticity.xyz>