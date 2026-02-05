[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## A fixed Manthan

This is an attempt at actually making the
[Manthan](https://github.com/meelgroup/manthan) repository by Priyanka Golia,
Subhajit Roy and Kuldeep S. Meel available to public, and usable. The original
repository is too brittle to be used as-is. In the orignal code, none of the subcalls
are checked for return values, i.e. `os.system` calls are made without checking for
success or failure. This version attempts to fix those issues, and make the
code more robust. Furthermore, the original system links libabc.a statically,
which will place certain static variables in the same exact memory location if you run
the binary again, which will lead to unexpected crashes in multiprocess (not
just multi-threaded) environments. This version builds libabc with `-fPIC` and
links it dynamically to avoid that issue. Furthermore, this system actually
uses a single core for learning, by setting `os.environ["OMP_NUM_THREADS"] = "1"`
before importing numpy. The original system would use all available cores
for learning.

## Install

```shell
apt-get install build-essential cmake libboost-program-options-dev libreadline-dev libgmp-dev python3-venv git
git clone https://github.com/meelgroup/manthan
cd manthan
git submodule update --init --recursive
python3 -m venv manthan-venv
source manthan-venv/bin/activate
python -m pip install -r requirements.txt
./configure_dependencies.sh --all
```

You can clean the whole setup by running:

```shell
./configure_dependencies.sh --all --clean
```

Which will lead to `git status` reporting that everything is clean.

## How to Use

After building:

```shell
$ source manthan-venv/bin/activate
$ python manthan.py  myfile.qdimacs
c make to preprocess succeeded
c preprocess exists.
c WARNING: Empty line at line number 303 -- this is not part of the DIMACS specifications (http://www.satcompetition.org/2009/format-benchmarks2009.html). Ignoring.
c configuring dependency paths
c starting Manthan
c parsing
c count X (universally quantified variables) variables 8
c count Y (existentially quantified variables) variables 87
c preprocessing: finding unates (constant functions)
c count of positive unates 11
c count of negative unates 8
c finding uniquely defined functions
c count of uniquely defined variables 59
c generating samples
c generated samples.. learning candidate functions via decision learning
c generated candidate functions for all variables.
c verification check UNSAT
c no more repair needed
c number of repairs needed to converge 98
c Total time taken 4.825810670852661
Skolem functions are stored at factorization8_skolem.v
```

## Results

You will find two directories here, with the logfiles of two runs of Manthan on
the [CNF benchmarks](https://zenodo.org/records/3892859#.XuTB2XUzZhE) published by the authors:
```
 out-manthan-873994-0
 out-manthan-876346-0
```
The first directory contains a run with a memory limit of 10GB, the second with
a memory limit of 20GB (and open-wbo compiled in release mode). The
`.out_manthan` files contain the logs of the runs by the tool itself, and the
`.timeout_manthan` files contain the logs from the `/usr/bin/time -v` command
that was used to measure time and memory consumption of the python process.
Notice that the python process launches subprocesses, and the 10GB and 20GB
limits were imposed only on a per-process basis, hence the total memory
consumption can be up to 2x that, given that the manthan.py process typically
has one subprocess running at any time.

## Original Authors
* Priyanka Golia (pgoila@cse.iitk.ac.in)
* Subhajit Roy (subhajit@cse.iitk.ac.in)
* Kuldeep Meel (meel@comp.nus.edu.sg)
