# Snapdragon-AI-Drone
Offloads UAV AI vision to a Snapdragon PC NPU using Qualcomm AI Hub. The PC processes live video offline and sends telemetry flight commands to the drone hardware, ensuring zero cloud latency and saving drone battery.
# Snapdragon Edge-Compute Ground Station

This project bridges the raw edge-computing power of a Snapdragon PC with physical drone hardware. It offloads heavy AI vision tasks from the drone to the PC's NPU using the Qualcomm AI Hub, preserving drone battery life and operating entirely offline.

## 💻 Simulated Execution (Input / Output)

**Input:** Raw live camera frames received via telemetry radio.
**Processing (NPU):** Runs `yolo-v8-det-quantized` natively on the Snapdragon Hexagon NPU.
**Output System Log:**

```text
--- Snapdragon AI Ground Station ---
[SYSTEM] Initializing Snapdragon NPU...
[SYSTEM] Loading optimized YOLO vision model from Qualcomm AI Hub...
[NPU] Processing live video frame locally (Zero Cloud Latency)...
[NPU] AI identified: Obstacle at 2.5m
[RADIO] Transmitting command to Flight Controller: EMERGENCY_STOP & HOVER
**2. requirements.txt (Dependencies dikhane ke liye)**
Phir se `Add file` -> `Create new file` karo. Naam `requirements.txt` likho aur yeh chota sa text paste karke **Commit changes** dabao:

```text
qai-hub>=0.11.0
pyserial>=3.5
opencv-python>=4.9.0
