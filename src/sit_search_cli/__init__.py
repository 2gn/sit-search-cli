from argparse import ArgumentParser
from pdb import set_trace
from rich.console import Console
from rich.table import Table

from .api import search

console = Console()

parser = ArgumentParser()

parser.add_argument('query')

parser.add_argument('-l', '--locale', default="jp")

args = parser.parse_args()


def main() -> int:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Type")
    table.add_column("Authors", justify="right")
    table.add_column("Language", justify="right")

    tasks = ["Fetching results", "Creating a fancy table", "Complete"]

    with console.status("Loading results...") as status:
        while tasks:
            console.log(tasks.pop(0))
            result = search(args.query)
            console.log(tasks.pop(0))
            for item in result:
                table.add_row(
                    " ".join(item["publication_years"]),
                    item["full_title"].replace("<mark>", "[bold red]").replace("</mark>", "[/bold red]"),
                    item["content_types"][0],
                    " & ".join([ author["fullname"] for author in item["authors"]]),
                    " ".join(item["languages"])
                )
            console.log(tasks.pop(0))

    console.print(table)
    return 0