
# 📐 Stereo Vision Triangulation using Two Cameras (Python + OpenCV)

This project demonstrates **distance estimation using stereo vision triangulation** with two normal USB cameras.
A **green object** is detected in both camera frames, and its **distance from the cameras** is calculated using disparity-based triangulation.

---

## 🔍 Concept Overview

Two cameras observe the same object from slightly different positions.
Because of this, the object appears at different horizontal pixel locations in each image.

The depth is calculated using the stereo vision formula:

[
\text{Depth} = \frac{f \times B}{d}
]

Where:

* **f** = focal length (in pixels)
* **B** = baseline (distance between cameras)
* **d** = disparity (pixel difference between left & right images)

---

## 🧰 Hardware Requirements

* Laptop / PC
* **Two USB cameras**
* Cameras mounted:

  * Horizontally aligned
  * Same height
  * Parallel to each other
* A **green-colored object**
* Measured **baseline distance** between the camera lenses (in cm)

---

## 💻 Software Requirements

### Operating System

* Windows / Linux / macOS

### Python Version

* Python **3.8 or above**

Check Python version:

```bash
python --version
```

---

## 📦 Python Dependencies

Install the required libraries using pip:

```bash
pip install opencv-python numpy
```

### Libraries Used

| Library         | Purpose                         |
| --------------- | ------------------------------- |
| `opencv-python` | Camera access, image processing |
| `numpy`         | Mathematical operations         |

---

## 📁 Project Structure

```text
stereo_triangulation/
│
├── stereo_distance.py   # Main Python script
├── README.md            # Project documentation
```

---

## ▶️ How to Run

1. Connect **two cameras** to your system
2. Note their camera IDs (usually `0` and `1`)
3. Update baseline and focal length in code if needed
4. Run the script:

```bash
python stereo_distance.py
```

Press **`q`** to exit.

---

## ⚙️ Important Parameters (Edit in Code)

```python
BASELINE_CM = 6.0        # Distance between cameras (cm)
FOCAL_LENGTH_PX = 700    # Approximate focal length
```

* Measure **baseline accurately**
* Focal length is approximate for webcams
* For high accuracy, camera calibration is recommended

---

## ⚠️ Limitations

* Accuracy decreases at long distances
* Sensitive to lighting conditions
* Requires visible texture or clear object edges
* Cameras must be well aligned
* Frame synchronization is not hardware-locked

---

## 🚀 Possible Improvements

* Stereo camera calibration using chessboard
* Stereo rectification
* Sub-pixel disparity estimation
* Depth filtering
* ROS / ROS2 integration
* Replace webcams with depth cameras (e.g., Intel RealSense)

---

## 📚 Learning Outcome

This project helps in understanding:

* Stereo vision fundamentals
* Disparity and triangulation
* Practical depth estimation
* Computer vision geometry

---

## 📜 License

This project is open-source and free to use for educational and research purposes.

 

 

Just tell me 👍
