#!/usr/bin/env python3
"""
Run ComfyUI on port 6000
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    comfyui_dir = Path("ComfyUI")

    if not comfyui_dir.exists():
        print("Error: ComfyUI directory not found!")
        print("Please run this script from the Flux.2-dev directory")
        sys.exit(1)

    print("Starting ComfyUI on http://localhost:6000")
    print("Press Ctrl+C to stop")
    print()

    # Change to ComfyUI directory and run
    os.chdir(comfyui_dir)

    try:
        subprocess.run([
            sys.executable,
            "main.py",
            "--port", "6000",
            "--listen", "0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\nShutting down ComfyUI...")
    except Exception as e:
        print(f"Error running ComfyUI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
