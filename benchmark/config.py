# Number of benchmark runs for each configuration
NUM_RUNS = 5
SHOW_MODEL_OUTPUT = False
SAVE_MODEL_OUTPUT = True
WARMUP = True

# Temperature values to benchmark
TEMPERATURES = [
    0.0,
    0.2,
    0.4,
    0.6,
]

# Models to benchmark
MODELS = [
    "phi3:mini",
    "llama3.2:latest",
    "mistral:latest",
]