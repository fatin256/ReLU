import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.write("ReLU(x) = max(0, x)")

x = np.linspace(-10, 10, 400)
y = np.maximum(0, x)

plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.grid(True)

st.pyplot(plt)
