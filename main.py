import os
import cv2
import numpy as np
from teackers.tracker import Tracker
from utils.video_utils import read_video
from team_assigner.team_assigner import TeamAssigner

def save_video(frames, output_path, fps=30):
    if not frames:
        raise ValueError("No frames to save.")

    height, width = frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))
        out.write(frame)
    out.release()

def main():
    # Read input video frames
    video_frames = read_video('input_videos/15sec_input_720p.mp4')

    # Initialize tracker with model path
    tracker = Tracker('models/best.pt')

    os.makedirs('stubs', exist_ok=True)

    tracks = tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,
        stub_path='stubs/track_stubs.pkl'
    )

    tracker.add_position_to_tracks(tracks)

    team_ball_control = np.random.choice([1, 2], size=len(video_frames))

    annotated_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    # Draw colored circles around players based on team color
    for frame_num, frame in enumerate(annotated_frames):
        player_track = tracks['players'][frame_num]
        for player_id, track in player_track.items():
            center_pos = track.get('center', None)
            team_color_rgb = track.get('team_color', (255, 0, 0))  # default red RGB if missing

            if center_pos is not None:
                # Convert RGB to BGR for OpenCV
                team_color_bgr = (team_color_rgb[2], team_color_rgb[1], team_color_rgb[0])

                # Draw a circle at center position
                cv2.circle(frame, (int(center_pos[0]), int(center_pos[1])), radius=15, color=team_color_bgr, thickness=3)

    save_video(annotated_frames, 'output_videos/annotated_output.mp4')

if __name__ == "__main__":
    main()
