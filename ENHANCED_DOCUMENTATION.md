# Enhanced Stadium Crowd Monitoring System with Camera Control

This document provides comprehensive documentation for the enhanced stadium crowd monitoring system with camera control, zoom, and crop functionality.

## Overview

The Enhanced Stadium Crowd Monitoring System extends the original system with advanced camera control capabilities that allow:

1. **Camera Movement**: Automatically move a camera across the stadium seating areas
2. **Zoom Functionality**: Zoom in on detected cases of interest (fighting, throwing objects, misplaced fans)
3. **Crop Functionality**: Extract and save images of specific people for security alerts
4. **Sequence Generation**: Create zoom sequences and animations for better visualization

This enhanced system is designed to help security personnel monitor large crowds in stadiums, detect problematic behaviors, and quickly respond to incidents.

## System Architecture

The enhanced system consists of the following main components:

1. **Stadium Monitoring System**: The core detection system that identifies fans, their team affiliations, and behaviors
2. **Camera Controller**: Handles camera movement, positioning, and basic zooming
3. **Zoom Processor**: Specialized component for creating crops, zoom sequences, and visual effects
4. **Enhanced System Integration**: Combines all components into a unified system

### Component Diagram

```
┌─────────────────────────────────────────────────────────┐
│                Enhanced Stadium Monitoring System        │
│                                                         │
│  ┌───────────────────┐    ┌────────────────────────┐    │
│  │ Stadium Monitoring│    │    Camera Controller   │    │
│  │      System       │    │                        │    │
│  │                   │    │  - Movement control    │    │
│  │ - Fan detection   │    │  - Position tracking   │    │
│  │ - Team detection  │    │  - Basic zooming       │    │
│  │ - Behavior        │    │  - Area scanning       │    │
│  │   classification  │    │                        │    │
│  │ - Alert generation│    └────────────────────────┘    │
│  └───────────────────┘                                  │
│                                                         │
│  ┌───────────────────┐    ┌────────────────────────┐    │
│  │  Zoom Processor   │    │    Integration Layer   │    │
│  │                   │    │                        │    │
│  │ - Crop generation │    │ - Unified API          │    │
│  │ - Zoom sequences  │    │ - Process coordination │    │
│  │ - GIF creation    │    │ - Result aggregation   │    │
│  │ - Visual effects  │    │                        │    │
│  └───────────────────┘    └────────────────────────┘    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Key Features

### 1. Camera Movement

The system can move a virtual camera across the stadium seating areas using different scanning patterns:

- **Horizontal Scan**: Move from left to right, row by row
- **Vertical Scan**: Move from top to bottom, column by column
- **Grid Scan**: Move in a grid pattern, covering larger areas with each step

The camera movement is controlled by the `CameraController` class, which maintains the current position and zoom level.

### 2. Zoom Functionality

When a detection of interest is found (fighting, throwing objects, misplaced fans), the system can:

- **Zoom In**: Focus on the specific area with adjustable zoom levels
- **Create Zoom Sequence**: Generate a sequence of frames with progressively increasing zoom
- **Create Animations**: Create smooth zoom animations as GIFs or MP4 videos

The zoom functionality is provided by both the `CameraController` and `ZoomProcessor` classes.

### 3. Crop Functionality

For each detection, the system can:

- **Crop Detection**: Extract the region containing the detected person
- **Save Crops**: Save cropped images with detection information
- **Create Detection Grid**: Arrange multiple crops in a grid for easy viewing

The crop functionality is primarily handled by the `ZoomProcessor` class.

### 4. Visual Effects

The system includes several visual effects to enhance the presentation of detections:

- **Highlight Detection**: Draw bounding boxes with color coding based on behavior
- **Zoom Box Effect**: Show a zoomed view of the detection alongside the original image
- **Sequence Animation**: Create animated GIFs showing progressive zoom on detections

## Usage

### Basic Usage

```python
from src.enhanced_system import EnhancedStadiumMonitoringSystem

