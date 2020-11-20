import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_samples = 100
x = np.random.rand(number_of_samples) + np.random.randint(0, 10, number_of_samples)

y = np.random.rand(number_of_samples) + np.random.randint(0, 10, number_of_samples)

event_a_radius = np.random.randint(1, 5)
event_a_center = np.random.randint(event_a_radius, 10 - event_a_radius)

event_b_radius = np.random.randint(1, 5)
event_b_center = np.random.randint(event_b_radius, 10 - event_b_radius)

a_count = 0
b_count = 0
joint_count = 0

for i in enumerate(x):

    # count samples in event a

    if (
        np.sqrt(
            (x[i[0]] - event_a_center[0]) ** 2
            + (y[i[0]] - event_a_center[1]) ** 2
        )
        <= event_a_radius
    ):
        a_count += 1

    # count samples in event b

    if (
        np.sqrt(
            (x[i[0]] - event_b_center[0]) ** 2
            + (y[i[0]] - event_b_center[1]) ** 2
        )
        <= event_b_radius
    ):
        b_count += 1

    # count samples in the intersection of a and b

    if (
        np.sqrt(
            (x[i[0]] - event_a_center[0]) ** 2
            + (y[i[0]] - event_a_center[1]) ** 2
        )
        <= event_a_radius
        and np.sqrt(
            (x[i[0]] - event_b_center[0]) ** 2
            + (y[i[0]] - event_b_center[1]) ** 2
        )
        <= event_b_radius
    ):
        joint_count += 1

# calculate the marginal probabilities

Prob_a = a_count / len(x)
Prob_b = b_count / len(x)

# calculate the joint probabilities

Joint_prob = joint_count / len(x)

# calculate the conditional probabilities

A_given_B = Joint_prob / Prob_b
B_given_A = Joint_prob / Prob_a

print(
    "The probability of Event A is %s, and the probability of Event A given Event B is %s"
    % (Prob_a, np.round(A_given_B, 2))
)
print(
    "The probability of Event B is %s, and the probability of Event B given Event B is %s"
)

print (
    "The joint probability is %s and the probability of Event A times the probability of Event B is %s, are the events independent?"
    % (Joint_prob, np.round(Prob_a * Prob_b, 2))
)

event_a = plt.Circle(
    event_a_center, event_a_radius, fc="g", ec="g", zorder=0, alpha=0.2
)

event_b = plt.Circle(
    event_b_center, event_b_radius, fc="b", ec="b", zorder=0, alpha=0.2
)
fig, ax = plt.subplots(figsize=(10, 10))
ax.add_patch(event_a)
ax.add_patch(event_b)
ax.legend([event_a, event_b], ["Event A", "Event B"])
plt.scatter(x, y, c="k", label="Sample")
plt.xlim(0, 10)
plt.ylim(0, 10)

plt.show()