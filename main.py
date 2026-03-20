from medical_device_processor import DeviceAnalyzer
from normalizer import StatusNormalizer
import pandas as pd


def main():
    raw_df = pd.read_excel('medical_diagnostic_devices_10000.xlsx')

    normalizer = StatusNormalizer()
    analyzer = DeviceAnalyzer(raw_df)

    raw_df['status'] = raw_df['status'].apply(normalizer.normalize)

    analyzer.set_df(raw_df)

    analyzer.normalize_dates()

    stats = analyzer.get_calibration_stats()

    print(f"Статистика калибровки: {stats}")

    print("\nСводная таблица:")
    print(analyzer.get_clinic_pivot())

if __name__ == "__main__":
    main()