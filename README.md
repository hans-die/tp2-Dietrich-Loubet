# 🎨 Edna - Image Editor

**Edna** is a simple image editor created for an academic project. It allows users to apply two quantization techniques—**Halftone** and **K-Means**—to modify and stylize images in creative ways. The program is fully interactive and offers users multiple customization options.

---

## 🧬 **Halftone Filter**

The **Halftone** filter creates a retro, print-style effect by turning each color chanel (RGB) into a grid of dots. The dot size varies based on pixel intensity—darker areas produce larger dots. Each channel is rotated slightly to create a layered, stylized look.

## 🧠 **K-Means quantization**

The K-Means filter reduces the number of colors in order to give the image a cartoon-like look. It applies the K-Means clustering algorithm in RGB space, replacing each pixel’s original color with the with the average color of its group.

This results in a simplified version of the image that maintains visual structure while reducing color complexity.


## ✨ Features
- 🧾 **Interactive prompts**: Allows users to customize point size, angles, and number of colors.
- 💾 Saves the processed images with custom names in specific folders.

---

**Original** | **Halftone** | **KMeans**
:--:|:--:|:--:
![original](https://udesa-pc.github.io/tps/tp2/img/soccer.bmp) | ![halftone](https://udesa-pc.github.io/tps/tp2/img/soccer_halftone.png) | ![kmeans](https://udesa-pc.github.io/tps/tp2/img/soccer_kmeans.png)

## 🗂️ File Overview

- `tp_edna_main.py`: Main script that coordinates user interaction and image processing.
- `halftone_func.py`: Contains all the functions related to the Halftone filter logic.
- `user_interaction.py`: This file contains the functions that manages the interaction with the user.
- `kmeans.py`: Contains all the functions related to K-Means Quantization filter.
- `generated_photos/`: Folder where all edited images are saved automatically.

## 🎓 Authors

Made by Hans Dietrich and Francisco Loubet – AI Engineering Students.

