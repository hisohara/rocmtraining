import torch
import time

def benchmark_matmul(backend: str,
                     size: int = 8192,
                     dtype: torch.dtype = torch.float16,
                     iters: int = 20):
    torch.backends.cuda.preferred_blas_library(backend)  # :contentReference[oaicite:0]{index=0}

    device = 'cuda'
    a = torch.randn(size, size, dtype=dtype, device=device)
    b = torch.randn(size, size, dtype=dtype, device=device)

    # Warm-up
    for _ in range(5):
        torch.matmul(a, b)
    torch.cuda.synchronize()

    start = time.time()
    for _ in range(iters):
        torch.matmul(a, b)
    torch.cuda.synchronize()
    total = time.time() - start

    avg_ms = total / iters * 1000
    dtype_str = str(dtype).split('.')[-1]  # 'torch.float16' → 'float16'
    print(f'backend={backend:10s} | size={size:>4d} | dtype={dtype_str:6s} | '
          f'avg {avg_ms:6.4f} ms over {iters} iters')

if __name__ == '__main__':
    backends = ['hipblas', 'hipblaslt', 'ck']
    for bk in backends:
        benchmark_matmul(bk)
