import streamlit as st
import yfinance as yf
import pandas as pd
import quantstats as qs


def get_data(tickers):
    data = yf.download(tickers, interval='1mo')['Adj Close']
    returns = data.pct_change().dropna()
    return data, returns


def main():
    st.title('Visualização de Ações')

    st.write('Selecione as ações que você deseja visualizar:')
    tickers = st.multiselect('Tickers', ['ITUB3.SA', 'PETR4.SA', 'VALE3.SA'])

    if tickers:
        data, returns = get_data(tickers)

        qs.extend_pandas()
        returns.plot_monthly_heatmap()

        st.write('### Dados de Preços')
        st.write(data)

        st.write('### Dados de Retornos')
        st.write(returns)

if __name__ == '__main__':
    main()
