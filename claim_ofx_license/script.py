import OrcFxAPI as ofx
import time

def run():
    start = time.time()
    count = 0
    while True:
        count += 1
        
        print(f'try: {count:0.0f}')
        try:
            model = ofx.Model()
            duration = time.time() - start
            print(f'Succes in {duration:0.0f} seconds! ({count:0.0f} tries)')
            
            break
        except ofx.DLLError:
            print('failed to open')

    input('press a key')