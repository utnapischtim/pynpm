# SPDX-FileCopyrightText: 2017 CERN.
# SPDX-FileCopyrightText: 2023 Rambaud Pierrick.
# SPDX-License-Identifier: BSD-3-Clause

"""Utility function to run NPM."""

from __future__ import absolute_import, print_function

import subprocess


def run_npm(pkgdir, cmd, args=None, npm_bin="npm", wait=True, shell=False):
    """Run NPM."""
    command = [npm_bin, cmd] + list(args)
    if wait:
        return subprocess.call(
            command,
            cwd=pkgdir,
            shell=shell,
        )
    else:
        return subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=pkgdir,
            shell=shell,
        )
