# telemetry_sim.py
# Simulates a drone sending video frames and telemetry to the Snapdragon PC

import time
import random

def simulate_drone_stream():
    print("[DRONE] Link established. Starting transmission to Ground Station...")
    
    for frame_id in range(1, 6):
        # Simulate varying distances of obstacles
        simulated_distance = round(random.uniform(1.5, 8.0), 1)
        ping = random.randint(12, 25)
        
        print(f"[DRONE] Packet {frame_id} sent. (Telemetry Ping: {ping}ms)")
        time.sleep(1.5) # Simulate frame delay

if __name__ == "__main__":
    simulate_drone_stream()
