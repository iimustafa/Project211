# Stadium Crowd Behavior Detection System

## Overview

This system uses AI technology to detect and monitor crowd behavior in stadiums using drone-view cameras. It can identify fans, classify their behavior (sitting, cheering, fighting, throwing), detect team affiliations (Hilal/Ittihad), and generate alerts for security personnel when problematic behaviors or misplaced fans are detected.

## Features

- **Fan Detection**: Identifies and locates fans in stadium images
- **Behavior Classification**: Classifies fan behavior into four categories:
  - Sitting (normal)
  - Cheering (normal)
  - Fighting (problematic)
  - Throwing (problematic)
- **Team Affiliation Detection**: Identifies which team a fan supports (Hilal/Ittihad)
- **Misplaced Fan Detection**: Identifies fans supporting one team sitting in another team's section
- **Alert System**: Generates alerts with location information and images for security personnel
- **Multiple Input Support**: Works with images, videos, and live camera feeds

## System Architecture

The system consists of the following components:

1. **Data Utilities** (`src/data_utils.py`): Handles loading and preprocessing the synthetic dataset
2. **Detection Model** (`src/model.py`): Implements the fan detection and classification model
3. **Behavior Classifier** (`src/behavior_classifier.py`): Specialized classifier for fan behaviors
4. **Team Detector** (`src/team_detector.py`): Specialized detector for team affiliations
5. **Alert System** (`src/alert_system.py`): Generates and manages security alerts
6. **Inference Module** (`src/inference.py`): Handles inference on new images
7. **Integrated System** (`src/system.py`): Integrates all components into a complete system
8. **Main Application** (`main.py`): Command-line interface for using the system

## Installation

### Prerequisites

- Python 3.10 or higher
- TensorFlow 2.x
- OpenCV
- NumPy, Matplotlib, PIL, tqdm

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/stadium-crowd-detection.git
   cd stadium-crowd-detection
   ```

2. Install dependencies:
   ```
   pip install tensorflow opencv-python pillow matplotlib numpy tqdm
   ```

3. Prepare the dataset:
   - Place the synthetic dataset in the `stadium_dataset` directory
   - Ensure the dataset follows the structure:
     ```
     stadium_dataset/
     ├── images/
     │   ├── 0001.png
     │   ├── 0002.png
     │   └── ...
     └── annotations/
         └── labels.json
     ```

## Usage

### Training the Models

To train the models on the synthetic dataset:

```
python train.py
```

This will train the fan detection model, behavior classifier, and team detector, and save them to the `models` directory.

### Running the System

The system can be run in three modes:

1. **Image Mode**: Process a single image
   ```
   python main.py --mode image --input path/to/image.png --output path/to/output.png
   ```

2. **Video Mode**: Process a video file
   ```
   python main.py --mode video --input path/to/video.mp4 --output path/to/output.mp4
   ```

3. **Live Mode**: Process a live camera feed
   ```
   python main.py --mode live --camera 0 --output path/to/output.mp4
   ```

### Command-Line Arguments

- `--mode`: Processing mode (`image`, `video`, or `live`)
- `--input`: Path to input image or video file
- `--output`: Path to save output results
- `--detector`: Path to trained detector model (default: `models/fan_detection_model.h5`)
- `--behavior`: Path to trained behavior classifier model (default: `models/behavior_classifier.h5`)
- `--team`: Path to trained team detector model (default: `models/team_detector.h5`)
- `--camera`: Camera ID for live feed mode (default: 0)
- `--duration`: Duration in seconds for live feed processing (default: None, runs indefinitely)
- `--no-alerts`: Disable alert generation

### Testing the System

To test the system on synthetic data samples:

```
python -m test.test_system
```

To run unit tests for individual components:

```
python -m test.test_components
```

## Alert System

The system generates alerts for two types of situations:

1. **Problematic Behaviors**: When fans are detected fighting or throwing objects
2. **Misplaced Fans**: When fans supporting one team are detected in another team's section

Alerts include:
- Alert type
- Location information
- Confidence score
- Image with highlighted detection
- Additional details

Alerts are saved to the `alerts` directory, with images in the `alerts/images` subdirectory and a log file at `alerts/alerts_log.json`.

## Extending the System

### Adding New Behaviors

To add new behavior classes:

1. Update the `action_mapping` in `src/data_utils.py`
2. Modify the behavior classifier in `src/behavior_classifier.py`
3. Update the alert system in `src/alert_system.py` to handle the new behavior

### Supporting New Teams

To add support for additional teams:

1. Update the `team_mapping` in `src/data_utils.py`
2. Modify the team detector in `src/team_detector.py`
3. Update the stadium sections in `src/system.py`

## Limitations and Future Work

- The current system is trained on synthetic data and may require adaptation for real-world deployment
- Performance may vary depending on lighting conditions, camera angle, and crowd density
- Future work could include:
  - Integration with multiple camera feeds
  - Real-time tracking of individuals across frames
  - More sophisticated behavior analysis
  - Mobile app for security personnel

## Troubleshooting

### Common Issues

- **Model Loading Errors**: Ensure the model paths are correct and the models exist
- **Camera Access Issues**: Check camera permissions and ID
- **Memory Errors**: Reduce batch size or image resolution for large videos

### Getting Help

For additional help or to report issues, please contact the development team.
