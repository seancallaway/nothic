import click


@click.group()
def main():
    """A utility for triggering actions based on matches in log files."""
    pass


@main.command()
def watch(**kwargs):
    """Watch a log file for matches and take action."""
    pass
