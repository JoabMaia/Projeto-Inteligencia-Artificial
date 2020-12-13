import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

#InterfaceGrafica.py
import pygame

from Solucionador import resolver, valida,matriz_automatica, totaljogadasalgoritmo, quantidadedojogadasalgoritmo
import time
pygame.font.init()

listaquantidadejogadasalgoritmo = []

class Grid:
    #tabuleiro inicial
    board = matriz_automatica

    def __init__(self, linhas, colunas, largura, altura):
        self.linhas = linhas
        self.colunas = colunas
        self.cubes = [[Cube(self.board[i][j], i, j, largura, altura) for j in range(colunas)] for i in range(linhas)]
        self.largura = largura
        self.altura = altura
        self.modelo = None
        self.selecionado = None

    def atualiza_modelo(self):
        self.modelo = [[self.cubes[i][j].value for j in range(self.colunas)] for i in range(self.linhas)]

    def desenhar(self, win):
        # Desenhar linhas da grade
        gap = self.largura / 9
        for i in range(self.linhas + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.largura, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.altura), thick)

        # Desenhar Cubes
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.cubes[i][j].desenhar(win)

    def selecionador(self, linha, coluna):
        # Reiniciar todos os outros
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.cubes[i][j].selected = False

        self.cubes[linha][coluna].selected = True
        self.selecionado = (linha, coluna)

    def transparente(self):
        linha, coluna = self.selecionado
        if self.cubes[linha][coluna].value == 0:
            self.cubes[linha][coluna].conjunto_temp(0)

    def click(self, pos):
        if pos[0] < self.largura and pos[1] < self.altura:
            gap = self.largura / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def local(self, val):
        linha, coluna = self.selecionado
        if self.cubes[linha][coluna].value == 0:
            self.cubes[linha][coluna].conjunto(val)
            self.atualiza_modelo()

            if valida(self.modelo, val, (linha, coluna)) and resolver(self.modelo):
                return True
            else:
                self.cubes[linha][coluna].conjunto(0)
                self.cubes[linha][coluna].conjunto_temp(0)
                self.atualiza_modelo()
                return False

    def esboco(self, val):
        linha, coluna = self.selecionado
        self.cubes[linha][coluna].conjunto_temp(val)

    def esta_terminado(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    linhas = 9
    colunas = 9

    def __init__(self, value, linha, coluna, largura, altura):
        self.value = value
        self.temp = 0
        self.linha = linha
        self.coluna = coluna
        self.largura = largura
        self.altura = altura
        self.selected = False

    def desenhar(self, win):
        # definindo cores
        AZUL = (0, 0, 255)

        fnt = pygame.font.SysFont("arial", 40, bold=True)

        gap = self.largura / 9
        x = self.coluna * gap
        y = self.linha * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (AZUL), (x, y, gap , gap), 3)

    def conjunto(self, val):
        self.value = val

    def conjunto_temp(self, val):
        self.temp = val

def redesenhar_janela(win, board, time, error, hits):
    #definindo cores
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    VERDE = (0, 255, 0)
    VERMELHO = (255, 0, 0)
    CINZA = (141, 141, 141)
    win.fill(CINZA)
    #desenhar tempo
    fnt = pygame.font.SysFont("arial", 20, bold=True)
    text = fnt.render("Tempo =" + formato_tempo(time), 1, (0,0,0))
    win.blit(text, (710 - 160, 10))

    #540 #560
    text = fnt.render("IFPB-CG", 1, (PRETO))
    win.blit(text, (730 - 160, 200))

    text = fnt.render("Engenharia", 1, (PRETO))
    win.blit(text, (710 - 150, 230))

    text = fnt.render("de", 1, (PRETO))
    win.blit(text, (710 - 110, 260))

    text = fnt.render("Computação", 1, (PRETO))
    win.blit(text, (710 - 160, 290))

    text = fnt.render("Projeto de IA", 1, (PRETO))
    win.blit(text, (740 - 190, 320))

    text = fnt.render("Aluno:", 1, (PRETO))
    win.blit(text, (720 - 140, 350))

    text = fnt.render("Joab Maia", 1, (PRETO))
    win.blit(text, (720 - 160, 380))


    #desenhar error e hits
    text = fnt.render("Erros:"  + str(error), (PRETO), 1, (VERMELHO))
    win.blit(text, (15, 550))


    text = fnt.render("Acertos:" + str(hits),(PRETO), 1, (VERDE))
    win.blit(text, (15, 570))

    #desenhar quantidade de tentativas
    text = fnt.render("Total de jogadas do(a) jogador(a):" + str(error+hits), 1, (PRETO))
    win.blit(text, (210, 550))

    listaquantidadejogadasalgoritmo.append(quantidadedojogadasalgoritmo())
    text = fnt.render("Total de jogadas do algoritmo:" + str(listaquantidadejogadasalgoritmo[0]), 1, (PRETO))
    win.blit(text, (210, 570))

    if len(listaquantidadejogadasalgoritmo) >= 2:
        listaquantidadejogadasalgoritmo.pop()

    #desenhar grid e board
    board.desenhar(win)



def formato_tempo(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

#funcao principal
def main():
    win = pygame.display.set_mode((680,600))
    #Efeitos de sons
    pygame.init()
    pygame.mixer.music.set_volume(0.6)
    som_de_fundo = pygame.mixer.music.load("sonsdojogo/backgroundsound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.init()
    som_acerto = pygame.mixer.Sound("sonsdojogo/accept.mp3")
    som_erro = pygame.mixer.Sound("sonsdojogo/error.mp3")
    som_erro.set_volume(100)

    #540 #600
    pygame.display.set_caption("Jogo(Sudoku)")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    error = 0
    hits = 0
    print("Quantidade de jogadas realizadas pelo algoritmo:", totaljogadasalgoritmo())
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.transparente()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selecionado
                    if board.cubes[i][j].temp != 0:
                        if board.local(board.cubes[i][j].temp):
                            som_acerto.play()
                            print("Você acertou! Parabéns!")
                            #print(board.modelo)
                            hits += 1
                        else:
                            som_erro.play()
                            print("Você errou!")
                            error += 1
                        key = None

                        if board.esta_terminado():
                            print("Game over")
                            print("Quantidade de jogadas realizadas pelo jogador:", hits + error)
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.selecionador(clicked[0], clicked[1])
                    key = None

        if board.selecionado and key != None:
            board.esboco(key)

        redesenhar_janela(win, board, play_time, error, hits)
        pygame.display.update()


main()
pygame.quit()
