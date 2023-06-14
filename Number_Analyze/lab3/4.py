import numpy as np
import matplotlib.pyplot as plt

num_segments = 10
segment_length = 100
num_time_steps = 100
Δt = 0.1
Δx = segment_length / num_segments

Vmax = 30 
ρmax = 10 

ρ = np.zeros(num_segments)
v = np.zeros(num_segments)

ρ[0] = 5 
v[:] = Vmax * (1 - ρ[:] / ρmax)  

ρ_data = np.zeros((num_time_steps, num_segments))
v_data = np.zeros((num_time_steps, num_segments))

# Perform simulation
for step in range(num_time_steps):
    for i in range(1, num_segments):
        ρ[i] = ρ[i] - Δt * (ρ[i] * v[i] - ρ[i-1] * v[i-1]) / Δx  
        v[i] = Vmax * (1 - ρ[i] / ρmax)


    q = ρ * v
    ρ_data[step] = ρ
    v_data[step] = v
    t = (step + 1) * Δt

x = np.linspace(0, segment_length, num_segments)
t = np.arange(num_time_steps) * Δt

#traffic density
plt.figure(figsize=(8, 6))
for i in range(num_segments):
    plt.plot(t, ρ_data[:, i], label=f"Segment {i+1}")
plt.xlabel("Time")
plt.ylabel("Traffic Density")
plt.title("Traffic Density over Time")
plt.legend()
plt.grid(True)
plt.show()

# traffic velocity
plt.figure(figsize=(8, 6))
for i in range(num_segments):
    plt.plot(t, v_data[:, i], label=f"Segment {i+1}")
plt.xlabel("Time")
plt.ylabel("Traffic Velocity")
plt.title("Traffic Velocity over Time")
plt.legend()
plt.grid(True)
plt.show()
