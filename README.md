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
- `k-means_func.py`: Contains all the functions related to K-Means Quantization filter.
- `generated_photos/`: Folder where all edited images are saved automatically.
- `Photos`: Folder where users can upload images they want to edit with the tool.

## 🧪 How to Use

1. Clone the repository and enter the project folder.
2. Make sure you have Python 3 installed. Then install the dependencies: `pip install pillow numpy`
3. Add the image you want to edit inside the `Photos/` folder or use one of the default ones (copy path).
4. Run the main code:  `python tp_edna_main.py`
5. Follow the on-screen instructions to choose a filter (`halftone` or `kmeans`) and decide your personal parameters.
6. The resulting image will be saved automatically in the `generated_photos/` folder and displayed next to the original.

---
## 🎓 Authors

Made by Hans Dietrich and Francisco Loubet – AI Engineering Students.

