
Aerial Beach Waste Dataset - v1 2023-09-02 11:39pm
==============================

This dataset was exported via roboflow.com on September 2, 2023 at 4:06 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2877 images.
Recyclable-trash-on-the-beach are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Random exposure adjustment of between -25 and +25 percent

The following transformations were applied to the bounding boxes of each image:
* Salt and pepper noise was applied to 5 percent of pixels


