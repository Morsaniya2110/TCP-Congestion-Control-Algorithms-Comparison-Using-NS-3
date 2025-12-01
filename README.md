# TCP Congestion Control Performance Analysis using NS-3

## Project Overview
Evaluates **TcpNewReno**, **TcpVegas**, **TcpCubic**, and **TcpBbr** in NS-3. Metrics include:

- Throughput (Mbps)  
- End-to-End Delay (s)  
- Jain’s Fairness Index  
- CWND & Time-series throughput  

---

## Key Features
- NS-3 simulation scripts  
- FlowMonitor metrics collection  
- Python visualization (Matplotlib)  
- Comparative analysis of TCP variants  

---

## TCP Algorithms

| Algorithm     | Type        | Notes                              |
|---------------|------------|-----------------------------------|
| TcpNewReno    | Loss-based | AIMD-based                        |
| TcpVegas      | Delay-based| RTT-based congestion detection     |
| TcpCubic      | Loss-based | Default Linux TCP                 |
| TcpBbr        | Model-based| Bandwidth estimation               |

---
## Repository Structure

project/
├── ns3/scratch-tcp-compare.cc
├── results/*.xml
├── python/plot_compare.py
├── python/plot_time_graphs.py

---

## Running Simulations

```bash
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpNewReno"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpVegas"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpCubic"
./ns3 run "scratch/scratch-tcp-compare.cc --tcpType=TcpBbr"

```
## Python Analysis
```base
python3 python/plot_compare.py       # Comparison graphs
python3 python/plot_time_graphs.py   # Time-series graphs
```


