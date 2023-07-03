import yfinance as yf


def get_exchange_rate(base_currency, target_currency):
    ticker = f"{base_currency}{target_currency}=X"
    data = yf.download(tickers=ticker, period='1d')
    rate = data["Close"].iloc[-1]
    return rate


def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount


def main():
    base_currency = "BRL"  # Real brasileiro
    target_currency = "USD"  # Dólar americano

    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency)

        amount_brl = float(input("Digite o valor em reais (BRL): "))
        converted_to_usd = convert_currency(amount_brl, exchange_rate)
        print(f"R$ {amount_brl} = US$ {converted_to_usd:.2f}")

        amount_usd = float(input("Digite o valor em dólares (USD): "))
        converted_to_brl = convert_currency(amount_usd, 1/exchange_rate)
        print(f"US$ {amount_usd} = R$ {converted_to_brl:.2f}")

    except Exception as e:
        print(f"Ocorreu um erro ao obter a taxa de câmbio: {str(e)}")


if __name__ == "__main__":
    main()
