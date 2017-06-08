FROM python:3-onbuild

ENTRYPOINT [ "python", "-W ignore", "./analyzer.py" ]
CMD []