max_sum: int = 0
best_tracks: list = []


def solve(tracks: list, target: int, current_sum: int, current_selection: list):
    global max_sum, best_tracks

    if current_sum > max_sum:
        max_sum = current_sum
        best_tracks = current_selection

    if max_sum == target:
        return

    for i in range(len(tracks)):
        track_duration = tracks[i]

        if current_sum + track_duration <= target:
            solve(
                tracks[i + 1:],
                target,
                current_sum + track_duration,
                current_selection + [track_duration]
            )


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        data = list(map(int, line.split()))
        if not data:
            continue

        n_limit = data[0]
        all_tracks = data[2:]

        max_sum = 0
        best_tracks = []

        solve(all_tracks, n_limit, 0, [])
        print(f"sum:{max_sum}")
    f.close()