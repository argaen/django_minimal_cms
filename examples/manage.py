#!/usr/bin/env python
import os
import sys

sys.path[0:0] = [os.path.abspath('..')]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examples.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
