import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            return True
        return False

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

def get_winning_score():
    font = pygame.font.SysFont(None, 74)
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            return int(text)
                        except ValueError:
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        score_text = font.render('Set Winning Score:', True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 100))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    paddle1 = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()
    
    score1 = 0
    score2 = 0
    game_over = False
    WINNING_SCORE = get_winning_score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.KEYDOWN:
                score1 = 0
                score2 = 0
                game_over = False
                ball.reset()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle1.move(-PADDLE_SPEED)
            if keys[pygame.K_s]:
                paddle1.move(PADDLE_SPEED)
            if keys[pygame.K_UP]:
                paddle2.move(-PADDLE_SPEED)
            if keys[pygame.K_DOWN]:
                paddle2.move(PADDLE_SPEED)

            if ball.move():
                if ball.rect.left <= 0:
                    score2 += 1
                else:
                    score1 += 1
                if score1 >= WINNING_SCORE or score2 >= WINNING_SCORE:
                    game_over = True
                ball.reset()

            if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
                ball.speed_x *= -1

            screen.fill(BLACK)
            paddle1.draw()
            paddle2.draw()
            ball.draw()

            font = pygame.font.SysFont(None, 74)
            score_text = font.render(f"{score1} : {score2}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

            if game_over:
                winner_text = "Player 1 Wins!" if score1 >= WINNING_SCORE else "Player 2 Wins!"
                game_over_text = font.render(f"{winner_text}", True, WHITE)
                restart_text = font.render("Press any key to restart", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
                screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()
