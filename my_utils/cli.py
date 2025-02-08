#!/usr/bin/env python
import argparse

from core import format_base64, generate_qr  # функции из бизнес-логики


def main():
    parser = argparse.ArgumentParser(
        prog='my_utils',
        description='Набор утилит: генерация QR-кодов, форматирование Base64 и др.',
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Подкоманда для генерации QR
    parser_qr = subparsers.add_parser('generate_qr', help='Генерация QR-кода из текста')
    parser_qr.add_argument('text', help='Текст для кодирования в QR')

    # Подкоманда для форматирования Base64
    parser_b64 = subparsers.add_parser('format_base64', help='Форматирование Base64 строки')
    parser_b64.add_argument('input', help='Исходная строка Base64')

    args = parser.parse_args()

    if args.command == 'generate_qr':
        # Предположим, функция генерирует файл или возвращает путь к картинке
        result = generate_qr(args.text)
        print(f'QR-код создан: {result}')
    elif args.command == 'format_base64':
        result = format_base64(args.input)
        print(f'Отформатированная строка: {result}')


if __name__ == '__main__':
    main()
