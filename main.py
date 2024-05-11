import click
from server import run_app


@click.command()
@click.option("--host", default="127.0.0.1", help="Host IP")
@click.option("--port", default=8080, help="Port number")
def main(host, port):
    run_app(host, port)


if __name__ == "__main__":
    main()
