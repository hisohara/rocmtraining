# OpenMP GPU Offloading
## Install AMD Next Gen Fortran Compiler
https://github.com/amd/InfinityHub-CI/blob/main/fortran/README.md
```bash
# Case of Ubuntu
$ wget https://repo.radeon.com/rocm/misc/flang/rocm-afar-7992-drop-6.2.0-ubuntu.tar.bz2
$ tar zxvf rocm-afar-7992-drop-6.2.0-ubuntu.tar.bz2
$ export PATH=<path to install>/rocm-afar-<version>/bin:$PATH
$ export LD_LIBRARY_PATH=<path to install>/rocm-afar-<version>/lib:$LD_LIBRARY_PATH
```
## Evaluation of saxpy
https://github.com/amd/HPCTrainingExamples/tree/main/Pragma_Examples/OpenMP/Fortran/1_saxpy
```bash
$ export HSA_XNACK=1
$ cd 0_saxpy_serial_portyourself
$ amdflang -fopenmp saxpy.F90 -o saxpy
$ ./saxpy

$ cd ../1_saxpy_omptarget
$ amdflang -fopenmp --offload-arch=gfx942 saxpy.F90 -o saxpy
$ ./saxpy

$ cd ../2_saxpy_teamsdistribute
$ amdflang -fopenmp --offload-arch=gfx942 saxpy.F90 -o saxpy
$ ./saxpy

$ cd ../3_saxpy_paralleldosimd
$ amdflang -fopenmp --offload-arch=gfx942 saxpy.F90 -o saxpy
$ ./saxpy

$ cd ../4_saxpy_nousm
$ amdflang -fopenmp --offload-arch=gfx942 saxpy.F90 -o saxpy
$ ./saxpy

$ cd ../5_saxpy_map
$ amdflang -fopenmp --offload-arch=gfx942 saxpy.F90 -o saxpy
$ ./saxpy
```
