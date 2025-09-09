
import streamlit as st
import pandas as pd

st.title("Active Share Calculator")

st.markdown("""
This app helps you understand the difference between passive and active portfolio managers using the **Active Share** metric.
You can enter custom weights or select the Artisan Global Opportunities Fund (ARTRX) to see its active share.
""")

# Real holdings for ARTRX (simplified top holdings)
artrx_data = {
    "Stock": ["NFLX", "BSX", "TSMC", "ARGX", "AMD", "LSEG", "TENCENT", "AMZN", "AAPL", "ADIDAS"],
    "Portfolio Weight (%)": [5.10, 5.00, 4.52, 4.03, 3.65, 3.64, 3.22, 3.09, 2.94, 2.82],
    "Benchmark Weight (%)": [1.20, 0.80, 1.50, 0.40, 1.10, 0.60, 0.90, 2.50, 3.00, 0.70]  # MSCI ACWI approximations
}

selected_fund = st.selectbox("Select Portfolio", ["Custom Input", "Artisan Global Opportunities Fund (ARTRX)"])

if selected_fund == "Artisan Global Opportunities Fund (ARTRX)":
    df = pd.DataFrame(artrx_data)
else:
    st.header("📊 Input Portfolio and Benchmark Weights")
    example_data = {
        "Stock": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
        "Portfolio Weight (%)": [20, 25, 15, 30, 10],
        "Benchmark Weight (%)": [22, 23, 18, 27, 10]
    }
    df = pd.DataFrame(example_data)

edited_df = st.data_editor(df, num_rows="dynamic")

# Calculate active share
if st.button("Calculate Active Share"):
    if edited_df[["Portfolio Weight (%)", "Benchmark Weight (%)"]].isnull().values.any():
        st.error("Please fill in all portfolio and benchmark weights before calculating.")
    else:
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
