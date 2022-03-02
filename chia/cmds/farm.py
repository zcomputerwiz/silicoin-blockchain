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
    "-sa",
    "--staking-addresses",
    help=(
        """\b
        Fetch staking addresses and cache them to
        always be shown when running 'farm summary'.
        You must rerun this command option when
        adding/removing keys or plots to update the
        cache, even across restarts.
        
        \b
        n - Clear staking address cache.
        k - Fetch staking addresses from keys. Does
            not show plot counts.
        p - Fetch staking addresses from plots. Does
            not show staking addresses for keys
            without plots.
        a - Fetch staking addresses from keys and
            plots. Shows plot counts and addresses
            for keys without plots."""
    ),
    type=str,
    default=None,
    show_default=True,
)
@click.option(
    "-sb",
    "--staking-balance",
    help=(
        """\b
        Show the balance of each staking address.
        Requires staking info to be cached by
        -sa/--staking-addresses beforehand."""
    ),
    is_flag=True,
    type=bool,
    default=False
)
def summary_cmd(
    rpc_port: Optional[int],
    wallet_rpc_port: Optional[int],
    harvester_rpc_port: Optional[int],
    farmer_rpc_port: Optional[int],
    staking_addresses: Optional[str],
    staking_balance: Optional[bool],
) -> None:
    from .farm_funcs import summary
    import asyncio

    asyncio.run(summary(rpc_port, wallet_rpc_port, harvester_rpc_port, farmer_rpc_port, staking_addresses, staking_balance))


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
