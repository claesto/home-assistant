# My Home Assistant automations

## Introduction
One of the most exciting aspects of building a smart home is the endless possibilities for automation. Over time, I’ve developed a set of automations that help streamline my daily routines, enhance convenience, and add an extra layer of security to my home. At the moment, I’ve organized my automations into three main categories:

1. **Lighting**: Automating lights based on motion, presence, or time of day to create an efficient, comfortable living environment.
2. **Alarm & Security**: Setting up motion sensors, door/window sensors, and presence detection to ensure my home stays secure at all times.
3. **Notifications**: Sending alerts for important events like security breaches, maintenance reminders, or unexpected changes in my system.

These automations have evolved over time, and I’m always looking for new ways to enhance their functionality. Below, you can take a look at the automations I currently use, as well as some ideas I’m working on for the future to make my home even smarter.

!!! tip "Automation management"

    Since I use the `packages` approach, I manage my automations in YAML rather than through the UI.

## Automations
### Lighting
1. **Storage room & guest bathroom lighting**  
I have HUE motion sensors in these rooms that turn on the light when movement is detected and the measured lux levels are below 60.I have HUE motion sensors in these rooms that trigger the lights to turn on when motion is detected and the lux levels are below 60.
2. **Garden & front entrance lighting at sunset**  
This automation turns on the lights in the garden and at the front entrance of the house at sunset, ensuring both areas are well-lit as the day transitions into night. These lights turn off at midnight but are sensor-activated throughout the night, ensuring both areas are lit when needed.
3. **Floor lamp(s) lighting automation**
Floor lamps turn on at sunset, with the light turning off at 11:45pm unless movement is still detected on the ground floor (to make sure if we forget to turn the lights off, that it doesn't remain active during the whole night). Additionally, if we’re home and the light levels drop below a lux threshold during the day, the floor lamp is turned on. It then turns off automatically once the light levels rise above the lux threshold again.

### Alarm & security
!!! warning "Work in progress"

    I am currently in the process of completing my Home Assistant documentation.

### Notifications
1. **Garbage collection notifications**  
Notifications are sent at 8 PM the day before garbage pickups, which occur at varying times throughout the week and change each week. These notifications help me stay on top of when to put out the bins, ensuring I never miss a collection day.
2. **Severe weather notifications**
I have an automation that sends notifications when the **MeteoAlarm** sensor changes state, indicating severe weather. These notifications keep me informed about upcoming weather events, ensuring I’m always prepared for any adverse conditions.
3. **Window opening/closing for temperature control**  
 I have an automation that sends notifications to open or close the windows based on the outdoor temperature to keep the house cool during hot weather. If the outside temperature is higher or lower than the indoor temperature, the notification is adjusted accordingly to help regulate the indoor climate. An accompanying automation ensures that notifications are only sent once a day by resetting flags (input booleans), preventing repeated alerts.

## Future automation ideas
