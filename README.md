# Hide Help Plugin
Customizable Tutor Plugin for Open edX

# Content
- [Hide Help Plugin](#hide-help-plugin)
- [Content](#content)
- [Setup](#setup)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Setup
> This is the `main` branch which is intended to be used for development purpose. Some bugs and unexpected behaviors will occur while installing from this branch.

1. Clone the git repository into `tutor plugins root` using the following command.
   ```bash
   git clone https://github.com/kylesinlynn/openedx/tutor-hide-help.git && mv "$(pwd)/tutor-hide-help/hide-help.py" "$(tutor plugins printroot)"
   ```

2. List the installed plugins.
   ```bash
   tutor plugins list
   ```

3. Enable the plugins if you found `hide-help` plugin.
   ```bash
   tutor plugins enable hide-help
   ```

# Troubleshooting
Create an issue upon your error that is associated with this project.

# Contributing
Feel free to fork and create pull requests. Your contribution will be appreciated.

# License
This project is licensed under [BSD License](LICENSE).