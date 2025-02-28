## Parking Assistant Embedded Systems Project
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
- [Embedded Systems Learning outcomes](#Embedded-Systems-Learning-outcomes).
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
  - **Blue**: Ideal distance for parking. ![Blue State](BlueState.jpg)
  - **Yellow**: Too close.![Yellow State](YellowState.jpg)
  - **Red**: Too far.![Red State](RedState.jpg)
- **Button Interface**: Switch between left- and right-side parking configurations.
- **Compact Design**: 8x8x3 cm, lightweight, and easy to install.





### Software Features
- **Interrupt-Driven Architecture**: Reduces latency in distance measurement and improves power efficiency.
- **UART Communication**: Real-time debugging and data visualization.
- **Customizable Parameters**: Threshold distances and configurations are user-adjustable.

---

## System Architecture

### Block Diagram

![Block Diagram](BlockDiagram.png)

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
![UltraSonicTiming](UltraSonicTiming.PNG)

- **Timing Configuration for Ultrasonic Sensor**:
  -The Parking Assistant uses an STM32 timer (TIM1) to measure the time it takes for the ultrasonic signal to travel to the obstacle and back. This section explains how the timing is achieved and the math behind it.
  -Prescaler: 719 divides the system clock frequency by 720 (Prescaler + 1).
  -Period: The timer counts from 0 to 65535.
  - ![Systick](SysTick.png)
  - Prescaler: Divides the system clock to achieve a timer tick rate of 100 kHz (10 µs per tick).
  - Timer Measurements: Captures the time between the rising and falling edges of the echo signal.
  - Distance Calculation: Converts time into distance using the speed of sound formula.
  
  
- **State Machine**:
  - **Idle**: System waits for user input.
  - **Active**: Measures distance and updates LEDs.
  - **Sleep**: Conserves power during inactivity.

### Interrupt Handling
- **Ultrasonic Echo**: Rising and falling edge detection via GPIO interrupts.
- **Button Press**: Mode toggling using edge detection. Used a 10uF capacitor in order to deal with debouoncing issues as seen here: 
![PushButton](PushButton.jpg)
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
- **Debouncing**: Push button debouncing, was fixed via hardware with a capacitor to smooth out these unintentianal presses.

### Lessons Learned
- Modular code design simplifies debugging and scalability.
- Real-time systems require careful timing and power management considerations.
  
### Embedded Systems Learning outcomes
- UART: Serial communication for debugging and data transfer.
- Interrupts: Real-time response to Echo signal edges and button presses.
- SysTick Timer: Internal timer for delays and periodic events.
- General-Purpose Timers (TIM1): Precise timing for ultrasonic sensor measurements.
- GPIO: Configured for input (Echo, button) and output (Trigger, LEDs).
- PWM (Pulse Width Measurement): Used indirectly by timing the Echo pulse.
- Power Management: Implementing sleep mode to reduce idle power consumption.
- State Machine: Managing Idle, Active, and Sleep states for efficiency.
- Mathematical Modeling: Converting Echo time to distance using speed of sound.
- GPIO Interrupt Prioritization: Handling simultaneous events like Echo and button presses.
- Clock Management: Configuring prescaler for timer resolution (10 µs tick).
- Real-Time Feedback: Using LEDs to provide immediate visual output based on distance.
- Debouncing: Button press handling for mode toggling.

---

## Future Improvements

- **Mobile App Integration**: Display distance and parking mode on a smartphone app via Bluetooth.
- **Enhanced Feedback**: Add audio cues for proximity warnings.
- **Advanced Sensors**: Replace HC-SR04 with LiDAR for improved accuracy.
- - **Prototype**: Complete the final prototype and make a PCB for this project.
![Prototype](Prototype.jpg)
---

