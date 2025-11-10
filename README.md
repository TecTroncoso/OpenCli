# OpenCLI

[![Commit Activity](https://img.shields.io/github/commit-activity/w/your-username/open-cli)](https://github.com/your-username/open-cli/graphs/commit-activity)
[![Checks](https://img.shields.io/github/check-runs/your-username/open-cli/main)](https://github.com/your-username/open-cli/actions)
[![Version](https://img.shields.io/pypi/v/open_cli)](https://pypi.org/project/open_cli/)
[![Downloads](https://img.shields.io/pypi/dw/open_cli)](https://pypistats.org/packages/open_cli)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/your-username/open-cli)

OpenCLI is a new CLI agent that can help you with your software development tasks and terminal operations.

> [!IMPORTANT]
> OpenCLI is currently in technical preview.

## Key features

- Shell-like UI and shell command execution
- Zsh integration
- [Agent Client Protocol] support
- MCP support
- And more to come...

[Agent Client Protocol]: https://github.com/agentclientprotocol/agent-client-protocol

## Installation

OpenCLI is published as a Python package on PyPI. We highly recommend installing it with [uv](https://docs.astral.sh/uv/). If you have not installed uv yet, please follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/) to install it first.

Once uv is installed, you can install OpenCLI with:

```sh
uv tool install --python 3.13 open_cli
```

Run `opencli --help` to check if OpenCLI is installed successfully.

> [!IMPORTANT]
> Due to the security checks on macOS, the first time you run `opencli` command may take 10 seconds or more depending on your system environment.

## Upgrading

Upgrade OpenCLI to the latest version with:

```sh
uv tool upgrade open_cli --no-cache
```

## Usage

Run `opencli` command in the directory you want to work on, then send `/setup` to setup OpenCLI:

![](./docs/images/setup.png)

After setup, OpenCLI will be ready to use. You can send `/help` to get more information.

## Features

### Shell mode

OpenCLI is not only a coding agent, but also a shell. You can switch the mode by pressing `Ctrl-X`. In shell mode, you can directly run shell commands without leaving OpenCLI.

> [!NOTE]
> Built-in shell commands like `cd` are not supported yet.

### Zsh integration

You can use OpenCLI together with Zsh, to empower your shell experience with AI agent capabilities.

Install the [zsh-open-cli](https://github.com/your-username/zsh-open-cli) plugin via:

```sh
git clone https://github.com/your-username/zsh-open-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/open-cli
```

> [!NOTE]
> If you are using a plugin manager other than Oh My Zsh, you may need to refer to the plugin's README for installation instructions.

Then add `open-cli` to your Zsh plugin list in `~/.zshrc`:

```sh
plugins=(... open-cli)
```

After restarting Zsh, you can switch to agent mode by pressing `Ctrl-X`.

### ACP support

OpenCLI supports [Agent Client Protocol] out of the box. You can use it together with any ACP-compatible editor or IDE.

For example, to use OpenCLI with [Zed](https://zed.dev/), add the following configuration to your `~/.config/zed/settings.json`:

```json
{
  "agent_servers": {
    "OpenCLI": {
      "command": "opencli",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

Then you can create OpenCLI threads in Zed's agent panel.

### Using MCP tools

OpenCLI supports the well-established MCP config convention. For example:

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Run `opencli` with `--mcp-config-file` option to connect to the specified MCP servers:

```sh
opencli --mcp-config-file /path/to/mcp.json
```

## Development

To develop OpenCLI, run:

```sh
git clone https://github.com/your-username/open-cli.git
cd open-cli

make prepare  # prepare the development environment
```

Then you can start working on OpenCLI.

Refer to the following commands after you make changes:

```sh
uv run opencli  # run OpenCLI

make format  # format code
make check  # run linting and type checking
make test  # run tests
make help  # show all make targets
```

## Contributing

We welcome contributions to OpenCLI! Please refer to [CONTRIBUTING.md](./CONTRIBUTING.md) for more information.
