# Virtual Photobooth with a Twist — Neural Style Transfer Meets Fun!

A modern take on the virtual photobooth — with artistic flair! This app allows users to capture or upload photos and apply stunning artistic styles using **Neural Style Transfer** techniques.


---

## Features

- Take or upload photos directly from your browser
- Apply artistic styles using **Fast Neural Style Transfer**
- Built-in sample style (more styles coming soon!)
- Style inspiration via Pinterest mood boards
- Clean, responsive UI built with Vue.js

---

## Style Transfer Methods Explained

| Method                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Neural Style Transfer (NST) | Uses a training loop to directly optimize an output image to match style and content. Highly flexible. |
| Fast Neural Style Transfer     | Fast and efficient — but each style requires a separate pre-trained model. Ideal for real-time applications. |

The current app uses **Fast Neural Style Transfer**, trained in PyTorch on Google Colab.

---

## 🛠️ Tech Stack

| Layer        | Technology      |
|--------------|-----------------|
| Frontend     | `Vue.js`        |
| Backend API  | `Flask` (Python)|
| Model Training | `PyTorch` on Google Colab |
| Style Model  | Pre-trained Fast Style Transfer Model |

---

## Note 
I'm currently in the process of deploying it

---

