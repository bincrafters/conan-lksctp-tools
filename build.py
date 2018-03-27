#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    extended_builds = copy.deepcopy(builder)
    for settings, options, env_vars, build_requires, _ in extended_builds.items:
        options["lksctp-tools:with_sctp"] = True
        builder.add(settings=settings, options=options, env_vars=env_vars, build_requires=build_requires)
    builder.run()
