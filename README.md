# python-parallel

 Some experiments with python concurrency and parallelism

## Run

- Setup:

```bash
make setup
```

- Run:

```bash
source venv/bin/activate
cd cpu_bound
python -u count_with_pool.py
```

## CPU Bound Applications

CPU-bound, meaning access to the CPU is the main bottleneck, use multi-processing.

## I/O Bound Applications

It makes more sense to use multi-threading rather than using multi-processing because:

- The application is not CPU-bound, and thus the extra overhead from multi-processing is not worth it.
- The threads communicate between each other, which would induce additional overhead and complexity when used with multi-processing.

### Python GIL

Global Interpreter Lock (GIL) manages concurrent access to the Python interpreter. This lock becomes effective for multi-threaded applications, making sure that only one thread at a time is allowed to run Python code. Due to this, every multi-threaded Python application effectively is single-core.

## References

[Comprehensive Guide to Concurrency and Parallelism in Python](https://towardsdatascience.com/comprehensive-guide-to-concurrency-and-parallelism-in-python-415ee5fbec1a)
