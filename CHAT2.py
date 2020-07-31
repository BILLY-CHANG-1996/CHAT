import os
#讀取文字檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig')as f:
        for line in f:
            lines.append(line.strip())
    return lines

#轉換文字檔
def convert(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_pic = 0
    viki_pic = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_pic += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_pic += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了', allen_word_count,'個字','傳了', allen_sticker_count, '個貼圖','及', allen_pic, '張圖片')
    print('Viki說了', viki_word_count, '個字','傳了', viki_sticker_count, '個貼圖','及', viki_pic, '張圖片')

        #print(s)c

#寫入文字檔
def write_file(filename, lines):
    with open(filename, 'w')as f:
        for line in lines:
            f.write(line + '\n')

#主程式
def main():
    lines = read_file('Line-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)   

#執行主程式
main()