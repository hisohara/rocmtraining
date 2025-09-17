# Installation of PyTorch on ROCm
## Wheels package
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.4
$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.version.hip
'6.4.43484-123eb5128'
```

## Docker images
```bash
# $ docker pull rocm/pytorch:rocm6.4.1_ubuntu24.04_py3.12_pytorch_release_2.5.1
# $ docker run -it --privileged --network=host --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host rocm/pytorch:rocm6.4.1_ubuntu24.04_py3.12_pytorch_release_2.5.1
$ docker pull rocm/pytorch:rocm6.4.1_ubuntu24.04_py3.12_pytorch_release_2.7.1
$ docker run -it --privileged --network=host --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host rocm/pytorch:rocm6.4.1_ubuntu24.04_py3.12_pytorch_release_2.7.1
# python
Python 3.12.10 | packaged by conda-forge | (main, Apr 10 2025, 22:21:13) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.version.hip
'6.4.43483-a187df25c'
```
