# Creating the .txt file content for the README

An intelligent microcontroller-based device that provides real-time assistance for safe and precise vehicle parking. Designed with efficiency, accuracy, and simplicity in mind, this project integrates hardware and software components to enhance the parking experience.

![Block Diagram](image-Photoroom.png)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Specifications](#hardware-specifications)
- [Software Design](#software-design)
  - [Key Algorithms](#key-algorithms)
  - [Interrupt Handling](#interrupt-handling)
  - [Power Optimization](#power-optimization)
- [Data Flow and Communication](#data-flow-and-communication)
- [Challenges and Lessons Learned](#challenges-and-lessons-learned)
- [Future Improvements](#future-improvements)


---

## Overview

The Parking Assistant is a compact, energy-efficient system that helps drivers park vehicles precisely in confined spaces. Using an STM32 microcontroller and ultrasonic sensors, the system measures real-time distances and provides intuitive LED-based feedback for users. Designed with modularity and scalability in mind, it supports dual parking configurations for left- and right-side parking.

### Key Objectives

- Simplify vehicle parking in tight spaces.
- Ensure energy-efficient operation using advanced power management techniques.
- Provide accurate distance measurement with real-time feedback.

---

## Features

### Hardware Features
- **Ultrasonic Sensor**: Accurate distance measurement using HC-SR04 sensors.
- **LED Indicators**:
  - **Blue**: Ideal distance for parking.
  - **Yellow**: Too close.
  - **Red**: Too far.
- **Button Interface**: Switch between left- and right-side parking configurations.
- **Compact Design**: 8x8x3 cm, lightweight, and easy to install.

### Software Features
- **Interrupt-Driven Architecture**: Reduces latency in distance measurement and improves power efficiency.
- **UART Communication**: Real-time debugging and data visualization.
- **Customizable Parameters**: Threshold distances and configurations are user-adjustable.

---

## System Architecture

### Block Diagram

![Block Diagram](image-Photoroom.png)

### Core Components
1. **Microcontroller (STM32)**: Manages sensor data, LED outputs, and power modes.
2. **Ultrasonic Sensor (HC-SR04)**: Measures the distance to obstacles with high precision.
3. **Button Interface**: Configures parking modes dynamically.
4. **Power Supply**: 5V via USB, with efficient power regulation.

---

## Hardware Specifications

| Component             | Details                       |
|-----------------------|-------------------------------|
| **Microcontroller**   | STM32 (ARM Cortex-M series)   |
| **Sensor**            | HC-SR04 ultrasonic sensor     |
| **LED Indicators**    | RGB LEDs for status feedback  |
| **Power**             | 5V DC, USB powered            |
| **Communication**     | UART, 115200 baud            |
| **Dimensions**        | 8cm x 8cm x 3cm               |
| **Weight**            | 150g                          |

---

## Software Design

### Key Algorithms

- **Distance Calculation**: The HC-SR04's echo pulse width is converted to distance using the formula:
  \[
  \text{Distance (cm)} = \frac{\text{Echo Time (µs)} \times 0.034}{2}
  \]
- **State Machine**:
  - **Idle**: System waits for user input.
  - **Active**: Measures distance and updates LEDs.
  - **Sleep**: Conserves power during inactivity.

### Interrupt Handling
- **Ultrasonic Echo**: Rising and falling edge detection via GPIO interrupts.
- **Button Press**: Mode toggling using edge detection.

### Power Optimization
- Sleep mode ensures minimal power consumption during idle states, achieving an idle power of 5mW.

---

## Data Flow and Communication

1. **Ultrasonic Measurement**:
   - Trigger signal sent by STM32.
   - Echo response captured by GPIO interrupts.
2. **Distance Feedback**:
   - Calculated in microcontroller.
   - LEDs indicate proximity status.
3. **Debugging and Logging**:
   - UART outputs distance measurements and system status.

---


## Challenges and Lessons Learned

### Challenges
- **Timing Precision**: Achieving microsecond-level accuracy for ultrasonic measurements.
- **Power Efficiency**: Reducing power consumption in idle states.
- **Interrupt Management**: Handling simultaneous events (e.g., button press and sensor echo).

### Lessons Learned
- Modular code design simplifies debugging and scalability.
- Real-time systems require careful timing and power management considerations.

---

## Future Improvements

- **Mobile App Integration**: Display distance and parking mode on a smartphone app via Bluetooth.
- **Enhanced Feedback**: Add audio cues for proximity warnings.
- **Advanced Sensors**: Replace HC-SR04 with LiDAR for improved accuracy.

---