# Initialize the system
system = EnhancedStadiumMonitoringSystem()
system.initialize()

# Process an image
detections, alerts, results = system.process_image(
    'stadium_image.jpg',
    output_path='output.jpg',
    generate_alerts=True,
    zoom_on_detections=True
)

# Access the results
print(f"Detected {len(detections)} fans")
print(f"Generated {len(alerts)} alerts")
print(f"Created {len(results['crops'])} crops")
```

### Command Line Interface

The system can be used from the command line using the `enhanced_main.py` script:

```bash
python enhanced_main.py --mode image --input stadium_image.jpg --output output.jpg
```

Available modes:
- `image`: Process a single image
- `video`: Process a video file
- `live`: Process a live camera feed
- `scan`: Scan an image using the specified pattern

Additional options:
- `--zoom-level`: Set the zoom level (default: 2.5)
- `--scan-pattern`: Set the scan pattern (horizontal, vertical, grid)
- `--scan-speed`: Set the scan speed in pixels (default: 15)
- `--no-alerts`: Disable alert generation
- `--no-zoom`: Disable zooming on detections

### Demo Script

A demonstration script is provided in `demo.py` that shows how to use the enhanced system with a sample image:

```bash
python demo.py --output-dir demo_outputs --create-sample
```

This will create a sample stadium image with fans and process it using both the regular processing mode and the scan mode.

## Camera Controller

The `CameraController` class provides the following functionality:

### Movement Control

- `move_camera(direction, distance)`: Move the camera in the specified direction
- `set_position(position)`: Set the camera position directly
- `zoom(level)`: Set the zoom level

### Area Scanning

- `scan_area(frame, width, height, pattern)`: Scan the area according to the specified pattern
- `get_current_view(frame)`: Get the current view based on position and zoom level

### Detection Handling

- `zoom_to_detection(frame, bbox, padding, zoom_level)`: Zoom to a detected object
- `save_detection_crop(frame, bbox, detection_info)`: Save a cropped image of a detection
- `create_detection_sequence(frame, bbox, num_frames, zoom_start, zoom_end)`: Create a sequence of frames zooming in on a detection
- `save_detection_sequence(frame, bbox, detection_info)`: Save a sequence of frames zooming in on a detection
- `create_gif_from_sequence(sequence, output_path, duration)`: Create a GIF from a sequence of frames

## Zoom Processor

The `ZoomProcessor` class provides specialized functionality for zoom and crop operations:

### Crop Operations

- `crop_detection(image, bbox, padding)`: Crop a detection from an image
- `save_crop(image, bbox, detection_info, padding)`: Save a cropped detection

### Zoom Sequences

- `create_zoom_sequence(image, bbox, num_frames, zoom_start, zoom_end, padding)`: Create a sequence of frames zooming in on a detection
- `save_zoom_sequence(image, bbox, detection_info, num_frames, zoom_start, zoom_end, padding)`: Save a sequence of frames zooming in on a detection

### Visual Effects

- `create_gif(sequence, output_path, duration)`: Create a GIF from a sequence of frames
- `create_mp4(sequence, output_path, fps)`: Create an MP4 video from a sequence of frames
- `highlight_detection(image, bbox, color, thickness, zoom_box, zoom_factor)`: Highlight a detection in an image
- `create_detection_grid(crops, grid_size, cell_size, background_color)`: Create a grid of detection crops
- `save_detection_grid(crops, output_path, grid_size, cell_size)`: Save a grid of detection crops
- `create_zoom_animation(image, bbox, output_path, num_frames, zoom_end, fps)`: Create a smooth zoom animation focusing on a detection

## Enhanced System Integration

The `EnhancedStadiumMonitoringSystem` class integrates all components and provides the following functionality:

### Image Processing

- `process_image(image_path, output_path, generate_alerts, zoom_on_detections)`: Process a single image with camera control and zoom
- `process_video(video_path, output_path, generate_alerts, zoom_on_detections, frame_interval)`: Process a video with camera control and zoom
- `process_live_feed(camera_id, output_path, generate_alerts, zoom_on_detections, duration)`: Process a live camera feed with camera control and zoom
- `scan_and_monitor(image_path, output_path, generate_alerts)`: Scan an image and monitor for problematic behaviors with camera movement

### Reporting

- `generate_report(output_path)`: Generate a summary report of the monitoring system
- `visualize_alerts(output_path)`: Visualize the distribution of alerts

## Output Structure

The system generates various outputs organized in the following directory structure:

```
├── camera_outputs/           # Camera controller outputs
│   ├── temp_frame.jpg        # Temporary frame for processing
│   └── ...
├── zoom_outputs/             # Zoom processor outputs
│   ├── crops/                # Cropped detections
│   ├── sequences/            # Zoom sequences
│   ├── gifs/                 # GIFs and animations
│   ├── scans/                # Scan crops
│   └── ...
├── alerts/                   # Alert system outputs
│   ├── report.txt            # Alert report
│   ├── alert_distribution.png # Alert visualization
│   └── ...
└── output.jpg                # Main output image with detections
```

## Configuration

The system can be configured using a configuration dictionary with the following options:

```python
config = {
    'model_dir': 'models',                # Directory for model files
    'input_shape': (384, 512, 3),         # Input shape for models
    'detection_threshold': 0.5,           # Detection confidence threshold
    'alerts_dir': 'alerts',               # Directory for alerts
    'camera_outputs_dir': 'camera_outputs', # Directory for camera outputs
    'zoom_outputs_dir': 'zoom_outputs',   # Directory for zoom outputs
    'zoom_level': 2.5,                    # Default zoom level
    'scan_speed': 15,                     # Scan speed in pixels
    'scan_pattern': 'grid',               # Scan pattern (horizontal, vertical, grid)
    'stadium_sections': {                 # Stadium section definitions
        'hilal': [0, 0, 256, 384],        # Left half of stadium (x1, y1, x2, y2)
        'ittihad': [256, 0, 512, 384]     # Right half of stadium
    }
}
```

## Testing

The system includes comprehensive tests in the `test` directory:

- `test_enhanced_system.py`: Tests for the enhanced system integration
- `test_components.py`: Tests for individual components

To run the tests:

```bash
python -m unittest test.test_enhanced_system
python -m unittest test.test_components
```

## Use Cases

### 1. Detecting Fighting Fans

1. The system scans the stadium seating areas
2. When fans engaged in fighting are detected:
   - The system zooms in on the fighting fans
   - Crops the image to focus on the incident
   - Creates a zoom sequence for better visualization
   - Generates an alert with the location and image

### 2. Identifying Misplaced Fans

1. The system detects fans and their team affiliations
2. When a fan supporting one team is found in another team's section:
   - The system zooms in on the misplaced fan
   - Crops the image to focus on the fan
   - Generates an alert with the location and image

### 3. Monitoring Throwing Objects

1. The system scans the stadium seating areas
2. When fans throwing objects are detected:
   - The system zooms in on the incident
   - Crops the image to focus on the fan
   - Creates a zoom sequence for better visualization
   - Generates an alert with the location and image

## Limitations and Future Improvements

### Current Limitations

- The system works best with the synthetic dataset provided (Hilal/Ittihad teams)
- Real-time processing may be limited by hardware capabilities
- The system requires clear visibility of fans from a drone-view perspective

### Future Improvements

- Implement tracking to follow fans across frames
- Add support for multiple cameras and views
- Enhance the alert system with real-time notifications
- Improve detection accuracy with more training data
- Add support for additional team affiliations and behaviors

## Conclusion

The Enhanced Stadium Crowd Monitoring System with Camera Control provides a powerful tool for stadium security personnel to monitor large crowds, detect problematic behaviors, and quickly respond to incidents. The system's ability to automatically move a camera across the stadium, zoom in on detections of interest, and crop images of specific people makes it an effective solution for stadium security.
