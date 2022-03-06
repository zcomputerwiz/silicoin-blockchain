from typing import Optional

import click


@click.group("farm", short_help="Manage your farm")
def farm_cmd() -> None:
    pass


@farm_cmd.command("summary", short_help="Summary of farming information")
@click.option(
    "-p",
    "--rpc-port",
    help=(
        "Set the port where the Full Node is hosting the RPC interface. "
        "See the rpc_port under full_node in config.yaml"
    ),
    type=int,
    default=None,
    show_default=True,
)
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
    show_default=True,
)
@click.option(
    "-hp",
    "--harvester-rpc-port",
    help=(
        "Set the port where the Harvester is hosting the RPC interface"
        "See the rpc_port under harvester in config.yaml"
    ),
    type=int,
    default=None,
    show_default=True,
)
@click.option(
    "-fp",
    "--farmer-rpc-port",
    help=(
        "Set the port where the Farmer is hosting the RPC interface. " "See the rpc_port under farmer in config.yaml"
    ),
    type=int,
    default=None,
    show_default=True,
)
@click.option(
    "-sd",
    "--staking-detail",
    help=(
        """\b
        Fetch a specific selection of staking
        information. Everything except for balances
        will be cached, and this cache will only be
        used when 'k' and 'p' aren't specified.
        
        \b
        Specify more than one of the following letters:
        n - Clear cache and don't show staking information.
        k - Fetch staking addresses from keys. Does
            not show plot counts.
        p - Fetch staking addresses from plots. Does
            not show staking addresses for keys
            without plots.
        b - Fetch staking balances from listed addresses.
        
        \b
        The default selection is "kpb"."""
    ),
    type=str,
    default="kpb",
    show_default=False,
)
def summary_cmd(
    rpc_port: Optional[int],
    wallet_rpc_port: Optional[int],
    harvester_rpc_port: Optional[int],
    farmer_rpc_port: Optional[int],
    staking_detail: Optional[str],
) -> None:
    from .farm_funcs import summary
    import asyncio

    asyncio.run(summary(rpc_port, wallet_rpc_port, harvester_rpc_port, farmer_rpc_port, staking_detail))


@farm_cmd.command("challenges", short_help="Show the latest challenges")
@click.option(
    "-fp",
    "--farmer-rpc-port",
    help="Set the port where the Farmer is hosting the RPC interface. See the rpc_port under farmer in config.yaml",
    type=int,
    default=None,
    show_default=True,
)
@click.option(
    "-l",
    "--limit",
    help="Limit the number of challenges shown. Use 0 to disable the limit",
    type=click.IntRange(0),
    default=20,
    show_default=True,
)
def challenges_cmd(farmer_rpc_port: Optional[int], limit: int) -> None:
    from .farm_funcs import challenges
    import asyncio

    asyncio.run(challenges(farmer_rpc_port, limit))
