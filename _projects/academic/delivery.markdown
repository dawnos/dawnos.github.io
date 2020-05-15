---
layout: single
title:  "Delivery Mobile Robot"
date: 2016-06-30 21:00:00 +0800
header:
  teaser: /assets/images/jd.jpg
---

Collaborated with JD.com to develop a last mile delivery robot. The robot is targeted at long-term autonomous navigation in off-road environment (e.g. campus, community). This Ackermann platform based robot has a interface for users to pick up parcels. 3D LiDAR, IMU and stereo camera are used for mapping and localization. 2D LiDAR is mounted at the bottom for obstacle avoidance. The crucial challenge lies in long-term localization.

![](/assets/images/jd.jpg){:width="500px" .align-center}

I built the firmware (such as motors driving and sensors synchronization) and designed the software architecture (mapping, localization and navigation). To deal with failure of matching in long-term localization, TLF was proposed. In TLF, the map is organized in a topological form. Localization is performed in a local neighbourhood to relax global consistency. When sensory data fails to match with the map, it will be stored in the map for localization in the future. With TLF, constant memory and computation was achieved, with ever growing localization performance. The robot was deployed on a route over χև։ with autonomous navigation for delivery in our campus.

{% include video id="3LOYvHnh5GY" provider="youtube" %}
