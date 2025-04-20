"""
Main application script for the stadium crowd monitoring system with camera control.
This script demonstrates the usage of the integrated system with camera movement and zoom.
"""

import os
import argparse
import tensorflow as tf
from src.camera_monitoring import CameraMonitoringSystem

def main():
    """Main function to run the stadium crowd monitoring system with camera control."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Stadium Crowd Monitoring System with Camera Control')
    parser.add_argument('--mode', type=str, default='image', choices=['image', 'video', 'live', 'scan'],
                        help='Processing mode: image, video, live camera feed, or scan')
    parser.add_argument('--input', type=str, default=None,
                        help='Path to input image or video file')
    parser.add_argument('--output', type=str, default=None,
                        help='Path to save output results')
    parser.add_argument('--detector', type=str, default='models/fan_detection_model.h5',
                        help='Path to trained detector model')
    parser.add_argument('--behavior', type=str, default='models/behavior_classifier.h5',
                        help='Path to trained behavior classifier model')
    parser.add_argument('--team', type=str, default='models/team_detector.h5',
                        help='Path to trained team detector model')
    parser.add_argument('--camera', type=int, default=0,
                        help='Camera ID for live feed mode')
    parser.add_argument('--duration', type=int, default=None,
                        help='Duration in seconds for live feed processing')
    parser.add_argument('--no-alerts', action='store_true',
                        help='Disable alert generation')
    parser.add_argument('--no-zoom', action='store_true',
                        help='Disable zooming on detections')
    parser.add_argument('--zoom-level', type=float, default=2.5,
                        help='Zoom level for detections (default: 2.5)')
    parser.add_argument('--scan-pattern', type=str, default='grid', choices=['horizontal', 'vertical', 'grid'],
                        help='Scan pattern for scanning mode')
    parser.add_argument('--scan-speed', type=int, default=15,
                        help='Scan speed in pixels (default: 15)')
    
    args = parser.parse_args()
    
    # Create output directories if needed
    if args.output and not os.path.exists(os.path.dirname(args.output)):
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    # Create camera outputs directory
    camera_outputs_dir = 'camera_outputs'
    os.makedirs(camera_outputs_dir, exist_ok=True)
    
    # Initialize the system with camera control
    print("Initializing stadium crowd monitoring system with camera control...")
    system = CameraMonitoringSystem(config={
        'model_dir': 'models',
        'alerts_dir': 'alerts',
        'camera_outputs_dir': camera_outputs_dir,
        'zoom_level': args.zoom_level,
        'scan_speed': args.scan_speed,
        'scan_pattern': args.scan_pattern,
        'stadium_sections': {
            'hilal': [0, 0, 256, 384],  # Left half of stadium
            'ittihad': [256, 0, 512, 384]  # Right half of stadium
        }
    })
    
    system.initialize(
        detector_path=args.detector if os.path.exists(args.detector) else None,
        behavior_classifier_path=args.behavior if os.path.exists(args.behavior) else None,
        team_detector_path=args.team if os.path.exists(args.team) else None
    )
    
    # Process based on mode
    if args.mode == 'image':
        if not args.input:
            raise ValueError("Input image path must be provided for image mode")
            
        print(f"Processing image: {args.input}")
        detections, alerts, crops = system.process_image(
            args.input,
            output_path=args.output,
            generate_alerts=not args.no_alerts,
            zoom_on_detections=not args.no_zoom
        )
        
        print(f"Detected {len(detections)} fans")
        if not args.no_alerts:
            print(f"Generated {len(alerts)} alerts")
        print(f"Created {len(crops)} cropped detection images")
        
        if args.output:
            print(f"Output saved to: {args.output}")
        print(f"Detection crops saved to: {camera_outputs_dir}")
            
    elif args.mode == 'video':
        if not args.input:
            raise ValueError("Input video path must be provided for video mode")
            
        print(f"Processing video: {args.input}")
        all_detections, all_alerts, all_crops = system.process_video(
            args.input,
            output_path=args.output,
            generate_alerts=not args.no_alerts,
            zoom_on_detections=not args.no_zoom
        )
        
        total_detections = sum(len(dets) for dets in all_detections)
        print(f"Detected {total_detections} fans across all processed frames")
        
        if not args.no_alerts:
            print(f"Generated {len(all_alerts)} alerts")
        print(f"Created {len(all_crops)} cropped detection images")
        
        if args.output:
            print(f"Output saved to: {args.output}")
        print(f"Detection crops saved to: {camera_outputs_dir}")
            
    elif args.mode == 'live':
        print(f"Processing live feed from camera {args.camera}")
        all_alerts, all_crops = system.process_live_feed(
            camera_id=args.camera,
            output_path=args.output,
            generate_alerts=not args.no_alerts,
            zoom_on_detections=not args.no_zoom,
            duration=args.duration
        )
        
        if not args.no_alerts:
            print(f"Generated {len(all_alerts)} alerts")
        print(f"Created {len(all_crops)} cropped detection images")
        
        if args.output:
            print(f"Output saved to: {args.output}")
        print(f"Detection crops saved to: {camera_outputs_dir}")
            
    elif args.mode == 'scan':
        if not args.input:
            raise ValueError("Input image path must be provided for scan mode")
            
        print(f"Scanning image: {args.input}")
        print(f"Using scan pattern: {args.scan_pattern}, scan speed: {args.scan_speed}")
        
        detections, alerts, crops = system.scan_and_monitor(
            args.input,
            output_path=args.output,
            generate_alerts=not args.no_alerts
        )
        
        print(f"Detected {len(detections)} fans")
        if not args.no_alerts:
            print(f"Generated {len(alerts)} alerts")
        print(f"Created {len(crops)} cropped detection images")
        
        if args.output:
            print(f"Output saved to: {args.output}")
        print(f"Detection crops saved to: {camera_outputs_dir}")
    
    # Generate report
    report_path = 'alerts/report.txt' if args.output else None
    report = system.generate_report(report_path)
    print("\nAlert Report:")
    print(report)
    
    # Visualize alerts
    viz_path = 'alerts/alert_distribution.png' if args.output else None
    system.visualize_alerts(viz_path)
    
    print("Processing complete.")
    print(f"All detection crops and zoom sequences saved to: {camera_outputs_dir}")

if __name__ == '__main__':
    main()
