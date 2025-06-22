# hipify
```bash
$ hipify-perl -examine nbody-orig.cu
$ hipify-perl nbody-orig.cu > nbody-orig.cpp
$ hipcc -DSHMOO nbody-orig.cpp -o nbody-orig
$ ./nbody-orig
```

## References
https://github.com/amd/HPCTrainingExamples/tree/main/HIPIFY
