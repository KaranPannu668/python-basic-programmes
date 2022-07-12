def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Prints a string on screen if length is less than screen width

    Args:
        text (str, optional): The test to be printed. Defaults to " ".
        screen_width (int, optional): The width of the screen. Defaults to 80.

    Raises:
        ValueError: If the output string is larger than the screen width
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
    
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*",60)
banner_text("Always look on the bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(" ",60)
banner_text("When you're feeling in the dumps,",60)
banner_text(screen_width=60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life...",60)
banner_text("*",60)