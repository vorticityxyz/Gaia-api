# Description:
#
# WARNING!!! This file is a critical component of Vorticity Gaia API for seismic imaging
# PLEASE DO NOT MODIFY
#
# (C) Vorticity Inc. Mountain View, CA 2021
# Licence: MIT

# Validation parameters
MAX_DIM = 1024
MIN_DIM = 10
MAX_STEPS = 100000
MIN_STEPS = 10
MAX_BLOCK = 10000
MIN_BLOCK = 10
MAX_BOX = 2000
MIN_BOX = 10

# Vallidate the earth model for correct parameters
def model(model):
    # check if float32
    if (model.dtype != "float32"):
        raise Exception("Earth model must be of type float32.")

    # check if 3 dimensions
    if (model.ndim != 3):
        raise Exception("Earth model must be a three dimensional numpy array.")

    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    if ((nx > MAX_DIM) or (ny > MAX_DIM) or (nz > MAX_DIM)):
        raise Exception("Earth model cannot be larger than 1024 grid points in any dimension.")

    if ((nx < MIN_DIM) or (ny < MIN_DIM) or (nz < MIN_DIM)):
        raise Exception("Earth model cannot be smaller than 10 grid points in any dimension.")

# Validate earth model for multi card processing
def multicard_model(model, cnum):
    # check if float32
    if (model.dtype != "float32"):
        raise Exception("Earth model must be of type float32.")

    # check if 3 dimensions
    if (model.ndim != 3):
        raise Exception("Earth model must be a three dimensional numpy array.")

    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    if ((nx > (cnum * MAX_DIM)) or (ny > (cnum * MAX_DIM)) or (nz > (cnum * MAX_DIM))):
        raise Exception("Earth model dimensions exceeds maximum allowed. Check your setup.")

    if ((nx < MIN_DIM) or (ny < MIN_DIM) or (nz < MIN_DIM)):
        raise Exception("Earth model cannot be smaller than 10 grid points in any dimension.")

# Vallidate the earth block for batch processing
def block(block):
    # check if float32
    if (block.dtype != "float32"):
        raise Exception("Earth block must be of type float32.")

    # check if 3 dimensions
    if (block.ndim != 3):
        raise Exception("Earth block must be a three dimensional numpy array.")

    nx = block.shape[0]
    ny = block.shape[1]
    nz = block.shape[2]

    if ((nx > MAX_BLOCK) or (ny > MAX_BLOCK) or (nz > MAX_BLOCK)):
        raise Exception("Earth block cannot be larger than 10000 grid points in any dimension.")

    if ((nx < MIN_BLOCK) or (ny < MIN_BLOCK) or (nz < MIN_BLOCK)):
        raise Exception("Earth block cannot be smaller than 10 grid points in any dimension.")

# Validate earth model for rUpload
def remote_model(shape, dtype):
    # check if float32
    if (dtype != "float32"):
        raise Exception("Earth model must be of type float32.")

    # check if 3 dimensions
    if (len(shape) != 3):
        raise Exception("Earth model must be a three dimensional numpy array.")

    nx = shape[0]
    ny = shape[1]
    nz = shape[2]

    if ((nx > MAX_BLOCK) or (ny > MAX_BLOCK) or (nz > MAX_BLOCK)):
        raise Exception("Earth model cannot be larger than 10000 grid points in any dimension.")

    if ((nx < MIN_BLOCK) or (ny < MIN_BLOCK) or (nz < MIN_BLOCK)):
        raise Exception("Earth model cannot be smaller than 10 grid points in any dimension.")

# Validate that the shotbox for batch processing
def shotbox(block, shotbox):
    
    if (shotbox.dtype != "int32"):
        raise Exception("Shotbox values must be of type int32.")
    
    block_x = block.shape[0]
    block_y = block.shape[1]
    block_z = block.shape[2]

    shot_x = shotbox[0]
    shot_y = shotbox[1]
    shot_z = shotbox[2]

    if ((shot_x > MAX_BOX) or (shot_y > MAX_BOX) or (shot_z > MAX_BOX)):
        raise Exception("Shot box cannot be larger than 2000 grid points in any dimension.")

    if ((shot_x < MIN_BOX) or (shot_y < MIN_BOX) or (shot_z < MIN_BOX)):
        raise Exception("Shot box cannot be smaller than 10 grid points in any dimension.")

    if ((shot_x > block_x) or (shot_y > block_y) or (shot_z > block_z)):
        raise Exception("Shot box cannot be larger than block size in any dimension.")

