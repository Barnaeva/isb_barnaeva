from .find_card import FindCard
from matplotlib import pyplot as plt
import time


class MeasuringTime:

    @staticmethod
    def meas_time(
        bins: list[str], last_digits: str, target_hash: str
    ) -> list[tuple[int, float]]:
        """
        Measures the time to find a hash collision for a different number of processes

        :param bins: bins
        :param last_digits: last 4 digits
        :param target_hash: target hash
        :return: measurement result
        """
        num_cor = FindCard.number_of_cores()
        num_cor *= 1.5
        time_res = []
        for i in range(1, int(num_cor + 1)):

            time_start = time.time()
            FindCard.find_card_parallel(bins, last_digits, target_hash, i)
            time_end = time.time()
            all_time = time_end - time_start
            time_res.append((i, all_time))
            print(f"Cores: {i}, Time: {all_time:.2f} sec")

        return time_res

    @staticmethod
    def plot_time(time_res: list[tuple[int, float]]) -> None:
        """
        The function visualizes the dependence of the collision detection time on the number of processes.
        :param time_res: measurement result
        :return: None
        """
        cores = [x[0] for x in time_res]
        times = [x[1] for x in time_res]

        min_time = min(times)
        best_cores = cores[times.index(min_time)]

        plt.figure(figsize=(10, 5))

        plt.plot(
            cores,
            times,
            color="pink",
            marker="o",
            linestyle="-",
            linewidth=2,
            markersize=8,
            label="Execution time",
        )

        plt.scatter(
            [best_cores],
            [min_time],
            color="red",
            s=200,
            label=f"Best: {best_cores} processes",
            zorder=3,
        )

        plt.title("Time measurement schedule")
        plt.xlabel("Number of processes")
        plt.ylabel("Time (seconds)")

        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()
        plt.show()
