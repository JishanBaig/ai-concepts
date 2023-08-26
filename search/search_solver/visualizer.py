from PIL import Image, ImageDraw


class Visualizer:
    @staticmethod
    def visualize(space, solution):
        actions, cells = solution if solution else (None, None)
        print()
        for i, row in enumerate(space.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == space.get_start():
                    print("A", end="")
                elif (i, j) == space.get_goal():
                    print("B", end="")
                elif cells is not None and (i, j) in cells:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def output_image(space, solution, filename="maze.png"):
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (space.width * cell_size, space.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        actions, cells = solution if solution else (None, None)
        for i, row in enumerate(space.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == space.get_start():
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == space.get_goal():
                    fill = (0, 171, 28)

                # Solution path
                elif cells is not None and (i, j) in cells:
                    fill = (220, 235, 113)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)
