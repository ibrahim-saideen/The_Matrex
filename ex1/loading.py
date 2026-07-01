from importlib.metadata import version
import sys


def main() -> None:

    print('LOADING STATUS: Loading programs...')
    print('\nChecking dependencies:')
    x = False

    try:
        import pandas
        print(f'[OK] pandas {version('pandas')} '
            '- Data manipulation ready')
    except Exception:
        print('[KO] pandas not installed yet')
        x = True

    try:
        import numpy
        print(f'[OK] numpy {version('numpy')} '
            '- Numerical computation ready')
    except Exception:
        print('[KO] numpy not installed yet')
        x = True

    try:
        import matplotlib.pyplot as plt
        print(f'[OK] matplotlib {version('matplotlib')} '
            '- Visualization ready')
    except Exception:
        print('[KO] matplotlib not installed yet')
        x = True

    if x:
        print('\nInstall all the required packages:')
        print('use one of:')
        print('pip install -r requirements.txt')
        print('poetry install')
        sys.exit()

    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualization...')

    data = numpy.random.randint(0, 100, size=1000)
    df = pandas.DataFrame(data, columns=['signal'])
    plt.plot(df['signal'])
    plt.savefig("data.png")

    print('\nAnalysis complete!')
    print('Results saved to: data.png')

if __name__ == '__main__':
    main()
