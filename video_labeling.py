import cv2

def downsize_video(input_video_path, output_video_path, scale_percent=50):
    # Open the original video
    cap = cv2.VideoCapture(input_video_path)

    # Get original dimensions and frame rate
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate new dimensions
    width = int(original_width * scale_percent / 100)
    height = int(original_height * scale_percent / 100)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

        # Write the resized frame to the new video
        out.write(resized_frame)

    # Release everything when done
    cap.release()
    out.release()






if __name__ == '__main__':
    # Example usage
    input_path = 'path_to_your_large_video.mp4'
    output_path = 'path_to_your_downsized_video.mp4'
    downsize_video(input_path, output_path)
