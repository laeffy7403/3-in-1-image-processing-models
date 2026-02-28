#!/usr/bin/env python3
"""
Integrated Launcher — Final_Group4
Shows a menu and runs the selected model in the same terminal.

Usage (from Final_Group4/, with root .venv activated):
    python launch.py
"""

import subprocess
import sys
import os

# ─── Path Configuration ───────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

MODELS = [
    {
        "label":  "CNN  — ResNet18 Flask Web App  (http://127.0.0.1:5000)",
        "script": "app.py",
        "cwd":    os.path.join(ROOT, "Model_CNN"),
    },
    {
        "label":  "YOLO — Object Tracker          (video / webcam menu)",
        "script": "track_yolo.py",
        "cwd":    os.path.join(ROOT, "Model_YOLO"),
    },
    {
        "label":  "MobileNet — Webcam Breed Predictor",
        "script": "mobilenet_predict.py",
        "cwd":    os.path.join(ROOT, "Model_MobileNet", "AI_MobileNet"),
    },
]


def print_menu():
    print()
    print("=" * 55)
    print("        AI Model Launcher — Final Group 4")
    print("=" * 55)
    for i, m in enumerate(MODELS, 1):
        print(f"  {i}. {m['label']}")
    print("  0. Exit")
    print("=" * 55)


def run_model(model_cfg):
    script_path = os.path.join(model_cfg["cwd"], model_cfg["script"])
    if not os.path.isfile(script_path):
        print(f"\n  ❌  Script not found: {script_path}\n")
        return

    print(f"\n  ▶  Starting: {model_cfg['label']}")
    print("  (Press Ctrl+C to stop and return to menu)\n")

    try:
        # subprocess.run inherits stdin/stdout/stderr — fully interactive
        subprocess.run(
            [PYTHON, script_path],
            cwd=model_cfg["cwd"],
        )
    except KeyboardInterrupt:
        print("\n\n  🛑  Stopped. Returning to menu...")


def main():
    while True:
        print_menu()
        try:
            choice = input("  Select (0–3): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Goodbye!")
            break

        if choice == "0":
            print("\n  Goodbye!")
            break
        elif choice in ("1", "2", "3"):
            run_model(MODELS[int(choice) - 1])
        else:
            print("\n  ⚠️  Invalid choice. Enter 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()
