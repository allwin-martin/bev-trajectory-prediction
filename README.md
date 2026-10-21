# BEV Trajectory Prediction — Synthetic Baseline

A runnable educational **2D bird's-eye-view visualisation** and constant-velocity trajectory forecast. This is **not** the original fisheye-camera BEV neural network or a validated autonomous-driving model.

## Run
```bash
python -m pip install -r requirements.txt
python bev_demo.py --output bev_demo.png
python -m unittest discover -p "test_*.py"
```

## Explain
The final two observed points determine velocity; future points extrapolate at that same velocity. Demonstrate the generated image, then discuss why turns and acceleration invalidate the assumption.

## Next phase
Integrate the original Master's files, camera calibration, segmentation, dataset handling and learned trajectory prediction, with proper attribution. No benchmark performance is claimed.
