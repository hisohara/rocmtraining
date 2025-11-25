# vLLM demonstration
## vLLM serving (11/25/2025 on AMD Developer Cloud)
```bash
$ docker pull rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103
$ docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --privileged --device /dev/kfd --device /dev/dri rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103

# vllm serve Qwen/Qwen2-7B-Instruct
# curl http://localhost:8000/v1/completions     -H "Content-Type: application/json"     -d '{
        "model": "Qwen/Qwen2-7B-Instruct",
        "prompt": "Write a haiku about artificial intelligence",
        "max_tokens": 128,
        "top_p": 0.95,
        "top_k": 20,
        "temperature": 0.8
      }'| jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   801  100   586  100   215   3426   1257 --:--:-- --:--:-- --:--:--  4711
{
  "id": "cmpl-652043733fb24f9ca29c9a6d167eda41",
  "object": "text_completion",
  "created": 1764067224,
  "model": "Qwen/Qwen2-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "text": " in the style of William Shakespeare.\nMinds born of code and math,\nInquiry deep as human thought,\nAI doth ponder, learn, and play.",
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": null,
      "token_ids": null,
      "prompt_logprobs": null,
      "prompt_token_ids": null
    }
  ],
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "prompt_tokens": 7,
    "total_tokens": 40,
    "completion_tokens": 33,
    "prompt_tokens_details": null
  },
  "kv_transfer_params": null
}
```

## vLLM performance
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
