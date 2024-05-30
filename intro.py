import pgzrun

# Definir o ator alienígena
alien = Actor('alien')
alien.pos = 100, 56

# Configurar a posição inicial do alienígena
alien.topright = 0, 10

# Configurar a largura e a altura da tela
WIDTH = 500
HEIGHT = alien.height + 300

# Função para desenhar na tela
def draw():
    screen.clear()
    alien.draw()

# Função para atualizar a posição do alienígena
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

# Função que trata o clique do mouse
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

# Função que define o estado machucado do alienígena
def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)
    print('Eek')

# Função que redefine o alienígena ao estado normal
def set_alien_normal():
    alien.image = 'alien'

# Rodar o jogo
pgzrun.go()