# Validate the sweep values for batch processing
def sweep(block, shotbox, sweep):
    if (sweep.dtype != "int32"):
        raise Exception("Sweep parameters must be of type int32.")

    block_x = block.shape[0]
    block_y = block.shape[1]
    block_z = block.shape[2]

    shot_x = shotbox[0]
    shot_y = shotbox[1]
    shot_z = shotbox[2]

    x_start = sweep[0]
    x_end = sweep[1]
    x_step = sweep[2]
    y_start = sweep[3]
    y_end = sweep[4]
    y_step = sweep[5]

    if ((x_start < 0) or (y_start < 0)):
        raise Exception("Starting sweep values cannot be negative.")

    if ((x_start > x_end) or (y_start > y_end)):
        raise Exception("Starting sweep values cannot be larger than ending values.")

    if ((x_step < 0) or (y_step < 0)):
        raise Exception("Step values cannot be negative.")

    if (((x_end + shot_x) > block_x) or ((y_end + shot_y) > block_y)):
        raise Exception("The sweep must lie within the boundaries of the block")

# Vallidate the elastic model for correct parameters
def emodel(vp, vs, rho):
    # check if float32
    if (vp.dtype != "float32"):
        raise Exception("P velocity model must be of type float32.")
    if (vs.dtype != "float32"):
        raise Exception("S velocity model must be of type float32.")
    if (rho.dtype != "float32"):
        raise Exception("Density model must be of type float32.")

    # check if 3 dimensions
    if (vp.ndim != 3):
        raise Exception("P velocity model must be a three dimensional numpy array.")
    if (vs.ndim != 3):
        raise Exception("S velocity model must be a three dimensional numpy array.")
    if (rho.ndim != 3):
        raise Exception("Density model must be a three dimensional numpy array.")

    vpnx = vp.shape[0]
    vpny = vp.shape[1]
    vpnz = vp.shape[2]
    vsnx = vs.shape[0]
    vsny = vs.shape[1]
    vsnz = vs.shape[2]
    rhonx = rho.shape[0]
    rhony = rho.shape[1]
    rhonz = rho.shape[2]

    if ((vpnx > MAX_DIM) or (vpny > MAX_DIM) or (vpnz > MAX_DIM)):
        raise Exception("P velocity model cannot be larger than 1024 grid points in any dimension.")
    if ((vsnx > MAX_DIM) or (vsny > MAX_DIM) or (vsnz > MAX_DIM)):
        raise Exception("S velocity model cannot be larger than 1024 grid points in any dimension.")
    if ((rhonx > MAX_DIM) or (rhony > MAX_DIM) or (rhonz > MAX_DIM)):
        raise Exception("Denisty model cannot be larger than 1024 grid points in any dimension.")

    if ((vpnx < MIN_DIM) or (vpny < MIN_DIM) or (vpnz < MIN_DIM)):
        raise Exception("P Velocity model cannot be smaller than 10 grid points in any dimension.")
    if ((vsnx < MIN_DIM) or (vsny < MIN_DIM) or (vsnz < MIN_DIM)):
        raise Exception("S velocity model cannot be smaller than 10 grid points in any dimension.")
    if ((rhonx < MIN_DIM) or (rhony < MIN_DIM) or (rhonz < MIN_DIM)):
        raise Exception("Density model cannot be smaller than 10 grid points in any dimension.")

    if ((vpnx != vsnx) or (vpnx != rhonx)):
        raise Exception("P velocity, S velocity and Density models should all have the same dimensions.")
    if ((vpny != vsny) or (vpny != rhony)):
        raise Exception("P velocity, S velocity and Density models should all have the same dimensions.")
    if ((vpnz != vsnz) or (vpnz != rhonz)):
        raise Exception("P velocity, S velocity and Density models should all have the same dimensions.")

