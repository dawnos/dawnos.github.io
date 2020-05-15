---
layout: single
title:  "Autonomous Driving Platform"
date: 2019-11-01 21:00:00 +0800
header:
  teaser: /assets/images/thomas-car.jpg
---
To collect data for research topics on long-term autonomous driving, we developed a sensory platform on a car. The platform is equipped with multiple sensors (3D LiDARs, cameras, IMU, INS). Currently it has one 32-line 3D LiDAR on the top, two 16-line 3D LiDARs on the sides, two stereo cameras facing forward, three fisheye cameras facing left/right/rear, and an IMU. It also has an INS for ground truth.

With the lessons learned from several previous projects, I redesign the synchronization system to synchronize every sensors in this platform. Details will be presented later.

This project is still on progress. We are planning to release the dataset to help the community.
