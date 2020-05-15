---
layout: single
title:  "Amazon Picking Challenge"
date: 2014-09-01 21:00:00 +0800
header:
  teaser: /assets/images/apc.jpg
---

Cooperated with UTS (University of Technology Sydney) to participate in Amazon Picking Challenge (APC) on ICRA2015

(https://youtu.be/f2LEatcHz94). Robots in APC are intended for packing and sorting in logistics. In APC, participants are required to design a robot to finish shelf-picking task according to a given shopping list. Our team has designed a two-arm robot. It can grasp multiple objects simultaneously, which increases efficiency by minimizing movement and expanding work space. RGB and depth cameras are mounted on the head for perception. The primary challenges for perception are perspective and limited field of view.

I designed an object recognition and pose estimation system to assist grasping. Camera calibration and hand-eye calibration were also parts of my work. RGB cameras were used for object recognition using Kernel Descriptor and CNN, while depth cameras were leveraged to capture convexes or bounding boxes of target objects. For goods with rich texture, MOPED was used for pose estimation. We took the 5th place in the final competition.
