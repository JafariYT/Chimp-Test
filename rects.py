import pygame

def num1rectget(num1, WIDTH, HEIGHT, loc):
    return num1.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[1],   (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[0])))

def num2rectget(num2, WIDTH, HEIGHT, loc):
    return num2.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[3],   (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[2])))

def num3rectget(num3, WIDTH, HEIGHT, loc):
    return num3.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[5],   (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[4])))

def num4rectget(num4, WIDTH, HEIGHT, loc):
    return num4.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[7],   (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[6])))

def num5rectget(num5, WIDTH, HEIGHT, loc):
    return num5.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[9],   (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[8])))

def num6rectget(num6, WIDTH, HEIGHT, loc):
    return num6.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[11],  (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[10])))

def num7rectget(num7, WIDTH, HEIGHT, loc):
    return num7.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[13],  (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[12])))

def num8rectget(num8, WIDTH, HEIGHT, loc):
    return num8.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[15],  (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[14])))

def num9rectget(num9, WIDTH, HEIGHT, loc):
    return num9.get_rect(topleft=(((WIDTH - WIDTH/20) // 2) + WIDTH/20*1.05*loc[17],  (((HEIGHT - WIDTH/20) // 2) + WIDTH/20*1.05/2 + WIDTH/20*1.05*loc[16])))
