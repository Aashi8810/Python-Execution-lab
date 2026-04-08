# 🚀 Python Execution Lab

A hands-on exploration of Python’s execution model through controlled performance experiments covering CPU, I/O, memory, concurrency, and profiling.

---

## 📌 Overview

This project investigates how Python behaves under different execution scenarios by designing and running five focused micro-experiments.

Rather than relying on theoretical explanations, each experiment is built to **measure, compare, and explain real performance behavior**.

---

## 🎯 Objectives

- Understand Python’s execution model  
- Analyze CPU-bound vs I/O-bound workloads  
- Explore threading, multiprocessing, and async  
- Investigate memory usage patterns  
- Learn profiling and performance optimization  

---

## 🧪 Experiments

### 1️⃣ Threading vs Multiprocessing (CPU-bound)

**Goal:**  
Understand how Python utilizes CPU cores.

**Key Findings:**

- Threading does **not** improve CPU-bound performance due to the GIL  
- Multiprocessing enables **true parallelism**  
- Overhead matters for small workloads  

---

### 2️⃣ Async I/O vs Blocking I/O

**Goal:**  
Compare execution models for I/O-bound workloads.

**Key Findings:**

- Blocking I/O scales poorly (linear delay)  
- Threading improves throughput by overlapping waits  
- Async achieves similar performance with **lower overhead**  

---

### 3️⃣ Lists vs Generators (Memory Behavior)

**Goal:**  
Analyze memory allocation strategies.

**Key Findings:**

- Lists allocate all data upfront → **high memory usage (~500MB)**  
- Generators use lazy evaluation → **constant memory (~60MB)**  
- Generators can also improve performance due to reduced allocation overhead  

---

### 4️⃣ GIL Impact Demonstration

**Goal:**  
Explicitly observe Python’s Global Interpreter Lock.

**Key Findings:**

- Multiple threads do **not** execute CPU-bound code in parallel  
- CPU utilization remains limited to a single core  
- Threads provide concurrency, not parallelism  

---

### 5️⃣ Profiling and Optimization

**Goal:**  
Identify and optimize performance bottlenecks.

**Key Findings:**

- `cProfile` identifies slow functions  
- `line_profiler` pinpoints slow lines  
- Effective optimization requires **measurement, not intuition**  

---


