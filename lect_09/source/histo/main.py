from ascii_art import Chart


def example_one():
    data = [1,2,3,4,3,12,4,16,18,15,5,5,10]
    c = Chart(data)
    print(c.render())


if __name__ == "__main__":
    example_one()
