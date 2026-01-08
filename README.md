# FLUX.2-dev with ComfyUI

A setup for running FLUX.2-dev image generation using ComfyUI.

## Requirements

- Python 3.10 or higher
- Hugging Face account with access to FLUX.2-dev model
- At least 20GB of free disk space for the model
- GPU with at least 12GB VRAM (recommended) or Mac with Apple Silicon

## Setup Instructions

### 1. Install Python Dependencies

First, install the basic requirements for the setup script:

```bash
pip install -r requirements.txt
```

### 2. Configure Hugging Face Token

Copy the example environment file and add your Hugging Face token:

```bash
cp .env.example .env
```

Edit `.env` and replace `your_huggingface_token_here` with your actual Hugging Face token.

To get a token:
1. Go to https://huggingface.co/settings/tokens
2. Create a new token with read access
3. Make sure you have accepted the FLUX.2-dev model license at https://huggingface.co/black-forest-labs/FLUX.2-dev

### 3. Install ComfyUI Dependencies

```bash
cd ComfyUI
pip install -r requirements.txt
cd ..
```

### 4. Download FLUX.2-dev Model

Run the setup script to download the model:

```bash
python setup_flux.py
```

This will download the FLUX.2-dev model to `ComfyUI/models/diffusion_models/FLUX.2-dev/`

## Running ComfyUI

### Option 1: Using the run script

```bash
python run_comfyui.py
```

### Option 2: Manual launch

```bash
cd ComfyUI
python main.py --port 6000
```

ComfyUI will be available at: http://localhost:6000

## Using FLUX.2-dev in ComfyUI

1. Open ComfyUI in your browser at http://localhost:6000
2. Load a FLUX workflow or create a new one
3. In the checkpoint/model loader node, select the FLUX.2-dev model
4. Enter your prompt and generate images

## Recommended ComfyUI Workflows for FLUX

You can find FLUX-specific workflows at:
- https://comfyanonymous.github.io/ComfyUI_examples/flux/
- ComfyUI community workflows tagged with "FLUX"

## Troubleshooting

### Out of Memory Errors

If you encounter CUDA out of memory errors:
- Try using the `--lowvram` flag: `python main.py --port 6000 --lowvram`
- Or for extreme cases: `python main.py --port 6000 --novram`

### Model Not Found

Make sure the model was downloaded successfully to:
`ComfyUI/models/diffusion_models/FLUX.2-dev/`

### Port Already in Use

If port 6000 is already in use, edit `run_comfyui.py` and change the port number.

## Directory Structure

```
Flux.2-dev/
├── .env                    # Your HF token (create from .env.example)
├── .env.example           # Template for .env
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies for setup
├── setup_flux.py         # Script to download FLUX.2-dev
├── run_comfyui.py        # Script to run ComfyUI
├── README.md             # This file
└── ComfyUI/              # ComfyUI installation
    └── models/
        └── diffusion_models/
            └── FLUX.2-dev/   # Downloaded model
```

## Additional Resources

- ComfyUI Documentation: https://github.com/comfyanonymous/ComfyUI
- FLUX.2-dev Model: https://huggingface.co/black-forest-labs/FLUX.2-dev
- ComfyUI Examples: https://comfyanonymous.github.io/ComfyUI_examples/
# Flux.2.slyd
