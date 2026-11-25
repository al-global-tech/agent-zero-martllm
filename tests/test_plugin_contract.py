"""Offline checks for the martllm_provider plugin. Run: python tests/test_plugin_contract.py"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load(rel):
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


def test_manifest():
    m = load("plugin.yaml")
    assert m["name"] == "martllm_provider" and re.fullmatch(r"[a-z0-9_]+", m["name"])
    assert all(isinstance(m.get(k), str) and m[k].strip() for k in ("title", "description", "version"))
    assert "always_enabled" not in m


def test_provider_entry():
    cfg = load("conf/model_providers.yaml")
    assert set(cfg) == {"chat"} and set(cfg["chat"]) == {"martllm"}
    e = cfg["chat"]["martllm"]
    assert e["name"] == "MartLLM" and e["litellm_provider"] == "openai"
    assert e["kwargs"] == {"a0_api_mode": "chat", "api_base": "https://api.martllm.com/v1"}
    assert e["models_list"] == {"endpoint_url": "https://api.martllm.com/v1/models"}


def test_maker_prefix_survives():
    lp = load("conf/model_providers.yaml")["chat"]["martllm"]["litellm_provider"]
    assert f"{lp}/deepseek/deepseek-v4-flash".split("/", 1)[1] == "deepseek/deepseek-v4-flash"


def test_config_only_no_secrets():
    for f in ("hooks.py", "execute.py", ".env"):
        assert not (ROOT / f).exists()
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.suffix in (".yaml", ".md", ".py"):
            assert not re.search(r"\bsk-[A-Za-z0-9_-]{16,}", p.read_text(encoding="utf-8")), p


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
