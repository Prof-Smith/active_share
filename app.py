
import streamlit as st
import pandas as pd

st.title("Active Share Calculator")

st.markdown("""
This app helps you understand the difference between passive and active portfolio managers using the **Active Share** metric.
Enter the weights of stocks in a portfolio and its benchmark to calculate the active share.
""")

st.header("📊 Input Portfolio and Benchmark Weights")

# Example data
example_data = {
    "Stock": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
    "Portfolio Weight (%)": [20, 25, 15, 30, 10],
    "Benchmark Weight (%)": [22, 23, 18, 27, 10]
}

df = pd.DataFrame(example_data)

edited_df = st.data_editor(df, num_rows="dynamic")

# Calculate active share
if st.button("Calculate Active Share"):
    portfolio_weights = edited_df["Portfolio Weight (%)"] / 100
    benchmark_weights = edited_df["Benchmark Weight (%)"] / 100
    active_share = 0.5 * sum(abs(portfolio_weights - benchmark_weights)) * 100

    st.subheader("🔍 Result")
    st.write(f"**Active Share:** {active_share:.2f}%")

    if active_share < 20:
        st.info("This portfolio is likely passive or a closet indexer.")
    elif active_share < 60:
        st.warning("This portfolio shows moderate activity.")
    else:
        st.success("This portfolio is actively managed.")

st.markdown("""
---
**Formula:** Active Share = ½ × Σ |Portfolio Weight − Benchmark Weight|
""")
