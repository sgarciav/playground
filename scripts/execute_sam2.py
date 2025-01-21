#!/usr/bin/env python3

# See: https://github.com/facebookresearch/sam2

import torch
from sam2.build_sam import build_sam2
from sam2.automatic_mask_generator import SAM2AutomaticMaskGenerator

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import cv2
import argparse

sam2_checkpoint = "/home/sergio/git-repos/3rd-party/sam2/checkpoints/sam2.1_hiera_large.pt"
model_cfg = "configs/sam2.1/sam2.1_hiera_l.yaml"


def show_one_mask(anns, mask_num, borders=True):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:, :, 3] = 0

    m = sorted_anns[mask_num]['segmentation']
    color_mask = np.concatenate([np.random.random(3), [0.5]])
    img[m] = color_mask
    if borders:
        contours, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Try to smooth contours
        contours = [cv2.approxPolyDP(contour, epsilon=0.01, closed=True) for contour in contours]
        cv2.drawContours(img, contours, -1, (0, 0, 1, 0.4), thickness=1)

    ax.imshow(img)


def show_anns(anns, borders=True):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:, :, 3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.5]])
        img[m] = color_mask
        if borders:
            contours, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            # Try to smooth contours
            contours = [cv2.approxPolyDP(contour, epsilon=0.01, closed=True) for contour in contours]
            cv2.drawContours(img, contours, -1, (0, 0, 1, 0.4), thickness=1)

    ax.imshow(img)


def main():
    parser = argparse.ArgumentParser(description = 'Run SAM model for semantic segmentation.')
    parser.add_argument('-f', '--filename',
                        type=str,
                        default=None,
                        help='Absolute or relative path to the input image.')
    parser.add_argument('-s', '--show-original-image',
                        action='store_true',
                        default=False,
                        help='Display original image before processing.')

    args = parser.parse_args()

    # 1. Read the image
    image = Image.open(args.filename)
    image = np.array(image.convert("RGB"))

    if args.show_original_image:
        plt.figure(figsize=(20, 20))
        plt.imshow(image)
        plt.axis('off')

    # 2. Select device
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    print(f"-- Using device: {device}")

    if device.type == "cuda":
        # use bfloat16 for the entire notebook
        torch.autocast("cuda", dtype=torch.bfloat16).__enter__()
        # turn on tfloat32 for Ampere GPUs (https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices)
        if torch.cuda.get_device_properties(0).major >= 8:
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True

    # 3. Automatic Mask Generator
    print(f"-- Running the mask generator")
    sam2 = build_sam2(model_cfg, sam2_checkpoint, device=device, apply_postprocessing=False)
    # mask_generator = SAM2AutomaticMaskGenerator(sam2)
    mask_generator = SAM2AutomaticMaskGenerator(
        model=sam2,
        points_per_side=32,
        points_per_batch=64,
        pred_iou_thresh=0.7,
        stability_score_thresh=0.92,
        stability_score_offset=0.7,
        crop_n_layers=1,
        box_nms_thresh=0.7,
        crop_n_points_downscale_factor=2,
        min_mask_region_area=10.0,
        use_m2m=False,
    )
    masks = mask_generator.generate(image)
    print(f"-- Number of masks: {len(masks)}")

    # 4. Display masks over image
    plt.figure(figsize=(20, 20))
    plt.imshow(image)
    show_anns(masks)
    plt.axis('off')

    # 5. Mask with largest area
    mask_num = 1
    sorted_masks = sorted(masks, key=(lambda x: x['area']), reverse=True)
    bbox_floats = sorted_masks[mask_num]['bbox']
    bbox = [int(x) for x in bbox_floats]
    print('-- Bounding box (XYWH): {}'.format(bbox))
    ul = [bbox[0], bbox[1]]
    br = [bbox[2] + bbox[0], bbox[3] + bbox[1]]
    bbox_img = cv2.rectangle(image, ul, br,
                             color=(0, 255, 0), thickness=3)

    plt.figure(figsize=(20, 20))
    plt.imshow(bbox_img)
    show_one_mask(masks, mask_num) # TODO: Need better way to select mask of interest
    plt.axis('off')

    # End. Show all plots
    print(f"-- Close each image window to exit program.")
    plt.show()

if __name__ == '__main__':
    sys.exit(main())
