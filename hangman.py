def hangman(word):                      # 関数 hangman,引数 word
    wrong=0                             # 何回間違えたかを数える変数
    stages=["",                         # 文字列のリスト、この文字列を使って吊られた人の絵を描いていく 
            "________        ",
            "|               ",
            "|        |      ",
            "|       頭      ",
            "|      手|手    ",
            "|      足 足    ",
            "|               "
             ]
    rletters = list(word)               # wordの文字を1文字ずつの要素の分解してリストにしたもの
    board = ["_"] * len(word)           # 文字列のリスト、プレーヤー2に見せるヒントを記憶しておく
    win = False
    print("ハングマンにようこそ！")

    # ゲームの手順を進めるループ処理
    while wrong<len(stages)-1:          # 変数wrongの値がlen(stages)-1より小さい間、繰り返す
        print("\n")                     # wrongはプレーヤー2がこれまで間違えた回数が記録されている
        msg="1文字を予想する"            # リストstagesの要素数と同じ回数間違えたら、ループは終了する
        char=input(msg)                 # プレーヤー2の回答入力を変数charに割り当て。
        if char in rletters:
            cind =rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け、正解は{}です.".format(word))

hangman("cat")