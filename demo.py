"""
Example script demonstrating the enhanced stadium monitoring system with camera control and zoom.
This script shows how to use the system with a sample image.
"""

import os
import cv2
import numpy as np
import argparse
from src.enhanced_system import EnhancedStadiumMonitoringSystem

def create_sample_image(output_path, width=512, height=384):
    """Create a sample stadium image with fans for demonstration."""
    # Create a blank image
    image = np.ones((height, width, 3), dtype=np.uint8) * 150  # Gray background
    
    # Draw some "seats"
    for y in range(100, 350, 30):
        cv2.rectangle(image, (10, y), (width-10, y + 20), (80, 80, 80), -1)
    
    # Draw some "fans"
    # Hilal fans (blue)
    for i in range(5):
        x = 50 + i * 40
        y = 150
        # Body
        cv2.rectangle(image, (x, y), (x+20, y+40), (255, 0, 0), -1)  # Blue
        # Head
        cv2.circle(image, (x+10, y-10), 10, (255, 224, 189), -1)  # Face
        
        # Random action
        action = np.random.choice(['sitting', 'cheering', 'fighting', 'throwing'])
        if action == 'cheering':
            # Arms up
            cv2.line(image, (x+10, y+5), (x-10, y-15), (255, 0, 0), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+30, y-15), (255, 0, 0), 3)  # Right arm
        elif action == 'fighting':
            # Arms fighting
            cv2.line(image, (x+10, y+5), (x-5, y+15), (255, 0, 0), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+25, y+15), (255, 0, 0), 3)  # Right arm
        elif action == 'throwing':
            # Arm throwing
            cv2.line(image, (x+10, y+5), (x+30, y), (255, 0, 0), 3)  # Right arm
        else:  # sitting
            # Arms down
            cv2.line(image, (x+10, y+5), (x-5, y+20), (255, 0, 0), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+25, y+20), (255, 0, 0), 3)  # Right arm
    
    # Ittihad fans (gold)
    for i in range(5):
        x = 300 + i * 40
        y = 150
        # Body
        cv2.rectangle(image, (x, y), (x+20, y+40), (0, 215, 255), -1)  # Gold
        # Head
        cv2.circle(image, (x+10, y-10), 10, (255, 224, 189), -1)  # Face
        
        # Random action
        action = np.random.choice(['sitting', 'cheering', 'fighting', 'throwing'])
        if action == 'cheering':
            # Arms up
            cv2.line(image, (x+10, y+5), (x-10, y-15), (0, 215, 255), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+30, y-15), (0, 215, 255), 3)  # Right arm
        elif action == 'fighting':
            # Arms fighting
            cv2.line(image, (x+10, y+5), (x-5, y+15), (0, 215, 255), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+25, y+15), (0, 215, 255), 3)  # Right arm
        elif action == 'throwing':
            # Arm throwing
            cv2.line(image, (x+10, y+5), (x+30, y), (0, 215, 255), 3)  # Right arm
        else:  # sitting
            # Arms down
            cv2.line(image, (x+10, y+5), (x-5, y+20), (0, 215, 255), 3)  # Left arm
            cv2.line(image, (x+10, y+5), (x+25, y+20), (0, 215, 255), 3)  # Right arm
    
    # Add a misplaced fan (Hilal fan in Ittihad section)
    x, y = 350, 200
    # Body
    cv2.rectangle(image, (x, y), (x+20, y+40), (255, 0, 0), -1)  # Blue
    # Head
    cv2.circle(image, (x+10, y-10), 10, (255, 224, 189), -1)  # Face
    
    # Add some fighting fans
    x1, y1 = 150, 250
    x2, y2 = 170, 250
    # Bodies
    cv2.rectangle(image, (x1, y1), (x1+20, y1+40), (255, 0, 0), -1)  # Blue
    cv2.rectangle(image, (x2, y2), (x2+20, y2+40), (0, 215, 255), -1)  # Gold
    # Heads
    cv2.circle(image, (x1+10, y1-10), 10, (255, 224, 189), -1)  # Face
    cv2.circle(image, (x2+10, y2-10), 10, (255, 224, 189), -1)  # Face
    # Fighting arms
    cv2.line(image, (x1+10, y1+5), (x1+25, y1+15), (255, 0, 0), 3)  # Blue arm
    cv2.line(image, (x2+10, y2+5), (x2-5, y2+15), (0, 215, 255), 3)  # Gold arm
    
    # Save the image
    cv2.imwrite(output_path, image)
    return output_path

