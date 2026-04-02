class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        warmer_forecasts = [0] * len(temps)
        prev_temps = []
        for i, t in enumerate(temps):
            while prev_temps and prev_temps[-1][0] < t:
                _, prev_i = prev_temps.pop()
                warmer_forecasts[prev_i] = i - prev_i
            prev_temps.append((t, i))
        return warmer_forecasts