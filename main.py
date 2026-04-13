"""Lab 10 - Data Visualization.

Loads reaction time data from a CSV file, creates a line graph, and
saves the visualization as an image.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


def load_reaction_data(csv_path: Path) -> tuple[list[int], list[float]]:
	"""Load trial numbers and reaction times from a CSV file."""
	trials: list[int] = []
	reaction_times: list[float] = []

	with csv_path.open(newline="", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			trials.append(int(row["Trial"]))
			reaction_times.append(float(row["ReactionTime_ms"]))

	return trials, reaction_times


def create_plot(trials: list[int], reaction_times: list[float], output_path: Path) -> None:
	"""Create and save a reaction-time plot."""
	plt.figure(figsize=(8, 5))
	plt.plot(trials, reaction_times, marker="o", linewidth=2, color="tab:blue")
	plt.title("Reaction Time Across Trials")
	plt.xlabel("Trial")
	plt.ylabel("Reaction Time (ms)")
	plt.grid(True, linestyle="--", alpha=0.5)
	plt.tight_layout()
	plt.savefig(output_path)
	plt.close()


def main() -> None:
	"""Run the data visualization workflow for the lab."""
	base_dir = Path(__file__).parent
	csv_path = base_dir / "reaction_time_data.csv"
	output_path = base_dir / "output.png"

	trials, reaction_times = load_reaction_data(csv_path)
	create_plot(trials, reaction_times, output_path)

	print(f"Graph saved to {output_path.name}")


if __name__ == "__main__":
	main()
