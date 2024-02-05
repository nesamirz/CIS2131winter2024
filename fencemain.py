def calculate_posts_length(length, width, post_distance):
    perimeter = 2 * (length + width)
    num_posts = int(perimeter / post_distance)
    return num_posts


def calculate_boards_length(length, board_length):
    num_boards = int(length / board_length)
    return num_boards


def main():
    length = float(input("Enter the length of the fenced area: "))
    width = float(input("Enter the width of the fenced area: "))
    post_distance = float(input("Enter the distance between posts: "))

    if (length % post_distance != 0) or (width % post_distance != 0):
        print("Error: The distance between posts should be evenly divisible by the fenced area's length and width.")
        return
    elif post_distance <= 0:
        print("Error: The distance between posts should be a positive value.")
        return

    num_posts = calculate_posts_length(length, width, post_distance)

    board_length = float(input("Enter the length of the boards: "))

    if board_length < post_distance:
        print("Error: Board length should be greater than or equal to post distance.")
        return

    num_boards_single = calculate_boards_length(length, board_length)

    boards_per_post = int(input("Enter the number of boards to run across each post: "))

    post_cost = float(input("Enter the cost of each post: "))
    board_cost = float(input("Enter the cost of each board: "))

    total_post_cost = num_posts * post_cost
    total_board_cost = num_boards_single * boards_per_post * board_cost
    grand_total = total_post_cost + total_board_cost

    print("\nResults:")
    print(f"Total number of posts required: {num_posts}")
    print(f"Total number of boards required: {num_boards_single * boards_per_post}")
    print(f"Total cost of posts: ${total_post_cost}")
    print(f"Total cost of boards: ${total_board_cost}")
    print(f"Grand total for the project: ${grand_total}")


if __name__ == "__main__":
    main()