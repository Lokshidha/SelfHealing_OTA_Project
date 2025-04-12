# ecu_simulator.py
import importlib.util

def run_ecu(version_path):
    spec = importlib.util.spec_from_file_location("ecu", version_path)
    ecu = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ecu)
    ecu.run()  # ❗Do NOT wrap this in try-except here
