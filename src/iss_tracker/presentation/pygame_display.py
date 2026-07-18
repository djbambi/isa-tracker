import pygame

from iss_tracker.adapters.open_notify import get_screen_data

def run() -> None:

    pygame.init()
    screen = pygame.display.set_mode((640, 320))
    pygame.display.set_caption("hello pygame")
    clock = pygame.time.Clock()
    running = True
    screen_data = get_screen_data()
    font = pygame.font.SysFont("monospace", 16)
    lat = font.render(f"Latitude:     {str(screen_data.latitude)}", True, (0, 255, 100))
    lon = font.render(f"Longitude:    {str(screen_data.longitude)}", True, (0, 255, 100))
    reg = font.render(f"Region:       {str(screen_data.region)}", True, (0, 255, 100))
    next_vis = font.render(f"Next Visible: {str(screen_data.next_visible)}", True, (0, 255, 100))
    when = font.render(f"Time Stamp:   {str(screen_data.timestamp)}", True, (0, 255, 100))



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(lat, (10, 10))
        screen.blit(lon, (10, 40))
        screen.blit(reg, (10, 70))
        screen.blit(next_vis, (10, 100))
        screen.blit(when, (10, 130))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    run()
