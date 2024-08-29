#!/usr/bin/env python3

# Github: https://github.com/huggingface/diffusers/tree/main?tab=readme-ov-file#new--stable-diffusion-is-now-fully-compatible-with-diffusers
# Quicktour: https://huggingface.co/docs/diffusers/quicktour

import sys
import argparse
import imageio

import torch
from diffusers import StableDiffusionPipeline
from diffusers import AutoPipelineForImage2Image
# from diffusers.utils import make_image_grid, load_image

model_id = "runwayml/stable-diffusion-v1-5"
negative_prompt = "ugly, deformed, disfigured, poor details, bad anatomy, blurred background"


def img_to_img(prompt, path_to_img):
    pipeline = AutoPipelineForImage2Image.from_pretrained(
        model_id, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    pipeline.enable_model_cpu_offload()

    # read image
    init_image = imageio.v2.imread(path_to_img)

    # pass prompt and image to pipeline
    image = pipeline(prompt, negative_prompt=negative_prompt, image=init_image).images[0]

    return image


def txt_to_img(prompt):
    pipeline = StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
    pipeline = pipeline.to("cuda")

    # image = pipeline(prompt).images[0]
    image = pipeline(prompt, negative_prompt=negative_prompt, strength=0.45, guidance_scale=10.5).images[0]

    return image


def main():
    parser = argparse.ArgumentParser(description = 'Call the stable difussion library to generate an image.')
    parser.add_argument('-p', '--prompt',
                        type=str,
                        default=None,
                        help='Prompt to generate an image.')
    parser.add_argument('-f', '--filename',
                        type=str,
                        default='result',
                        help='Name of the image that will be saved.')
    parser.add_argument('--path-to-img',
                        type=str,
                        default=None,
                        help='If an image passed as input, stabe diffusion will modify the image.')
    args = parser.parse_args()

    # Choose model
    if args.path_to_img is None:
        image = txt_to_img(args.prompt)
    elif args.path_to_img is not None:
        image = img_to_img(args.prompt, args.path_to_img)

    # Done
    filename = args.filename + ".png"
    image.save(filename)
    print(f'COMPLETE')


if __name__ == '__main__':
    sys.exit(main())
