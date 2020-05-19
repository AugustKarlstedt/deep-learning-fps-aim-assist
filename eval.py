import copy
import cv2
from detecto import core, utils, visualize
from detecto.utils import reverse_normalize, normalize_transform, _is_iterable
import progressbar
import torch
from torchvision import transforms
import warnings
warnings.filterwarnings("ignore")




model = core.Model.load('model.pth', ['enemy'])

input_file = "AT-cm 670698522.mp4"
output_file = "output.mp4"
fps = 60
score_filter = 0.7



video = cv2.VideoCapture(input_file)

current_frame = 1

# Video frame dimensions
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

bar = progressbar.ProgressBar(current_value=current_frame, max_value=frame_count).start()

# Scale down frames when passing into model for faster speeds
scaled_size = 256
scale_down_factor = min(frame_height, frame_width) / scaled_size

# The VideoWriter with which we'll write our video with the boxes and labels
# Parameters: filename, fourcc, fps, frame_size
out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Transform to apply on individual frames of the video
transform_frame = transforms.Compose([  # TODO Issue #16
    transforms.ToPILImage(),
    transforms.Resize(scaled_size),
    transforms.ToTensor(),
    normalize_transform(),
])

# Loop through every frame of the video
while True:
    ret, frame = video.read()
    # Stop the loop when we're done with the video
    if not ret:
        break

    # The transformed frame is what we'll feed into our model
    transformed_frame = transform_frame(frame)
    predictions = model.predict(transformed_frame)

    # Add the top prediction of each class to the frame
    for label, box, score in zip(*predictions):
        if score < score_filter:
            continue

        # Since the predictions are for scaled down frames,
        # we need to increase the box dimensions
        box *= scale_down_factor

        # Create the box around each object detected
        # Parameters: frame, (start_x, start_y), (end_x, end_y), (r, g, b), thickness
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 0, 255), 3)

        # Write the label and score for the boxes
        # Parameters: frame, text, (start_x, start_y), font, font scale, (r, g, b), thickness
        cv2.putText(frame, '{}: {}'.format(label, round(score.item(), 2)), (int(box[0]), int(box[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Write this frame to our video file
    out.write(frame)
    # cv2.imshow('vid', frame)

    bar.update(current_frame)
    current_frame += 1

bar.finish()

# When finished, release the video capture and writer objects
video.release()
out.release()

# Close all the frames
cv2.destroyAllWindows()
