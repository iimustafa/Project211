"""
Main application script for the stadium crowd monitoring system.
This script demonstrates the usage of the integrated system.
"""

import os
import argparse
import tensorflow as tf
from src.system import StadiumMonitoringSystem

def main():
    """Main function to run the stadium crowd monitoring system."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Stadium Crowd Monitoring System')
    parser.add_argument('--mode', type=str, default='image', choices=['image', 'video', 'live'],
                        help='Processing mode: image, video, or live camera feed')
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
    
    args = parser.parse_args()
    
    # Create output directory if needed
    if args.output and not os.path.exists(os.path.dirname(args.output)):
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    # Initialize the system
    print("Initializing stadium crowd monitoring system...")
    system = StadiumMonitoringSystem()
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
        detections, alerts = system.process_image(
            args.input,
            output_path=args.output,
            generate_alerts=not args.no_alerts
        )
        
        print(f"Detected {len(detections)} fans")
        if not args.no_alerts:
            print(f"Generated {len(alerts)} alerts")
            
        if args.output:
            print(f"Output saved to: {args.output}")
            
    elif args.mode == 'video':
        if not args.input:
            raise ValueError("Input video path must be provided for video mode")
            
        print(f"Processing video: {args.input}")
        all_detections, all_alerts = system.process_video(
            args.input,
            output_path=args.output,
            generate_alerts=not args.no_alerts
        )
        
        total_detections = sum(len(dets) for dets in all_detections)
        print(f"Detected {total_detections} fans across all processed frames")
        
        if not args.no_alerts:
            print(f"Generated {len(all_alerts)} alerts")
            
        if args.output:
            print(f"Output saved to: {args.output}")
            
    elif args.mode == 'live':
        print(f"Processing live feed from camera {args.camera}")
        all_alerts = system.process_live_feed(
            camera_id=args.camera,
            output_path=args.output,
            generate_alerts=not args.no_alerts,
            duration=args.duration
        )
        
        if not args.no_alerts:
            print(f"Generated {len(all_alerts)} alerts")
            
        if args.output:
            print(f"Output saved to: {args.output}")
    
    # Generate report
    report_path = 'alerts/report.txt' if args.output else None
    report = system.generate_report(report_path)
    print("\nAlert Report:")
    print(report)
    
    # Visualize alerts
    viz_path = 'alerts/alert_distribution.png' if args.output else None
    system.visualize_alerts(viz_path)
    
    print("Processing complete.")

if __name__ == '__main__':
    main()
