#!/bin/bash
uv python install 3.12.7
uv python pin 3.12.7
uv init --bare
uv add numpy scipy matplotlib otter-grader nbconvert ipykernel ipympl
