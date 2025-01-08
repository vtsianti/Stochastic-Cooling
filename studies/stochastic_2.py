import numpy as np
import matplotlib.pyplot as plt

N_particles = 1000
num_turns = 1000
Trev = 5e-7    # 500ns
Nf = 10  # split the machine into Nf parts, initializing taus
bandwidth = 0.5 * 10**9  # 0.5 GHz
W = 2.5 /( bandwidth)  # Pulse duration: 5ns


E = 3.5 * 10**9  # Particle energy in eV
mass = 0.938 * 10**9  # Mass of antiprotons in eV
ac = 0.001  # Momentum compaction factor
position_angle = np.pi / 2  # Phase advance between pickup and kicker
total_angle = 1.779 * np.pi * 3 / 2  # 1-turn phase advance -> AD
fraction = 0 # Fraction of ring covered by pickup
gain =0.001 # Gain, defines the kick

a_un = -(Trev / 2) * (1 / Nf) #The limits of my taus' uniform distribution
b_un = (Trev / 2) * (1 / Nf)

# Initializing arrays for particle states and calculations
x_final = np.zeros((num_turns, N_particles))
xp_final = np.zeros((num_turns, N_particles))
tau_final = np.zeros((num_turns, N_particles))
delta_final = np.zeros((num_turns, N_particles))
Dtau = np.zeros(N_particles)
x_temp = np.zeros(N_particles)
xp_temp = np.zeros(N_particles)
tau_temp = np.zeros(N_particles)
delta_temp = np.zeros(N_particles)

# Initial particle distributions
x = np.random.normal(0, 1, N_particles)
xp = np.random.normal(0, 1, N_particles)
delta = np.random.normal(0, 0.001, N_particles)
tau = np.random.uniform(a_un, b_un, N_particles)

X_0 = np.array([x, xp, tau, delta])
X_final = np.zeros((num_turns+1, 4, N_particles)) 
X_final[0] = X_0  #In the 1st cell, we give the initial beam

emittance_rms_initial = (np.mean(x**2) + np.mean(xp**2)) / 2  # Initial emittance
gamma = E / mass  # Relativistic gamma
hta = ac - (1 / gamma**2)  # Slip factor

# Transfer matrices
Mkick = np.array([[np.cos(position_angle), -np.sin(position_angle)], 
                  [np.sin(position_angle), np.cos(position_angle)]])
Mremain = np.array([[np.cos(total_angle - position_angle), -np.sin(total_angle - position_angle)], 
                    [np.sin(total_angle - position_angle), np.cos(total_angle - position_angle)]])




# Main loop over turns
for turns in range(num_turns):
        correction=np.zeros(N_particles)
        pos_pu=[]
        Dtau=np.zeros(N_particles)
        tau_kicker=np.zeros(N_particles)

        #we keep the positions of all the particles in the PU, the taus we have them already, we change the taus as well for all particles  
        for M in range(N_particles):
            pos_pu.append(X_final[turns][0][M])
            Dtau[M] = hta * X_final[turns][3][M] * Trev * fraction
            tau_kicker [M] = X_final[turns][2][M] + Dtau[M]
            tau_kicker[M]=((tau_kicker[M] - a_un) % (b_un - a_un)) + a_un     #We are using the mod technique to keep the taus between a_un and b_un
        

        X_fin2 = Mkick @ (X_final[turns][:2])  # Go to kicker

        
        # Calculate time delay Δτ
        
        Dtau=np.zeros(N_particles)
        neighbors_arrival_times = [[] for _ in range(N_particles)]
        neighbors_positions = [[] for _ in range(N_particles)]
        
        # Finding neighbors within the time window W
        for number_of_particle in range(N_particles):
          for M in range(N_particles):
             if tau_kicker[number_of_particle] - W/2 < X_final[turns][2][M] < tau_kicker[number_of_particle] + W/2:  #we find the particles that generated this kick 
                neighbors_arrival_times[number_of_particle].append( X_final[turns][2][M])  # we keep the starting taus, maybe we need the tau kicker, we will see
                neighbors_positions[number_of_particle].append( pos_pu[M] )

          correction[number_of_particle]  = gain * np.sum(neighbors_positions[number_of_particle])   #Calculate the kick
          X_fin2[1][number_of_particle] -= correction[number_of_particle]
          Dtau[number_of_particle] = hta * X_final[turns][3][number_of_particle] * Trev * (1 - fraction)
          tau_kicker [number_of_particle] += Dtau[number_of_particle]
          tau_kicker[M]=((tau_kicker[M] - a_un) % (b_un - a_un)) + a_un
        # Apply the correction to xp
       
        print(f'neighboring particles for a random particle', len(neighbors_positions[5]))
      
            
        

        # Calculate Δτ for the remaining fraction of the turn
        

        X_final[turns][:2]= Mremain @ (X_fin2)
        # Update X_final for the next turn
        if turns != num_turns:
            X_final[turns + 1][:2]=X_final[turns][:2]
            X_final[turns + 1][2][:] = tau_kicker[:]
            X_final[turns + 1][3][:] = X_final[turns][3][:]

        # Save temporary variables for later analysis
       

         
    # Store the current state
        x_final[turns] = X_final[turns][0][:].flatten()
        xp_final[turns] = X_final[turns][1][:].flatten()
        tau_final[turns] = X_final[turns][2][:].flatten()
        delta_final[turns] = X_final[turns][3][:].flatten()

# Emittance calculation


# Final results
print(f'The initial emittance is {emittance_rms_initial}{chr(0x03C0)} mm*mrad')
print(f'The final emittance after cooling is {emittance_rms_final[-1]}{chr(0x03C0)} mm*mrad')
print(f'Is emittance reduced? -->  {emittance_rms_final[-1] < emittance_rms_initial}')
if emittance_rms_final[-1] < emittance_rms_initial:
    print(f"Emittance is reduced by {(emittance_rms_initial - emittance_rms_final[-1]) * 100 / emittance_rms_initial}%")

# Plotting the results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 15))

# First plot: Phase Space
ax1.scatter(x, xp, color='blue', s=50, label='First Element')
ax1.scatter(x_final[-1], xp_final[-1], color='red', s=50, label='Last Element')
ax1.annotate('First', (x[0], xp[0]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
ax1.annotate('Last', (x_final[-1][0], xp_final[-1][0]), textcoords="offset points", xytext=(0, 10), ha='center', color='red')
ax1.set_xlabel('Position (x)')
ax1.set_ylabel("Angle (x')")
ax1.set_title('Phase Space')
ax1.grid(True)
ax1.set_aspect('equal', adjustable='box')

# Second plot: Emittance vs Turns
pa = np.arange(num_turns + 1) * total_angle
ax2.plot(pa / total_angle, emittance_rms_final, label='Simulation', color='blue')
ax2.set_xlabel('Turns')
ax2.set_ylabel('Emittance')
ax2.grid(True)
ax3.scatter(tau, delta, color='blue', s=50, label='First Element')
ax3.scatter(tau_final[-1], delta_final[-1], color='red', s=50, label='Last Element')
ax3.annotate('First', (tau[0], delta[0]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
ax3.annotate('Last', (tau_final[-1][0], delta_final[-1][0]), textcoords="offset points", xytext=(0, 10),ha='center', color='red')