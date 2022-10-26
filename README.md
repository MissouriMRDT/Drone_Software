# Drone Flight Computer Software
<!-- ![GitHub release (latest by date)](https://img.shields.io/github/v/release/MissouriMRDT/Flight_Computer_Software?style=flat) -->
![GitHub pull requests](https://img.shields.io/github/issues-pr/MissouriMRDT/Flight_Computer_Software?style=flat)
![GitHub issues](https://img.shields.io/github/issues/MissouriMRDT/Flight_Computer_Software)
<!-- ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MissouriMRDT/Flight_Computer_Software/Autonomy%20Flake8%20Linter/dev?label=flake8%20linter&style=flat) -->
<!-- ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MissouriMRDT/Flight_Computer_Software/Autonomy%20Unit%20Tests/dev?label=unit%20tests&style=flat) -->

## Install
1. Download and Install VirtualBox
```
https://www.virtualbox.org/wiki/Downloads
```

2. Download the Virtual Box OVA
```
https://drive.google.com/file/u/1/d/1fZ5l2liZ2T0wOKOBtkh47uGF_OQAomo9/view
```

3. Clone this Repository
```
git clone https://github.com/MissouriMRDT/Flight_Computer_Software.git ros2_ws
```

## Build and Run
1. Open ROS2 Workspace
```
cd ros2_ws/
```

2. Execute Continuous Colcon Build
```
colcon build --symlink-install
```

3. Update Source
```
source ~/.bashrc
```

4. Run ROS2
```
ros2 run autonomy <node_name>
```