def shot(shot):
    # check if float32
    if (shot.dtype != "float32"):
        raise Exception("Shot profile must be of type float32.")

    # check if 1 dimension
    if (shot.ndim != 1):
        raise Exception("Shot profile must be a one dimensional numpy array.")

    nt = shot.shape[0]

    if (nt < MIN_STEPS):
        raise Exception("Shot profile must have at least 10 timestep.")

    if (nt > MAX_STEPS):
        raise Exception("Shot profile cannot have more than 100,000 timesteps")

def traces(traces, shot, model):
    # check if float32
    if (traces.dtype != "float32"):
        raise Exception("Traces must be of type float32.")

    # check if 3 dimensions
    if (traces.ndim != 3):
        raise Exception("Traces must be a 3 dimensional numpy array [time, x, y].")
    
    shot_nt = shot.shape[0]
    trace_nt = traces.shape[0]
    trace_nx = traces.shape[1]
    trace_ny = traces.shape[2]
    
    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    if (shot_nt != trace_nt):
        raise Exception("Shot and traces must have the same number of time steps.")

    if (trace_nx > nx):
        raise Exception("Traces cannot have a larger x dim than model.")
        
    if (trace_ny > ny):
        raise Exception("Traces cannot have a larger y dim than model.")

def shotxyz(model, shotxyz):

    if (shotxyz.dtype != "int32"):
        raise Exception("Integer parameters must be of type int32")
    
    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    xs = shotxyz[0]
    ys = shotxyz[1]
    zs = shotxyz[2]

    # Shot location must be positive
    if ((xs < 0) or (ys < 0) or (zs < 0)):
        raise Exception("Shot location must have positive coordinates.")

    if ((xs > nx) or (ys > ny) or (zs > nz)):
        raise Exception("Shot location must be within the boundaries of the domain")

def recxxyyz(model, recxxyyz):

    if (recxxyyz.dtype != "int32"):
        raise Exception("Integer parameters must be of type int32")

    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    xt1 = recxxyyz[0]
    xt2 = recxxyyz[1]
    yt1 = recxxyyz[2]
    yt2 = recxxyyz[3]
    zt = recxxyyz[4]

    if ((xt1 < 0) or (xt2 < 0) or (yt1 < 0) or (yt2 < 0) or (zt < 0)):
        raise Exception("Receiver locations must have positive coordinates.")

    if ((xt1 > nx) or (xt2 > nx) or (yt1 > ny) or (yt2 > ny) or (zt > nz)):
        raise Exception("Receiver locations must be within the boundaries of the domain.")

    if (xt1 > xt2):
        raise Exception("Receiver start location connot be before the end location.")

    if (yt1 > yt2):
        raise Exception("Receiver start location connot be before the end location.")

def deltas(deltas):

    if (deltas.dtype != "float32"):
        raise Exception("Float parameters must be of type float32")

    dx = deltas[0]
    dy = deltas[1]
    dz = deltas[2]
    dt = deltas[3]

    if ((dx <= 0.0) or (dy <= 0.0) or (dz <= 0.0)):
        raise Exception("dx dy dz must have positive and non zero values.")

    if (dt <= 0.0):
        raise Exception("dt must be positive and non zero.")

def pml(model, pml):
    
    if (pml.dtype != "int32"):
        raise Exception("PML parameters must be of type int32")

    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    pmlw = pml[0]
    pmla = pml[1]

    if (pmlw <= 0):
        raise Exception("PML must have a width greater than 0.")

    if ((pmlw > round(nx/2)) or (pmlw > round(ny/2)) or (pmlw > round(nz/2))):
        raise Exception("PML cannot be larger than the domain")
    
    if (pmla <= 0):
        raise Exception("PML magnitude must be greater than 0.")


def abc(model, abc):
    
    if (abc.dtype != "int32"):
        raise Exception("ABC parameters must be of type int32")

    nx = model.shape[0]
    ny = model.shape[1]
    nz = model.shape[2]

    abcw = abc[0]
    abca = abc[1]

    if (abcw <= 0):
        raise Exception("ABC must have a width greater than 0.")

    if ((abcw > round(nx/2)) or (abcw > round(ny/2)) or (abcw > round(nz/2))):
        raise Exception("ABC cannot be larger than the domain")
    
    if (abca <= 0):
        raise Exception("ABC magnitude must be greater than 0.")
