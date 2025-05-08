# Tp Edna - Image Editor

**Edna** is a simple image editor created for an academic project. It allows users to apply two quantization techniques—**Halftone** and **K-Means**—to modify and stylize images in creative ways. The program is fully interactive and provides the user with multiple options.

---

## 🎨 **Halftone Filter**

The **Halftone** filter simulates vintage print techniques by converting each RGB channel into a grid of circular dots. The dot size varies based on pixel intensity—darker areas produce larger dots. Each channel is rotated at a different angle to enhance separation and avoid pattern overlap, recreating a stylized, retro aesthetic.

## 🧠 **K-Means quantization**:

The K-Means filter reduces the number of colors in the image by grouping similar colors into clusters. It applies the K-Means clustering algorithm in RGB space, replacing each pixel’s original color with the nearest cluster centroid.

This results in a simplified version of the image that maintains visual structure while reducing color complexity. It is useful for image compression, stylization, or artistic effects.


## ✨ Features
- 🧾 **Interactive prompts**: Allows users to customize point size, angles, and number of colors.
- 💾 Saves the processed images with custom names in specific folders

---

**Original** | **Halftone** | **KMeans**
:--:|:--:|:--:
![original](https://udesa-pc.github.io/tps/tp2/img/soccer.bmp) | ![halftone](https://udesa-pc.github.io/tps/tp2/img/soccer_halftone.png) | ![kmeans](https://udesa-pc.github.io/tps/tp2/img/soccer_kmeans.png)

## 🗂️ File Overview

- `tp_edna_main.py`: Main script that coordinates user interaction and image processing.
- `halftone_func.py`: Contains all the functions related to the Halftone filter logic.
- `user_interaction.py`: Handles terminal inputs, validations, and user experience flow.
- `kmeans.py`: Contains all the functions related to K-Means Quantization filter.
- `generated_photos/`: Folder where all edited images are saved automatically.

## 🎓 Authors

Made by Hans Dietrich and Francisco Loubet – AI Engineering Students.
