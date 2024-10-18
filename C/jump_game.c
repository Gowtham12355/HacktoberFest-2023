#include <SDL.h>
#include <stdio.h>
#include <stdbool.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600
#define GRAVITY 0.5
#define JUMP_FORCE -15

typedef struct {
    SDL_Rect rect;
    float velocityY;
    bool isJumping;
} Player;

void handleInput(SDL_Event event, Player *player) {
    const Uint8 *state = SDL_GetKeyboardState(NULL);
    if (state[SDL_SCANCODE_SPACE] && !player->isJumping) {
        player->velocityY = JUMP_FORCE;
        player->isJumping = true;
    }
}

void updatePlayer(Player *player) {
    player->velocityY += GRAVITY;
    player->rect.y += (int)player->velocityY;

    if (player->rect.y >= WINDOW_HEIGHT - player->rect.h) {
        player->rect.y = WINDOW_HEIGHT - player->rect.h;
        player->isJumping = false;
        player->velocityY = 0;
    }
}

void renderPlayer(SDL_Renderer *renderer, Player *player) {
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
    SDL_RenderFillRect(renderer, &player->rect);
}

int main(int argc, char *argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("Jumping Game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    
    Player player = { .rect = { 50, WINDOW_HEIGHT - 100, 50, 50 }, .velocityY = 0, .isJumping = false };

    bool running = true;
    SDL_Event event;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
            handleInput(event, &player);
        }

        updatePlayer(&player);

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        renderPlayer(renderer, &player);
        SDL_RenderPresent(renderer);

        SDL_Delay(16);  // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
