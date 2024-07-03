# Project Goals
1. Select and implement a machine learning algorithm that could successfully create a route and deliver all of the packages.
2. Select and implement a self-adjusting data structure that would be used to store package information.
3. Design a program that will effectively keep track of all package information, and calculate estimated delivery times, truck mileage traveled, and any other relevant factors.
4. Create a UI that a delivery manager could use to get updates on package information as they are being delivered.

## Project Constraints
1. The total delivery truck mileage can not exceed 140 miles.
2. Package deadlines must be met, including delivery times throughout the day.
3. All packages must be delivered before the day is finished.
4. There are only 3 delivery trucks and 2 drivers.

## Project Summary
- The **greedy algorithm** was selected because of its simple approach to solving the problem. It operates by immediately selecting the shortest local route, without considering the global solution.
- **Hash tables** were used to store package information and hub information (including distances from the hub to a delivery address). This is a simple and effective data structure that is capable of storing large volumes of data. Chaining is used for collision handling.
- Classes were created to calculate distances between points, estimate delivery times, track actual delivery times, and track total truck mileage.
- A command line UI was created with simple menu options to run different reports. The user can enter a package ID and time to look up specific packages.
