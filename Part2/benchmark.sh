sudo apt-get update

sudo apt-get install build-essential

sudo apt install git-all

git clone https://github.com/arihant15/Performance-Evaluation-Benchmark.git

cd Performance-Evaluation-Benchmark/CPU

gcc -pthread -o CPUBenchmark CPUBenchmark.c

./CPUBenchmark 100000 10
