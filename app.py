# app.py
# Snapdragon Edge-Compute Ground Station
# This script demonstrates using the Snapdragon PC as the local AI processing hub.

import qai_hub as hub
import time

def load_vision_model():
    print("[SYSTEM] Initializing Snapdragon NPU...")
    print("[SYSTEM] Loading optimized YOLO vision model from Qualcomm AI Hub...")
    # Pulls the pre-quantized object detection model from the AI Hub
    model = hub.get_model("yolo-v8-det-quantized") 
    return model

def process_camera_feed(model, frame_data):
    print("[NPU] Processing live video frame locally (Zero Cloud Latency)...")
    # Simulate the Snapdragon NPU detecting an object
    simulated_detection = {"object": "Obstacle", "distance_meters": 2.5, "position": "center"}
    return simulated_detection

def send_telemetry_command(detection):
    # Bridge to the telemetry radio/flight controller
    if detection["object"] == "Obstacle" and detection["distance_meters"] < 3.0:
        command = "EMERGENCY_STOP & HOVER"
    else:
        command = "PROCEED_FORWARD"
        
    print(f"[RADIO] Transmitting command to Flight Controller: {command}")
    return command

if __name__ == "__main__":
    print("--- Snapdragon AI Ground Station ---")
    
    # 1. Load the pre-trained Qualcomm model onto the NPU
    ai_hub_model = load_vision_model()
    
    # 2. Simulate receiving a live video frame from the drone
    live_frame = "simulated_pixel_data"
    
    # 3. Analyze the frame on the NPU
    target_data = process_camera_feed(ai_hub_model, live_frame)
    print(f"[NPU] AI identified: {target_data['object']} at {target_data['distance_meters']}m")
    
    # 4. Transmit flight instructions to the hardware
    send_telemetry_command(target_data)