def main():
    """Main function to demonstrate the enhanced stadium monitoring system."""
    parser = argparse.ArgumentParser(description='Enhanced Stadium Monitoring System Demo')
    parser.add_argument('--output-dir', type=str, default='demo_outputs',
                        help='Directory to save outputs')
    parser.add_argument('--create-sample', action='store_true',
                        help='Create a sample image for demonstration')
    parser.add_argument('--input', type=str, default=None,
                        help='Path to input image (if not creating sample)')
    args = parser.parse_args()
    
    # Create output directories
    os.makedirs(args.output_dir, exist_ok=True)
    camera_outputs_dir = os.path.join(args.output_dir, 'camera_outputs')
    zoom_outputs_dir = os.path.join(args.output_dir, 'zoom_outputs')
    os.makedirs(camera_outputs_dir, exist_ok=True)
    os.makedirs(zoom_outputs_dir, exist_ok=True)
    
    # Create or use input image
    if args.create_sample or args.input is None:
        input_path = os.path.join(args.output_dir, 'sample_stadium.jpg')
        create_sample_image(input_path)
        print(f"Created sample image: {input_path}")
    else:
        input_path = args.input
        print(f"Using provided image: {input_path}")
    
    # Initialize the enhanced system
    print("Initializing enhanced stadium monitoring system...")
    system = EnhancedStadiumMonitoringSystem(config={
        'model_dir': 'models',
        'alerts_dir': args.output_dir,
        'camera_outputs_dir': camera_outputs_dir,
        'zoom_outputs_dir': zoom_outputs_dir,
        'zoom_level': 2.5,
        'scan_speed': 15,
        'scan_pattern': 'grid',
        'stadium_sections': {
            'hilal': [0, 0, 256, 384],  # Left half of stadium
            'ittihad': [256, 0, 512, 384]  # Right half of stadium
        }
    })
    
    system.initialize()
    
    # Process the image
    print(f"Processing image: {input_path}")
    output_path = os.path.join(args.output_dir, 'output.jpg')
    detections, alerts, results = system.process_image(
        input_path,
        output_path=output_path,
        generate_alerts=True,
        zoom_on_detections=True
    )
    
    print(f"Detected {len(detections)} fans")
    print(f"Generated {len(alerts)} alerts")
    
    print("\nGenerated outputs:")
    print(f"Crops: {len(results['crops'])}")
    print(f"Zoom sequences: {len(results['sequences'])}")
    print(f"Zoom GIFs: {len(results['zooms'])}")
    print(f"Zoom animations: {len(results['animations'])}")
    print(f"Detection grids: {len(results['grids'])}")
    
    print(f"\nOutput image saved to: {output_path}")
    print(f"Detection crops saved to: {zoom_outputs_dir}")
    print(f"Zoom sequences saved to: {zoom_outputs_dir}/sequences")
    print(f"Zoom GIFs saved to: {zoom_outputs_dir}/gifs")
    
    # Also demonstrate the scan and monitor functionality
    print("\nDemonstrating scan and monitor functionality...")
    scan_output_path = os.path.join(args.output_dir, 'scan_output.jpg')
    scan_detections, scan_alerts, scan_results = system.scan_and_monitor(
        input_path,
        output_path=scan_output_path,
        generate_alerts=True
    )
    
    print(f"Scan detected {len(scan_detections)} fans")
    print(f"Scan generated {len(scan_alerts)} alerts")
    
    print("\nScan generated outputs:")
    print(f"Scans: {len(scan_results['scans'])}")
    print(f"Crops: {len(scan_results['crops'])}")
    print(f"Zoom sequences: {len(scan_results['sequences'])}")
    print(f"Zoom GIFs: {len(scan_results['zooms'])}")
    print(f"Zoom animations: {len(scan_results['animations'])}")
    print(f"Detection grids: {len(scan_results['grids'])}")
    
    print(f"\nScan output image saved to: {scan_output_path}")
    print(f"Scan crops saved to: {zoom_outputs_dir}/scans")
    
    print("\nDemo complete. Use these images for security alerts and monitoring.")

if __name__ == '__main__':
    main()
