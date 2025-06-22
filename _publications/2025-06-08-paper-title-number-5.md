---
title: "Agile3D: Adaptive Contention- and Content-Aware 3D Object Detection for Embedded GPUs"
collection: publications
category: conferences
permalink: /publication/agile3d
excerpt: 'A novel approach for efficient 3D object detection on embedded GPUs with adaptive contention and content awareness.'
date: 2025-06-08
venue: 'The 23rd ACM International Conference on Mobile Systems, Applications, and Services (MobiSys 2025)'
authors: 'Pengcheng Wang, Zhuoming Liu, Shayok Bagchi, Ran Xu, Saurabh Bagchi, Yin Li, Somali Chaterji'
slidesurl: 'https://your-slides-url.com'
paperurl: 'https://your-paper-url.com'
bibtexurl: 'https://your-bibtex-url.com'
citation: '@misc{agil3d,
    title={Agile3D: Adaptive Contention- and Content-Aware 3D Object Detection for Embedded GPUs},
    author={Wang, Pengcheng and Liu, Zhuoming and Bagchi, Shayok and Xu, Ran and Bagchi, Saurabh and Li, Yin and Chaterji, Somali},
    howpublished = {The 23rd ACM International Conference on Mobile Systems, Applications, and Services},
    year={2025}
}'
---
Abstract:  
Efficient 3D perception is critical for autonomous systems like self-driving vehicles and drones to operate safely in dynamic environments. Accurate 3D object detection from LiDAR data faces challenges due to the irregularity and high volume of point clouds, inference latency variability from contention and content dependence, and embedded hardware constraints. Balancing accuracy and latency under dynamical conditions is crucial, yet existing frameworks like Chanakya [NeurIPS '23], LiteReconfig [EuroSys '22], and AdaScale [MLSys '19] struggle with the unique demands of 3D detection. We present Agile3D, the first adaptive 3D system to integrate a cross-model Multi-branch Execution Framework (MEF) and a Contention- and Content-Aware RL-based controller (CARL). CARL dynamically selects the optimal execution branch using five novel MEF control knobs: partitioning format, spatial resolution, spatial encoding, 3D feature extractors, and detection heads. CARL employs a dual-stage optimization strategy: Supervised pretraining for robust initial learning and Direct Preference Optimization (DPO) for fine-tuning without manually tuned rewards, inspired by techniques for training large language models. Comprehensive evaluations show that Agile3D achieves state-of-the-art performance, maintaining high accuracy across varying hardware contention levels and latency budgets of 100-500 ms. On NVIDIA Orin and Xavier GPUs, it consistently leads the Pareto frontier, outperforming existing methods for robust, efficient 3D object detection.

## Video Demo

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 20px 0;">
  <iframe 
    src="https://www.youtube.com/embed/2RrRLNWIjx4" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
    allowfullscreen>
  </iframe>
</div>

<!-- ## Key Contributions

- **Adaptive Contention Management**: Novel approach to handle GPU resource contention
- **Content-Aware Processing**: Intelligent processing based on content characteristics  
- **Embedded GPU Optimization**: Specifically designed for resource-constrained devices -->

<!-- ## Results

Our experimental results show significant improvements in both performance and energy efficiency compared to state-of-the-art methods. -->
