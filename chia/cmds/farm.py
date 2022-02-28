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
        Set the level of detail to display for staking information.
        Higher detail levels will make this command run slower.
        0 - Don't show staking information (default).
        1 - Show staking addresses.
        2 - Show staking addresses plus staked coins per address.
        3 - Show staking addresses plus staked coins and plot count per address."""
    ),
    type=int,
    default=0
)
def summary_cmd(
    rpc_port: Optional[int],
    wallet_rpc_port: Optional[int],
    harvester_rpc_port: Optional[int],
    farmer_rpc_port: Optional[int],
    staking_detail: Optional[int],
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
