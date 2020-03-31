# Activity 11.1.4: Project 2 Plotting
# File: Team_Exercise_4_Team10.py
# Date: 3 March 2020
# By: Pranav Anandarao
# panandar
# Joseph Kawiecki
# jkawiec
# Samuel Pike
# pike16
# Tomohisa Shinagawa
# tshinaga
# Section: 1
# Team: 10
#
# ELECTRONIC SIGNATURE
# Pranav Anandarao
# Joseph Kawiecki
# Samuel Pike
# Tomohisa Shinagawa
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# Takes in data about the initial state of a pendulum
# system and outputs 3 graphs modelling the motion of
# the pendulum.
# ---------------------------------------------------
#  Inputs
# ---------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
from math import sin

sns.set()

L = float(input("What is the length L? "))
theta_prev = float(input("What is the initial angle? "))
omega_prev = float(input("What is the initial angular velocity? "))
dt = float(input("What is the time step? "))
T = float(input("What is the length of time? "))

# ---------------------------------------------------
#   Computations
# ---------------------------------------------------

t = [0]
theta = [theta_prev]
omega = [omega_prev]

for i in range(1, int(T/dt) + 1):
    t.append(i * dt)
    theta.append(theta[i - 1] + omega[i - 1] * dt)
    omega.append(omega[i - 1] - (9.81 / L) * sin(theta[i - 1]) * dt)

# ---------------------------------------------------
#   Outputs
# ---------------------------------------------------

plt.figure(1)
plt.plot(t, theta)
plt.title("Angle vs. Time")
plt.xlabel(r"$t$ (seconds)")
plt.ylabel(r"$\theta$ (radians)")

plt.figure(2)
plt.plot(t, omega)
plt.title("Angular Velocity vs. Time")
plt.xlabel(r"$t$ (seconds)")
plt.ylabel(r"$\omega$ (rad/sec)")

plt.figure(3)
plt.plot(theta, omega)
plt.title("Angular Velocity vs. Angle")
plt.xlabel(r"$\theta$ (radians)")
plt.ylabel(r"$\omega$ (rad/sec)")

plt.show()
