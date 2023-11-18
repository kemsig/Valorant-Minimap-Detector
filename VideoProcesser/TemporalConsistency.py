import sys
class TemporalConsistency:
    def __init__(self, history_len, threshold):
        self.detected_frames_history = []
        self.history_len = history_len
        self.threshold = threshold

    def update_history(self, frame_detected_truth):
        self.detected_frames_history.append(frame_detected_truth)

