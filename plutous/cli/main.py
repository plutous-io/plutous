from typer import Typer

app = Typer()
apps = []

try:
    from plutous.trade.cli import main as trade

    apps.append(trade.app)
except ImportError:
    pass

for a in apps:
    app.add_typer(a)


@app.command()
def start_server(
    host: str = "0.0.0.0",
    port: int = 8080,
    # reload: bool = True,
    # reload_dirs: list = ["plutous"],
):
    import uvicorn

    from plutous.app.main import app

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    app()
