import os
import pandas as pd


def collect_unique_wallets(folder_path):
    wallet_addresses = set()  # Используем set для автоматического удаления дубликатов

    # Проходим по всем файлам в указанной папке
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):  # Проверяем, что это Excel файл
            file_path = os.path.join(folder_path, file_name)

            # Загружаем Excel файл и ищем столбец "Wallet Address"
            try:
                df = pd.read_excel(file_path)
                if 'Wallet Address' in df.columns:
                    # Добавляем все уникальные кошельки в множество
                    wallet_addresses.update(df['Wallet Address'].dropna().unique())
                    print(f"Обработан файл: {file_name}")
                else:
                    print(f"Внимание: столбец 'Wallet Address' не найден в файле {file_name}")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")

    return wallet_addresses


def save_wallets_to_txt(wallet_addresses, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for address in wallet_addresses:
            f.write(f"{address}\n")
    print(f"Файл сохранён на рабочем столе: {output_path}")


if __name__ == "__main__":
    folder_path = '/Users/danferat/Desktop/Лудомания/сортировка по миграционке'


    # Сбор уникальных кошельков
    wallet_addresses = collect_unique_wallets(folder_path)

    # Определение пути для сохранения файла на рабочем столе
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file_path = os.path.join(desktop_path, "unique_wallet_addresses.txt")

    # Сохранение результата в файл
    save_wallets_to_txt(wallet_addresses, output_file_path)
