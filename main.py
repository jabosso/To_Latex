from os import listdir


def lettoreditag(s, tag):
    index = 0
    if tag in s:
        c = tag[0]
        for ch in s:
            if (ch == c) and (s[index:index + len(tag)] == tag):
                return index
            index += 1
    return -1


def spacecolapse(s):
    h = 0
    while ("	" in s) and (h < len(s)):
        h = h + 1
        x = lettoreditag(s, "	")
        s = s[:x] + "" + s[x + 1:]
    return s


def deletelast(namefi):
    output = open(namefi, "r")
    lines = output.readlines()
    output.close()
    output = open(namefi, "w+")
    output.writelines([item for item in lines[:-1]])
    output.close()


# if __name__ == '__main__':
def mama(name_file):
    input_file = "quizoriginali/" + name_file
    output_file = "quiz/" + name_file
    # --------------------------- VARIABILI DECISIONALI ----------------------------------------#
    opzioni = False
    quiz = False
    test = False
    mathmod = False
    # ----------------------------VARIABILI DI TRADUZIONE---------------------------------------#
    q_code = "quiz-desc"
    o_code = "quiz-risposte"
    t_code = "quiz-box"
    outputfile = open(output_file, "w+")
    diz = ["<div>", "</div>", "<h3>", "</h3>", "<li>", "</li>", "</ol>"]
    # -------------------------------------------------------------------------------------------#
    with open(input_file, 'r') as archivie:
        for cnt, line in enumerate(archivie):
            if t_code in line:
                line = ""
                if test:
                    outputfile.writelines("\n")
                    outputfile.write("\end{enumerate}")
                    outputfile.writelines("\n")
                    outputfile.write("\\begin{enumerate}")
                else:
                    test = True
                    # outputfile.write("\\begin{enumerate}")
            elif "<li>" in line:
                outputfile.writelines("\n")
                outputfile.write("\item")
                line = line.replace("<li>", "")
            elif q_code in line:
                line = line.replace('< class="quiz-desc">', "")
                line = line.replace('<div class="quiz-desc">', "")
                if opzioni:
                    outputfile.writelines("\n")
                    outputfile.close()
                    deletelast(output_file)
                    outputfile = open(output_file, "a+")
                    outputfile.write("\end{enumerate}")
                    opzioni = False
                outputfile.write("\large")
                outputfile.write(" \leftskip=0cm")
                outputfile.writelines("\n")
                outputfile.write("\item")


            elif o_code in line:
                line = line.replace('<ol type="a" class="quiz-risposte">', "")
                outputfile.writelines("\n")
                outputfile.write(" \small")
                outputfile.write("\\begin{enumerate}[A)]")
                outputfile.write("\leftskip=1cm")
                opzioni = True
            else:
                for element in diz:
                    inizio = lettoreditag(line, element)
                    if inizio > 0:
                        if element == "<h3>":
                            outputfile.write("\\\[0.2in]")
                            line = line.replace("<h3>", "\\textbf{")
                        elif element == "</h3>":
                            line = line.replace("</h3>", "}")
                        else:
                            line = line[:inizio] + line[inizio + len(element):]

            line = spacecolapse(line)
            # outputfile.write(len(line))
            line = line.replace("	", "")
            line = line.replace("\n", "")
            line = line.replace("&nbsp;", "")
            line = line.replace("<br>", "\\\\")
            if mathmod == False:
                line = line.replace("_", ".")

            if len(line) > 2:
                outputfile.writelines("\n")
                outputfile.write(line)
    outputfile.write("\end{enumerate}")
    # outputfile.write("\end{enumerate} ")
    outputfile.close()


if __name__ == '__main__':
    list_files = listdir("quizoriginali/")
    print(list_files)
    for element in list_files:
        mama(element)

