# vLLM performance
```bash
$ docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
$ docker run -it --privileged --network=host --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
$ cd ~
# git clone https://github.com/ROCm/MAD
# cd MAD/scripts/vllm
# ./vllm_benchmark_report.sh -s throughput -m deepseek-ai/deepseek-moe-16b-chat -g 1 -d float16

```
