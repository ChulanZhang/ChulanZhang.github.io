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
citation: '@inproceedings{wang2025agile3d,
    title={Agile3D: Adaptive Contention- and Content-Aware 3D Object Detection for Embedded GPUs},
    author={Wang, Pengcheng and Liu, Zhuoming and Bagchi, Shayok and Xu, Ran and Bagchi, Saurabh and Li, Yin and Chaterji, Somali},
    booktitle={The 23rd ACM International Conference on Mobile Systems, Applications, and Services},
    pages={TBD},
    year={2025},
    organization={ACM}
}'
---

<div style="display: flex; gap: 20px; margin: 20px 0; flex-wrap: wrap;">
  <a href="https://github.com/ChulanZhang/ChulanZhang.github.io/blob/pengcheng/paper/agile3d_preprint.pdf" style="display: flex; align-items: center; gap: 8px; padding: 12px 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500; transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
    📄 Paper
  </a>
  
  <a href="https://github.com/ChulanZhang/ChulanZhang.github.io/blob/pengcheng/poster/agile3d_preprint.pdf" style="display: flex; align-items: center; gap: 8px; padding: 12px 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500; transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
    🎯 Poster
  </a>
  
  <a href="https://github.com/ChulanZhang/Agile3D" style="display: flex; align-items: center; gap: 8px; padding: 12px 20px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500; transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
    💻 Code
  </a>
</div>

---

## Abstract

Efficient 3D perception is critical for autonomous systems like self-driving vehicles and drones to operate safely in dynamic environments. Accurate 3D object detection from LiDAR data faces challenges due to the irregularity and high volume of point clouds, inference latency variability from contention and content dependence, and embedded hardware constraints. Balancing accuracy and latency under dynamical conditions is crucial, yet existing frameworks like Chanakya [NeurIPS '23], LiteReconfig [EuroSys '22], and AdaScale [MLSys '19] struggle with the unique demands of 3D detection. We present Agile3D, the first adaptive 3D system to integrate a cross-model Multi-branch Execution Framework (MEF) and a Contention- and Content-Aware RL-based controller (CARL). CARL dynamically selects the optimal execution branch using five novel MEF control knobs: partitioning format, spatial resolution, spatial encoding, 3D feature extractors, and detection heads. CARL employs a dual-stage optimization strategy: Supervised pretraining for robust initial learning and Direct Preference Optimization (DPO) for fine-tuning without manually tuned rewards, inspired by techniques for training large language models. Comprehensive evaluations show that Agile3D achieves state-of-the-art performance, maintaining high accuracy across varying hardware contention levels and latency budgets of 100-500 ms. On NVIDIA Orin and Xavier GPUs, it consistently leads the Pareto frontier, outperforming existing methods for robust, efficient 3D object detection.

## Video Demo
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 20px 0;">
  <iframe 
    src="https://www.youtube.com/embed/2RrRLNWIjx4" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
    allowfullscreen>
  </iframe>
</div>

## System Overview

<img src="/images/agile3d_overview.png" alt="Agile3D System Overview" style="max-width:100%; margin: 20px 0; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" />

🚗 **Agile3D** is a multi-branch 3D object detection system equipped with a content- and contention-aware controller that adapts to both input scenes and hardware resource dynamics. It achieves superior latency-accuracy trade-offs on Waymo, nuScenes, and KITTI, running on NVIDIA Jetson embedded GPUs.

## Method & Contributions

**🏗️ Multi-branch Execution Framework (MEF)**
- Cross-model framework with five novel control knobs for dynamic adaptation
- **Innovation**: First adaptive 3D detection system integrating multi-branch execution with RL-based control

**🧠 Contention- and Content-Aware RL-based (CARL) Controller** 
- Reinforcement learning-based controller with dual-stage optimization
- **Innovation**: Content- and contention-aware adaptation eliminating manual reward engineering

**⚡ DPO Fine-tuning**
- Direct Preference Optimization guided by beam search oracle
- **Innovation**: Reward-free fine-tuning inspired by LLM training techniques

**🎯 System Impact**
- **Technical**: Novel control knobs for comprehensive 3D detection adaptation (5 dimensions)
- **Real-world**: Robust deployment on embedded GPUs for autonomous systems
- **Performance**: 3-7% accuracy improvement with Pareto frontier leadership

## Results

🏆 **3-7% accuracy improvement** over existing methods across different latency budgets  
⚡ **Robust performance** under varying contention levels (100-500 ms latency budgets)  
🚀 **Pareto frontier leadership** on NVIDIA Orin and Xavier GPUs  
🌟 **Real-world applicability** demonstrated on Waymo, nuScenes, and KITTI datasets


## Citation

**BibTeX:**

<div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 6px; padding: 15px; margin: 15px 0; font-family: 'Monaco', 'Consolas', monospace; font-size: 0.85em; line-height: 1.4; color: #495057;">
@inproceedings{wang2025agile3d,<br>
&nbsp;&nbsp;&nbsp;&nbsp;title={Agile3D: Adaptive Contention- and Content-Aware 3D Object Detection for Embedded GPUs},<br>
&nbsp;&nbsp;&nbsp;&nbsp;author={Wang, Pengcheng and Liu, Zhuoming and Bagchi, Shayok and Xu, Ran and Bagchi, Saurabh and Li, Yin and Chaterji, Somali},<br>
&nbsp;&nbsp;&nbsp;&nbsp;booktitle={The 23rd ACM International Conference on Mobile Systems, Applications, and Services},<br>
&nbsp;&nbsp;&nbsp;&nbsp;year={2025},<br>
&nbsp;&nbsp;&nbsp;&nbsp;organization={ACM}<br>
}
</div>

## Acknowledgements

This material is based in part upon work supported by the National Science Foundation under Grant Numbers CNS-2333491 / 2333487 (NSF Frontier) and CNS-2146449 (NSF CAREER award), and by the Army Research Lab under contract number W911NF-2020221. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the sponsors. The authors thank the reviewers and artifact evaluators for their enthusiastic comments, and the anonymous shepherd for their insightful feedback.
