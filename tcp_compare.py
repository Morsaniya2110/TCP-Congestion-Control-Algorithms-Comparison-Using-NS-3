import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Parse XML File
# ------------------------------
def parse_flow(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for flow in root.findall("FlowStats/Flow"):
        tx = int(flow.attrib["txBytes"])
        rx = int(flow.attrib["rxBytes"])

        delay_str = flow.attrib["delaySum"].replace("ns", "")
        delay = float(delay_str) / 1e9   # convert ns → sec

        throughput = (rx * 8) / 5e6  # Mbps (5-second simulation)

        return throughput, delay

# ------------------------------
# Your XML Files (Correct Names)
# ------------------------------
algorithms = {
    "Reno":  "tcp-TcpNewReno-flow.xml",
    "Vegas": "tcp-TcpVegas-flow.xml",
    "Cubic": "tcp-TcpCubic-flow.xml",
    "BBR":   "tcp-TcpBbr-flow.xml"
}

results = {"Algorithm": [], "Throughput": [], "Delay": [], "Fairness": []}

# ------------------------------
# Read Values
# ------------------------------
for algo, file in algorithms.items():
    thr, delay = parse_flow(file)
    results["Algorithm"].append(algo)
    results["Throughput"].append(thr)
    results["Delay"].append(delay)

# ------------------------------
# Jain Fairness Index
# ------------------------------
thr_array = np.array(results["Throughput"])
fairness = (thr_array.sum() ** 2) / (len(thr_array) * (thr_array**2).sum())

results["Fairness"] = [fairness] * len(thr_array)

# ------------------------------
# Aesthetic Settings
# ------------------------------
plt.style.use("seaborn-v0_8-darkgrid")
colors = ["#00b4d8", "#ff6b6b", "#90be6d", "#ffd166"]

# ------------------------------
# Plot: Throughput
# ------------------------------
plt.figure(figsize=(8,6))
bars = plt.bar(results["Algorithm"], results["Throughput"], color=colors)
plt.title("TCP Congestion Control Comparison – Throughput", fontsize=16, fontweight="bold")
plt.ylabel("Throughput (Mbps)", fontsize=14)

# labels inside bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, 
             bar.get_height()/2,
             f"{bar.get_height():.2f}",
             ha="center", va="center", color="white", fontsize=12, fontweight="bold")

plt.savefig("throughput.png")
plt.close()

# ------------------------------
# Plot: Delay
# ------------------------------
plt.figure(figsize=(8,6))
bars = plt.bar(results["Algorithm"], results["Delay"], color=colors)
plt.title("TCP Congestion Control Comparison – Delay", fontsize=16, fontweight="bold")
plt.ylabel("End-to-End Delay (seconds)", fontsize=14)

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height()/2,
             f"{bar.get_height():.4f}",
             ha="center", va="center", color="black", fontsize=12, fontweight="bold")

plt.savefig("delay.png")
plt.close()

# ------------------------------
# Plot: Fairness (Single Value)
# ------------------------------
plt.figure(figsize=(8,6))
bars = plt.bar(results["Algorithm"], results["Fairness"], color=colors)
plt.title("Jain Fairness Index (Throughput-Based)", fontsize=16, fontweight="bold")
plt.ylabel("Fairness Score", fontsize=14)

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height()/2,
             f"{bar.get_height():.4f}",
             ha="center", va="center", color="black", fontsize=12, fontweight="bold")

plt.savefig("fairness.png")
plt.close()

print("Graphs generated:")
print(" - throughput.png")
print(" - delay.png")
print(" - fairness.png")
