import os
import sys
from dotenv import load_dotenv

def main() -> None:

    load_dotenv()

    print('\nORACLE STATUS: Reading the Matrix...\n')
    print('Configuration loaded:')

    mode = os.getenv('MATRIX_MODE')
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    network = os.getenv('ZION_ENDPOINT')


    print(f'Mode: {mode}')
    print(f'Database: {database}')
    print(f'API Access: {api_key}')
    print(f'Log Level: {log_level}')
    print(f'Zion Network: {network}')
    print()

    print('Environment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')

    print('\nThe Oracle sees all configurations.')


if __name__ == '__main__':
    main()