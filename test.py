import opennsfw2 as n2

# The video can be in any format supported by OpenCV.
video_path = "/samples/test_nsfw.mp4"

# Return two lists giving the elapsed time in seconds and the NSFW probability of each frame.
elapsed_seconds, nsfw_probabilities = n2.predict_video_frames(video_path)

print("--> Elapsed seconds \n")
print("--> # es", len(elapsed_seconds))
print(elapsed_seconds)

print("--> Probabilities: \n")
print("--> # probabilities:", len(nsfw_probabilities))
print(nsfw_probabilities)
