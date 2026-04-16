from __future__ import annotations

import argparse
import os
import socket
from collections.abc import Callable, Sequence

import uvicorn

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
FALLBACK_PORT = 8001


def parse_port(value: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Port must be an integer.") from exc

    if not 0 < port < 65536:
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535.")

    return port


def port_is_available(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            sock.bind((host, port))
        except OSError:
            return False

    return True


def resolve_port(
    host: str,
    requested_port: int | None,
    availability_check: Callable[[str, int], bool] = port_is_available,
) -> int:
    if requested_port is not None:
        if availability_check(host, requested_port):
            return requested_port

        raise RuntimeError(
            f"Port {requested_port} is unavailable on {host}. Choose another port with --port."
        )

    env_port = os.getenv("PORT")
    if env_port:
        resolved_port = parse_port(env_port)
        if availability_check(host, resolved_port):
            return resolved_port

        raise RuntimeError(
            f"Port {resolved_port} from PORT is unavailable on {host}. Choose another port with --port."
        )

    if availability_check(host, DEFAULT_PORT):
        return DEFAULT_PORT

    if availability_check(host, FALLBACK_PORT):
        print(f"Port {DEFAULT_PORT} is unavailable; starting on {FALLBACK_PORT} instead.")
        return FALLBACK_PORT

    raise RuntimeError(
        f"Ports {DEFAULT_PORT} and {FALLBACK_PORT} are unavailable on {host}. Choose another port with --port."
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Start the ForgeOps Maintenance Orchestrator development server."
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host interface to bind to.")
    parser.add_argument(
        "--port",
        type=parse_port,
        default=None,
        help="Port to bind to. Defaults to 8000, with automatic fallback to 8001.",
    )
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        port = resolve_port(args.host, args.port)
    except RuntimeError as exc:
        parser.error(str(exc))

    print(f"Starting ForgeOps API at http://{args.host}:{port}")

    uvicorn_kwargs: dict[str, object] = {
        "host": args.host,
        "port": port,
        "reload": args.reload,
    }
    if args.reload:
        uvicorn_kwargs["reload_dirs"] = ["."]

    uvicorn.run("forgeops_orchestrator.main:app", **uvicorn_kwargs)
    return 0