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

if __name__ == "__main__":
    app()
