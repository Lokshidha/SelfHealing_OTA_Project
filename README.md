# Self-Healing OTA ECU System

A smart and simple demo project that simulates Over-the-Air (OTA) updates for Electronic Control Units (ECUs) with automatic crash detection and rollback recovery.

## Project Summary

This project solves the problem of ECU failures due to faulty software updates. It ensures system reliability by rolling back to the last stable version if a crash is detected after an OTA update.

## Objective

To simulate a self-healing OTA mechanism that:
- Applies ECU software updates
- Detects crashes after a bad update
- Automatically rolls back to the previous stable version


## Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **File Handling:** For backup & restore
- **Structure:**
  - `ecu_simulator.py` – logic for version handling and rollback
  - `gui_launcher.py` – user interface
  - `updates/` – contains `version1.py` (stable) & `version2.py` (buggy)
  - `backup/` – holds backup version of ECU software

##  How to Run

1. Install Python (if not already) (or) Open in VS code -> new terminal
2. Run `gui_launcher.py`
3. Click “Start OTA Update”
4. Observe the OTA simulation and rollback behavior

## Future Scope

- Connect to real-time hardware (e.g., Raspberry Pi)
- Enable cloud-based remote updates
- Add machine learning for predictive crashes

