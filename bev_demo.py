"""Synthetic BEV trajectory visualisation and constant-velocity forecast."""
import argparse

def predict(points, steps=5):
    if len(points) < 2:
        raise ValueError("Need at least two observations")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    dx, dy = x2-x1, y2-y1
    return [(x2+dx*i, y2+dy*i) for i in range(1, steps+1)]

def render(points, forecast, output):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(*zip(*points), "o-", label="observed")
    ax.plot(*zip(*([points[-1]] + forecast)), "x--", label="forecast")
    ax.set(xlabel="x (metres)", ylabel="y (metres)", title="Synthetic BEV trajectory")
    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(True)
    ax.legend()
    fig.savefig(output, dpi=160, bbox_inches="tight")
    plt.close(fig)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="bev_demo.png")
    args = parser.parse_args()
    observed = [(0,0), (1,0.4), (2,0.8), (3,1.2)]
    forecast = predict(observed)
    render(observed, forecast, args.output)
    print("Forecast:", forecast, "Output:", args.output)

if __name__ == "__main__":
    main()
