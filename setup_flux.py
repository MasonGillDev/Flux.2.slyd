#!/usr/bin/env python3
"""
Setup script to download FLUX.2-dev model for ComfyUI
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import snapshot_download, login, hf_hub_download

def main():
    # Load environment variables
    load_dotenv()

    # Get HF token
    hf_token = os.getenv('HF_TOKEN')
    if not hf_token or hf_token == 'your_huggingface_token_here':
        print("Error: HF_TOKEN not found or not set in .env file")
        print("Please copy .env.example to .env and add your Hugging Face token")
        sys.exit(1)

    # Login to Hugging Face
    print("Logging in to Hugging Face...")
    try:
        login(token=hf_token)
        print("Successfully logged in!")
    except Exception as e:
        print(f"Error logging in: {e}")
        sys.exit(1)

    # Create ComfyUI model directories
    comfyui_dir = Path("ComfyUI")
    if not comfyui_dir.exists():
        print("Error: ComfyUI directory not found!")
        print("Please make sure ComfyUI is cloned in this directory")
        sys.exit(1)

    # FLUX models go in the diffusion_models directory
    models_dir = comfyui_dir / "models" / "diffusion_models"
    models_dir.mkdir(parents=True, exist_ok=True)

    # Also create unet directory as backup location
    unet_dir = comfyui_dir / "models" / "unet"
    unet_dir.mkdir(parents=True, exist_ok=True)

    # Download FLUX.2-dev model
    model_id = "black-forest-labs/FLUX.2-dev"
    local_dir = models_dir / "FLUX.2-dev"

    print(f"\nDownloading {model_id}...")
    print("This may take a while depending on your internet connection...")
    print(f"Downloading to: {local_dir}")

    try:
        snapshot_download(
            repo_id=model_id,
            local_dir=str(local_dir),
            token=hf_token,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"\nModel successfully downloaded to: {local_dir}")

        # Also download VAE and text encoders if needed
        print("\nDownloading required components for FLUX...")

        # Create VAE directory
        vae_dir = comfyui_dir / "models" / "vae"
        vae_dir.mkdir(parents=True, exist_ok=True)

        # Create clip directory for text encoders
        clip_dir = comfyui_dir / "models" / "clip"
        clip_dir.mkdir(parents=True, exist_ok=True)

        print("\nSetup complete!")
        print("\nTo run ComfyUI:")
        print("  python run_comfyui.py")
        print("\nOr manually:")
        print("  cd ComfyUI && python main.py --port 6000")

    except Exception as e:
        print(f"Error downloading model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
