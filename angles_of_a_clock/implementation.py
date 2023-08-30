#Implementation of python-puzzles/angles_of_a_clock

def calcAngle(hours, minutes):
  hour_angle_from_12 = (hours % 12) * 30 + minutes/2
 
  minute_angle_from_12 = minutes * 6

  clock_angle = max(hour_angle_from_12,minute_angle_from_12) - min(hour_angle_from_12,minute_angle_from_12)

  return clock_angle if clock_angle <= 180 else 360 - clock_angle

print(calcAngle(3, 30))
# 75.0
print(calcAngle(12, 30))
# 165.0
