
print('LOADING STATUS: Loading programs...')
print('Checking dependencies:\n')


try:
    import pandas
    print(f'[OK] pandas {pandas.__version__} '
          '- Data manipulation ready')
except Exception:
    print('[KO] can not import importlib '
          'install it first (ya 7arfosh) \n'
          'use:pip install')



try:
    from importlib.metadata import version
    print(f'[OK] importlib {version('importlib')} '
          '- Data manipulation ready')
except Exception:
    print('[KO] can not import importlib '
          'install it first (ya 7arfosh) '
          'pip install -r ')




