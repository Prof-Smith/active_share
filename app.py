
import streamlit as st
import pandas as pd

st.title("Active Share Calculator")

st.markdown("""
This app helps you understand the difference between passive and active portfolio managers using the **Active Share** metric.
You can enter custom weights or select a real mutual fund to see its active share.
""")

# Example mutual fund data
fund_data = {
    "Artisan Global Opportunities (ARTRX)": {
        "Stock": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
        "Portfolio Weight (%)": [25, 20, 15, 30, 10],
        "Benchmark Weight (%)": [22, 23, 18, 27, 10]
    },
    "Diamond Hill Large Cap (DHLRX)": {
        "Stock": ["JNJ", "PG", "KO", "PEP", "WMT"],
        "Portfolio Weight (%)": [20, 25, 20, 15, 20],
        "Benchmark Weight (%)": [18, 22, 25, 20, 15]
    },
    "Parnassus Small Cap (PARSX)": {
        "Stock": ["NVDA", "AMD", "INTC", "QCOM", "MU"],
        "Portfolio Weight (%)": [30, 25, 15, 20, 10],
        "Benchmark Weight (%)": [28, 20, 18, 22, 12]
    }
}

selected_fund = st.selectbox("Select a Mutual Fund for Comparison", ["Custom Input"] + list(fund_data.keys()))

if selected_fund != "Custom Input":
    df = pd.DataFrame(fund_data[selected_fund])
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
