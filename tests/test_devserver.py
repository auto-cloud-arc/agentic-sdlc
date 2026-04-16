import pytest

from forgeops_orchestrator import devserver


def test_resolve_port_prefers_default_port() -> None:
    port = devserver.resolve_port(
        "127.0.0.1",
        requested_port=None,
        availability_check=lambda _host, candidate: candidate == devserver.DEFAULT_PORT,
    )

    assert port == devserver.DEFAULT_PORT


def test_resolve_port_falls_back_to_8001(capsys: pytest.CaptureFixture[str]) -> None:
    port = devserver.resolve_port(
        "127.0.0.1",
        requested_port=None,
        availability_check=lambda _host, candidate: candidate == devserver.FALLBACK_PORT,
    )

    assert port == devserver.FALLBACK_PORT
    assert f"Port {devserver.DEFAULT_PORT} is unavailable" in capsys.readouterr().out


def test_resolve_port_honors_requested_port() -> None:
    port = devserver.resolve_port(
        "127.0.0.1",
        requested_port=8010,
        availability_check=lambda _host, candidate: candidate == 8010,
    )

    assert port == 8010


def test_resolve_port_raises_for_unavailable_requested_port() -> None:
    with pytest.raises(RuntimeError, match="Choose another port with --port"):
        devserver.resolve_port(
            "127.0.0.1",
            requested_port=8010,
            availability_check=lambda _host, _candidate: False,
        )