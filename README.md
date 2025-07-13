
# Football Player Tracking and Team Classification

This project uses computer vision techniques to detect, track, and classify football players into their respective teams based on jersey colors from video footage.

---

## Features

- **Video Frame Processing**: Reads input video and processes frames.
- **Player Detection**: Detects football players in each frame.
- **Tracking**: Tracks players across frames using unique IDs.
- **Color-Based Team Assignment**: Clusters jersey colors using K-Means to assign players to teams.
- **Visual Overlay**: Draws bounding boxes and team labels on each player.

---

## 📁 Project Structure

```
football-tracker/
├── main.py                      # Main script to run the pipeline
├── team_assigner/
│   └── team_assigner.py         # Module for team color clustering and assignment
├── utils/
│   └── tracking_utils.py        # Utility functions for tracking (optional)
├── data/
│   └── input.mp4                # Input football match video
├── output/
│   └── annotated_output.mp4     # Processed video with bounding boxes and team overlays
├── requirements.txt             # Dependencies
└── README.md                    # Project overview
```

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Darshan8128/Soccer-player-Re-identification-in-sports-footage
cd football-tracker
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Add Your Input Video

Place your input football video (e.g. `15sec_input_720p.mp4`) into the `data/` directory.

### 4. Run the Pipeline

```bash
python main.py
```

---

## ⚙️ Configuration Options

You can modify parameters like:

- KMeans `n_clusters`
- Frame skipping rate
- Bounding box handling
- Output video resolution and codec

All changes should be made in `main.py` and `team_assigner.py`.

---

## How It Works

1. **Player Color Extraction**  
   Top half of each player's bounding box is used to sample jersey color (ignores grass/legs).

2. **K-Means Clustering**  
   Colors are clustered into 2 groups (2 teams) automatically.

3. **Prediction**  
   Each player's color is compared against the learned clusters to determine their team.

4. **Overlay**  
   Bounding boxes and team labels are drawn using OpenCV.

---

##  Dependencies

- `numpy`
- `opencv-python`
- `scikit-learn`

Install via:

```bash
pip install numpy opencv-python scikit-learn
```

---

##  Example Output

- Red and Blue boxes on players based on their team
- Video saved in `output/output_video.mp4`


---

##  Acknowledgements

- OpenCV for image processing
- scikit-learn for clustering
- YOLOv5/YOLOv8 (if used for detection)
