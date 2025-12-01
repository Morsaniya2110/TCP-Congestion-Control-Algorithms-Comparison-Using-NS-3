```markdown
# **TCP Congestion Control Performance Analysis using NS-3**

This repository presents a complete performance evaluation of four TCP congestion control algorithms in **NS-3**: **TcpNewReno**, **TcpVegas**, **TcpCubic**, and **TcpBbr**.
The analysis includes **Throughput**, **End-to-End Delay**, and **Jain’s Fairness Index**, along with **graphical visualizations** using Python.

---

## **1. Project Overview**

This project investigates how modern TCP variants behave under identical network conditions. The simulation environment is built in NS-3, FlowMonitor is used to capture performance metrics, and Python scripts are used to visualize results.

---

## **2. Key Features**

* **NS-3 simulation script** for running different TCP algorithms
* **FlowMonitor output parsing** for extracting accurate statistics
* **Throughput comparison graphs**
* **Delay comparison graphs**
* **Jain’s Fairness Index calculation**
* **Time-series throughput graphs**
* **CWND visualization** (if enabled)

---

## **3. Algorithms Evaluated**

* **TcpNewReno** — Loss-based AIMD algorithm
* **TcpVegas** — Delay-based congestion detection
* **TcpCubic** — Default Linux congestion control
* **TcpBbr** — Model-based, bottleneck bandwidth estimation

---

## **4. Repository Structure**

```

project/
│
├── ns3/
│   └── scratch-tcp-compare.cc
│
├── results/
│   ├── tcp-TcpNewReno-flow.xml
│   ├── tcp-TcpVegas-flow.xml
│   ├── tcp-TcpCubic-flow.xml
│   └── tcp-TcpBbr-flow.xml
│
├── python/
│   ├── plot_compare.py
│   └── plot_time_graphs.py
│
└── README.md

```

---

## **5. Running the NS-3 Simulations**

Run all algorithms one by one:

```

./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpNewReno"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpVegas"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpCubic"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpBbr"

```

Each execution generates a FlowMonitor XML file inside the project root:

```

tcp-TcpNewReno-flow.xml
tcp-TcpVegas-flow.xml
tcp-TcpCubic-flow.xml
tcp-TcpBbr-flow.xml

```

---

## **6. Running the Python Analysis**

### **A. Generate Throughput, Delay, and Fairness Graphs**

```

python3 plot_compare.py

```

### **B. Generate Time-Series Throughput and CWND Graphs**

```

python3 plot_time_graphs.py

```

Outputs include:

* `throughput_comparison.png`
* `delay_comparison.png`
* `fairness.txt`
* `throughput_vs_time.png`
* `cwnd_vs_time.png` (if enabled in NS-3)

---

## **7. Performance Metrics**

This project evaluates:

* **Throughput (Mbps)**
* **End-to-End Delay (seconds)**
* **Jain’s Fairness Index**
* **Throughput vs Time**
* **Congestion Window (CWND)**

---

## **8. Observations (General Expectations)**

* **TcpCubic** and **TcpNewReno** typically achieve **higher throughput**.
* **TcpVegas** maintains **lower delays** due to its delay-based congestion detection.
* **TcpBbr** provides **stable throughput** with advanced bandwidth estimation.
* Fairness results depend on bandwidth sharing between flows.

---

## **9. Research Reference**

If this work is based on a research paper, you may include a reference such as:

```

[1] Cardwell, N., Cheng, Y., Gunn, C., Yeganeh, S., & Jacobson, V.
“BBR: Congestion-Based Congestion Control.” ACM SIGCOMM.

```

Replace with the exact publication you used.

---

## **10. Tools and Technologies**

* **NS-3 (v3.41)**
* **C++** (for simulation logic)
* **FlowMonitor**
* **Python** (Pandas, Matplotlib)

---

## **11. Learning Outcomes**

Through this project, the following concepts were explored:

* Understanding the behavior of different TCP variants
* Implementing simulation environments in NS-3
* Extracting insights from FlowMonitor XML statistics
* Plotting comparative performance graphs
* Evaluating fairness among competing flows
```
