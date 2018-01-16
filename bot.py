import bot_func
import time

def main():
    dic = bot_2_1.get_updates()
    nl = len(dic['result'])
    text = ''
    print(nl)
    while(text != '1!=1'):
        dic = bot_2_1.get_updates()
        n = len(dic['result'])
        if(n>nl):
            print('я попал в if')
            nl = n
            d = bot_2_1.resend_message()
            text = d['text']
        time.sleep(1)
    print('exit')

if __name__ == '__main__':
    main()