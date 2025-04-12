
# update_manager.py

import shutil
from ecu_simulator import run_ecu

def backup_current_version():
    try:
        shutil.copy("updates/version1.py", "backup/version_backup.py")
        print("🗂️ Backup of Version 1 created.")
    except Exception as e:
        print("❌ Backup Failed:", e)

def apply_update(new_version_path):
    print("\n🚀 Starting OTA Update...")
    try:
        run_ecu(new_version_path)
        print("✅ OTA Update Applied Successfully!")
        shutil.copy(new_version_path, "backup/version_backup.py")
    except Exception as e:
        print("\n❌ Update Failed! Rolling back to last stable version...")
        try:
            run_ecu("backup/version_backup.py")
            print("🔁 Rollback successful. ECU is now running the stable version.")
        except Exception as rollback_error:
            print("❌ Rollback also failed:", rollback_error)

# Start simulation
backup_current_version()
apply_update("updates/version2.py")
