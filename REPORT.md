# Football Player Team Detection and Visualization

## Overview

This project implements a system to detect football players in a video, identify their team affiliations using jersey color clustering, and visualize the results by overlaying bounding boxes and team labels on each player.

---

## Objectives

- Detect players in football video footage.
- Extract average jersey colors from players using bounding boxes.
- Cluster players based on dominant color using KMeans.
- Assign each player to a team (Team 1 or Team 2).
- Overlay team info on the video for visualization.

---

## Workflow

### 1. Preprocessing

- Input: Annotated video with player bounding boxes.
- Each bounding box is passed to a color extractor to determine average jersey color (top-half of body).
- Skip frames or players with invalid bounding boxes or empty crops.

### 2. Color Clustering

- Use KMeans clustering (`n_clusters=2`) on the extracted jersey colors.
- Classify players into two teams based on proximity to cluster centers.
- Assign team IDs accordingly.

### 3. Team Assignment

- Player ID → team ID mapping is saved.
- The same mapping is reused across frames for consistency.

### 4. Visualization

- Draw bounding boxes with different colors for each team.
- Overlay team labels above each player's bounding box.

---
### 5. Challenges
Color Similarity: If teams have similar jersey colors (e.g., shades of blue vs purple), KMeans might fail to clearly separate them.

Lighting Variations: Different lighting conditions across the field (shadows, glare) affect color extraction accuracy.

Occlusion: Players may block one another, leading to poor bounding boxes and misleading color crops.

Resolution Constraints: Low-resolution videos reduce color detail, impacting clustering performance.

Non-Uniform Jerseys: Logos, stripes, or numbers on jerseys may skew color averaging.

Corner Detection Bias: The assumption that corners of the bounding box are background might fail if the player's head or shoulders are near corners.

Frame Rate vs Performance: Processing every frame can be computationally expensive. Skipping too many frames may miss important player movements. 

## Project Structure

```plaintext
.
├── main.py
├── team_assigner/
│   └── team_assigner.py
├── annotated_output.mp4
├── README.md
└── Football_Team_Detection_Report.md
