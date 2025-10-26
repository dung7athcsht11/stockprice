from vnstock import Vnstock
import pandas as pd
import datetime as dt
import os

def download_vn_stocks(symbols):
    today = dt.datetime.today().strftime("%Y-%m-%d")

    save_dir = r"C:/Users/ADMIN/Stock-Price/notebook/datack"
    os.makedirs(save_dir, exist_ok=True)

    for symbol in symbols:
        try:
            print(f"Downloading {symbol}...")

            # Khởi tạo đối tượng cổ phiếu (module mới của vnstock 3.x)
            stock = Vnstock().stock(symbol=symbol, source='VCI')

            # Lấy dữ liệu lịch sử từ 2015 đến nay
            df = stock.quote.history(
                start="2015-01-01",
                end=today,
                interval="1D"    # dữ liệu ngày
            )

            if df is None or df.empty:
                print(f"No data for {symbol}")
                continue

            # Giữ lại các cột chính
            df = df.rename(columns={
                'time': 'Date',
                'open': 'Open',
                'high': 'High',
                'low': 'Low',
                'close': 'Close'
            })[['Date', 'Open', 'High', 'Low', 'Close']]

            # Thêm cột index ngược
            df.insert(0, '', range(len(df), 0, -1))

            # Lưu file CSV
            file_path = os.path.join(save_dir, f"stock_market_data-{symbol}_{today}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8')

            print(f"Downloaded {symbol} to {file_path}")

        except Exception as e:
            print(f"Error {symbol}: {e}")

if __name__ == "__main__":
    symbols = [
    "VCB", "BID", "CTG", "TCB", "VPB", "MBB", "ACB", "HDB", "TPB", "STB",
    "EIB", "SHB", "LPB", "VIB", "OCB", "NAB", "BAB",
    "VIC", "VHM", "NVL", "PDR", "KDH", "DXG", "NLG", "HDG", "DIG", "HBC",
    "SCR", "CII", "TDC", "HDC", "TTB", "CRE",
    "HPG", "HSG", "GEX", "REE", "DQC", "VGC", "BMP", "AAA", "VCS", "BWE",
    "PVT", "GMD", "HAH", "VSC", "VTO",
    "GAS", "PLX", "POW", "BSR", "PVD", "PVS", "PVC", "OIL",
    "VNM", "MWG", "FPT", "SAB", "PNJ", "MSN", "KDC", "VRE", "HVN", "VJC",
    "AST", "DGW", "BHN", "SCS",
    "DPM", "DCM", "LTG", "QNS", "PAN", "VAF", "TSC", "NSC", "SBT", "BFC",
    "SSI", "VND", "VCI", "HCM", "FTS", "ORS", "MBS", "SHS", "BVS", "TVS",
    "APS", "CTS", "VIX", "AGR", "FPTS"
]

    download_vn_stocks(symbols)
