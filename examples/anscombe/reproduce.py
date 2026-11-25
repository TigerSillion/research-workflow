"""Recompute the four regressions from the published observations."""
import csv
import hashlib
import platform
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent


def fit(points):
    xs, ys = zip(*points)
    xbar, ybar = mean(xs), mean(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    if sxx == 0:
        raise ValueError("constant x: slope is unidentifiable")
    slope = sum((x - xbar) * (y - ybar) for x, y in points) / sxx
    intercept = ybar - slope * xbar
    residual = sum((y - intercept - slope * x) ** 2 for x, y in points)
    total = sum((y - ybar) ** 2 for y in ys)
    return intercept, slope, 1 - residual / total


def plot(groups, output):
    elements = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 450">',
                '<title>Anscombe quartet: observations and least-squares fits</title>',
                '<rect width="100%" height="100%" fill="white"/>',
                '<g font-family="sans-serif" font-size="12" fill="#203147">']
    for i, points in enumerate(groups):
        left = 45 + 337 * (i % 2)
        top = 35 + 223 * (i // 2)
        def px(x):
            return left + 13 * x
        def py(y):
            return top + 160 - 10 * y
        def line(x1, y1, x2, y2, color):
            elements.append(f'<line x1="{px(x1)}" y1="{py(y1)}" x2="{px(x2)}" y2="{py(y2)}" stroke="{color}"/>')
        elements.append(f'<text x="{left}" y="{top-8}" font-size="16">Dataset {i+1}</text>')
        for x in (0, 5, 10, 15, 20):
            line(x, 0, x, 15, "#dce2e8")
            elements.append(f'<text x="{px(x)}" y="{py(0)+16}" text-anchor="middle">{x}</text>')
        for y in (0, 5, 10, 15):
            line(0, y, 20, y, "#dce2e8")
            elements.append(f'<text x="{left-7}" y="{py(y)+4}" text-anchor="end">{y}</text>')
        elements.append(f'<text x="{px(20)+12}" y="{py(0)}">x</text>')
        elements.append(f'<text x="{left-20}" y="{py(15)}">y</text>')
        intercept, slope, _ = fit(points)
        line(0, intercept, 20, intercept + 20*slope, "#c34432")
        for x, y in points:
            elements.append(f'<circle cx="{px(x)}" cy="{py(y)}" r="3.7" fill="#165b83"/>')
    output.write_text("\n".join(elements + ["</g></svg>"]), encoding="utf-8")


def main():
    data = HERE / "data.csv"
    with data.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    groups = []
    passed = True
    print("Python", platform.python_version(), "CSV SHA256", hashlib.sha256(data.read_bytes()).hexdigest())
    print("set  n  intercept     slope        R2  match")
    for i in range(1, 5):
        xfield = "x4" if i == 4 else "x123"
        points = [(float(row[xfield]), float(row[f"y{i}"])) for row in rows]
        groups.append(points)
        intercept, slope, r2 = fit(points)
        match = (len(points) == 11 and abs(intercept-3) <= 0.005
                 and abs(slope-0.5) <= 0.001 and abs(r2-0.667) <= 0.001)
        passed = passed and match
        print(f"{i:3} {len(points):2} {intercept:10.6f} {slope:9.6f} {r2:9.6f}  {match}")
    output = HERE / "output"
    output.mkdir(exist_ok=True)
    plot(groups, output / "figure.svg")
    print(output / "figure.svg")
    reduced = [(x, y) for x, y in groups[3] if x != 19]
    if len(reduced) != len(groups[3]) - 1 or len({x for x, _ in reduced}) != 1:
        raise SystemExit("Sensitivity check differed from prediction")
    print("Set 4 without x=19: constant x; slope is unidentifiable.")
    if not passed:
        raise SystemExit("Baseline differed from protocol")


if __name__ == "__main__":
    main()
