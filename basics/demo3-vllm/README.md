# vLLM performance
https://github.com/ROCm/MAD/tree/develop/benchmark/vllm#standalone-benchmarking

```bash
$ docker pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
$ docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
root@ab648041505a:~# more run.sh
#!/bin/bash

export ROCR_VISIBLE_DEVICES="1"

model=amd/Llama-3.1-8B-Instruct-FP8-KV
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=8192
max_model_len=131072

vllm bench throughput --model $model \
    -tp $tp \
    --num-prompts $num_prompts \
    --input-len $in \
    --output-len $out \
    --dtype $dtype \
    --kv-cache-dtype $kv_cache_dtype \
    --max-num-seqs $max_num_seqs \
    --max-seq-len-to-capture $max_seq_len_to_capture \
    --max-num-batched-tokens $max_num_batched_tokens \
    --max-model-len $max_model_len \
    --trust-remote-code \
    --output-json throughput.json \
    --gpu-memory-utilization 0.9

```
