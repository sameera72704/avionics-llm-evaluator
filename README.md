# Avionics LLM Evaluator

A small framework for testing how LLMs generate **embedded / avionics-style C code**.

The idea behind this project was simple:

**Can different models write safe, compilable embedded C code under different prompting conditions?**

To test that, I built a local evaluation pipeline using Ollama, static analysis checks, compilation testing, and benchmark reporting.

---

## What this project does

This project compares how different LLMs perform on embedded C programming tasks.

It evaluates:

* Code generation quality
* Compilation success
* Safety keyword coverage
* Forbidden API usage
* Prompting strategy impact

The benchmark currently tests multiple models and multiple prompt personas.

---

## Models Tested

* Mistral
* CodeLlama 7B

---

## Prompt Personas

### Strict

Embedded / avionics engineer style prompting.

Focuses on:

* MISRA-style behavior
* no dynamic allocation
* minimal unsafe patterns
* code-only outputs

### Neutral

Standard software engineering prompt.

### Permissive

Loose prompting with fewer restrictions.

Used to compare how prompt governance changes model behavior.

---

## Benchmark Tasks

Current task set:

### Task 001 — Altitude Clamp

Clamp a floating-point altitude value between:

```c
-500 and 50000 feet
```

### Task 002 — XOR Checksum

Generate an 8-bit checksum function.

### Task 003 — Ring Buffer Push

Generate a fixed-size ring buffer insertion function.

---

## Tech Stack

* Python
* Ollama
* Mistral
* CodeLlama
* Pandas
* Matplotlib
* GCC / Clang

---

## Project Structure

```plaintext
avionics-llm-evaluator/

fixtures/
    baseline_functions.json

src/
    prompts/
    evaluators/
    compilers/

reports/

test_full_pipeline.py
plot_results.py
generate_report.py
```

---

## Running the Project

Clone the repo:

```bash
git clone https://github.com/sameera72704/avionics-llm-evaluator.git
cd avionics-llm-evaluator
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Pull models:

```bash
ollama pull mistral
ollama pull codellama:7b
```

Run the benchmark:

```bash
python test_full_pipeline.py
```

Generate charts:

```bash
python plot_results.py
```

Generate dashboard:

```bash
python generate_report.py
```

---

## Outputs

The framework generates:

```plaintext
reports/results.csv
reports/benchmark_plot.png
reports/dashboard.html
```

---



## Future Improvements

Planned additions:

* more embedded benchmark tasks
* pytest automation
* richer scoring metrics
* Docker setup
* CI pipeline support
* additional model integrations

---

## Why I built this

I wanted a hands-on project that combines:

* LLM evaluation
* embedded systems concepts
* prompt engineering
* benchmarking / reporting

instead of building another generic chatbot demo.
